
# coding: utf-8

'''
This class implements necessary methods for generating annotation template files for main annotation. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

import pandas as pd
import numpy as np

import sys,os
packages_path = os.getcwd()
sys.path.append(packages_path.split('classes'+os.path.sep)[0])
from classes.Utils.PandasUtils import PandasUtils

class GenerateLabelFiles:
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
            df = PandasUtils.get_pickle_files_in_dataframe(self.pickle_path,[file])
            try:
                cell_count = df.shape[0]
                cell_type = df.cell_type.values
                starting_text = df.text.apply(self.retreive_first_element)
                filename = file.split('.pkl')[0]
                filenames = [filename]*cell_count
                cell_numbers = range(0,cell_count)
                cell_numbers = [int(i) for i in cell_numbers]
                #labels = ['']*cell_count #choose this over followring way of label generation
                labels_ = ['data_preparation','data_exploration','modelling','evaluation','data_visualization','result_reporting']
                y = np.random.choice(labels_,cell_count,replace=True)
                labels = [[] for each in y]
                #print(len(filenames),len(cell_numbers),len(labels))
                df_temp = pd.DataFrame({'filename':filenames,'cell_number':cell_numbers,'cell_type':cell_type,
                                        'starting_text':starting_text,'labels':labels})
                file_name = self.labels_path+filename+'.csv'
                df_temp.to_csv(file_name, encoding='utf-8', index=False)
            except:
                print("error in generating label file for ",file)
                print(df)
        print("Done")

