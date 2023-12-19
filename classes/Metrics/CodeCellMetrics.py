
# coding: utf-8

'''
This class implements necessary methods for extracting metrics for code cells features from notebooks. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

# import statements
import math,os
import json
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
from glob import glob 
from collections import namedtuple
import string
import re


class CodeCellMetrics:
    # init function, set path (where notebook is) and files (list of notebooks) for which features are to be extracted 
    def __init__(self,path,files):
        self.path = path
        self.files = files
        self.df = pd.DataFrame()
    
    def get_help(self):
        help_text = """This class implements necessary methods for extracting metrics from notebooks aggregated over code cells. 
        Class is initialized with params: path_to_folder_containing_notebooks, list_of_notebooks. 
        get_code_cell_metrics() is the main method for extracting metrics based features. 
        A dataframe containing metrics based features (all notebooks) is returned. 
        Each row in the dataframe indicates a notebook. 
        Happy machine learning!"""
        return help_text
    
    def get_files(self): 
        if len(self.files) < 1:
            pfiles = glob(self.path+'\*.ipynb')
            #get file names
            for pfile in pfiles:
                self.files.append(pfile.split(os.path.sep)[-1])
        if len(self.files) < 1:
            print("No .ipynb files found")
            
    def read_file(self,text):
        data =''
        try:
            data = json.loads(text)
            #print json dict keys if necessary to the type of contents in json formatted jupyter notebook
        except:
            print("Bad json!")
            data = None
        return data

    def variable_counter(self,data):
        variable_count = 0
        #if only alphanumerics before '=' then throw the left side
        pattern = re.compile('[\w+.*\s*]=') #allows underscore,alphanumerics
        for d in data:
            found = pattern.findall(d)
            #print(d, pattern,d.split('=',1)[0])
            if found:
                variable_count = variable_count + 1
        return variable_count
    
    def function_counter(self,data):
        function_count = 0
        for d in data:
            fwords = [w.strip() for w in d.split(' ')]
            if 'def' in fwords:
                function_count = function_count + 1
        return function_count

    def code_processing(self,data):
        #print("***************")
        variable_count = self.variable_counter(data)
        function_count = self.function_counter(data)
        #words_without_variables = variable_remover(data) 
        #words_without_params = remove_params(data)
        return variable_count,function_count
            
    def get_metrics(self,data): 
        cell_metrics = []
        if isinstance(data, dict): 
            keys = data.keys()
        else:
            keys = []
        code_cells_count = 0
        variable_c,function_c,linesofcomment_c,linesofcode_c = 0,0,0,0
        if 'cells' in keys:
            values = data['cells']
            for each in values:
                if each['cell_type'] == 'code':
                    code_cells_count +=1
                    variable_count,function_count,linesofcomment_count,linesofcode_count = 0,0,0,0
                    code, comment = [], []
                    try:
                        if each['source']:  ## check for empty cells
                            for line in each['source']:
                                # ignore line spaces
                                if line != '\n':
                                    result = line.strip()
                                    if len(result) > 0:
                                        if result[0] == '#':
                                            comment.append(result)
                                        else:
                                            code.append(result)
                            if len(code) >=1:
                                variable_count,function_count = self.code_processing(code)
                            linesofcomment_count = len(comment)
                            linesofcode_count = len(code)
                            cell_metrics.append((variable_count,function_count,linesofcomment_count,linesofcode_count))
                    except:
                        cell_metrics.append((variable_count,function_count,linesofcomment_count,linesofcode_count))
                        pass
        try:
            variable_c = sum([elem[0] for elem in cell_metrics])
            function_c = sum([elem[1] for elem in cell_metrics])
            linesofcomment_c = sum([elem[2] for elem in cell_metrics])
            linesofcode_c = sum([elem[3] for elem in cell_metrics])
        except:
            pass
        return (code_cells_count,variable_c,function_c,linesofcomment_c,linesofcode_c)

    
    def get_code_cell_metrics(self):
        self.get_files()
        #get file content
        for file in self.files:
            with open(os.path.join(self.path,file),'r',encoding='utf-8') as f:
                data = self.read_file(f.read())
            try:
                if data:
                    (code_cell_c,variable,func,comment,loc) = self.get_metrics(data)
                    code_cell_metrics = namedtuple('code_cell_metrics','file tot_loc_per_nb tot_locomment_per_nb tot_function_count_per_nb tot_variable_count_per_nb')
                    ccm = code_cell_metrics(file,loc,comment,func,variable)
                    #print(ccm)
                    self.df = self.df.append(pd.DataFrame(data=[ccm]))
            except:
                pass
                print("unable to extract data from the file ",file)
        self.df.index = range(self.df.shape[0])
        return self.df

