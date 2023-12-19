
# coding: utf-8

'''
This class implements necessary methods for generating annotation template files for annotation experiment. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

import pandas as pd
import numpy as np

import sys,os
packages_path = os.getcwd()
sys.path.append(packages_path.split('classes'+os.path.sep)[0])
from classes.Utils.PandasUtils import PandasUtils

class GenerateExperimentLabelFiles:
    def __init__(self,pickle_files,pickle_path,labels_path):
        self.pickle_files = pickle_files
        self.pickle_path = pickle_path
        self.labels_path = labels_path
    
    def retreive_first_element(self,s):
        if s:
            if isinstance(s,list):
                return s[0]
            else:
                return s
        else:
            return s

    def generate_label_files(self):
        for file in self.pickle_files:
            #file extension function necessary in this case
            try:
                df = PandasUtils.get_pickle_files_in_dataframe(self.pickle_path,[file])
            except:
                print('pickles do not exist')
            try:
                cell_count = df.shape[0]
                cell_type = list(df.cell_type.values) + ['','']
                starting_text = df.text.apply(self.retreive_first_element)
                starting_text = list(starting_text) + ['','']
                filename = file.split('.pkl')[0]
                filenames = ([filename]*cell_count) + ['confidence_percentage','notebook_score']
                cell_numbers = list(range(0,cell_count)) + ['','']   
                primary_label = ([''] * cell_count)+ ['',''] 
                load_data  = ([0] * cell_count)+ ['','']   
                helper_functions = ([0] * cell_count)+ ['','']   
                data_preprocessing = ([0] * cell_count)+ ['','']   
                data_exploration = ([0] * cell_count)+ ['','']   
                modelling = ([0] * cell_count)+ ['','']   
                prediction = ([0] * cell_count)+ ['','']   
                evaluation = ([0] * cell_count)+ ['','']   
                data_visualization = ([0] * cell_count)+ ['','']   
                save_results = ([0] * cell_count)+ ['','']   
                comment_only = ([0] * cell_count)+ ['','']   
                other_label = ([''] * cell_count)+ ['','']   
                other_comments = ([''] * cell_count)+ ['','']  
                #print(len(filenames),len(cell_numbers),len(primary_label),len(other_label))
                file_name = self.labels_path+filename+'.csv'
                #print(file_name)
                df_temp = pd.DataFrame({'filename':filenames,'cell_number':cell_numbers,'cell_type':cell_type,
                                        'starting_text':starting_text,'primary_label':primary_label,
                                        'load_data':load_data,'helper_functions':helper_functions,
                                        'data_preprocessing':data_preprocessing,'data_exploration':data_exploration,
                                        'modelling':modelling,'prediction':prediction,'evaluation':evaluation,
                                        'data_visualization':data_visualization,'save_results':save_results,
                                        'comment_only':comment_only,
                                        'other_label':other_label,
                                        'notes':other_comments})
                df_temp.to_csv(file_name, encoding='utf-8', index=False)
            except:
                print("error in generating label file for ",file)
                #print(df)
        print("Done")

