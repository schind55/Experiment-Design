
# coding: utf-8

'''
This class implements necessary methods for extracting metrics from notebooks. Most of the methods are self-explanatory. Comments are available wherever necessary.
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
               
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, casual_tokenize


class NotebookMetrics:
    # init function, set dataframe containing features from CellFeatures class 
    def __init__(self,df):
        self.df = df.copy()
        self.df_metrics = pd.DataFrame()
        self.group = None
        self.f = {}
            
    def get_help(self):
        help_text = """This class implements necessary methods for extracting metrics from notebooks. 
        Class is initialized with params: dataframe_result_from_cellfeatures_class. 
        get_notebook_metrics() is the main method for building metrics based features. 
        A dataframe containing metrics based features (all notebooks) is returned. 
        Each row in the dataframe indicates a notebook. 
        Happy machine learning!"""
        return help_text
        
    def combine_lists_to_text(self,obj):
        text = ''
        if obj:
            try:
                if isinstance(obj,list):
                    for element in obj:
                        if isinstance(element,list):
                            for e in element:
                                text = text + ' ' + str(e)
                        else:
                            text = text + ' ' + str(element)
                elif isinstance(obj,str):
                    text = text + ' ' + obj
            except:
                print("excpecting string or list, found %s" %type(obj))
                
            text = text.strip().lower()
        return text

    def get_metrics(self):      
        for k,v in self.group.groups.items():
            file = k[0]
            cell_type = k[1]
            count = 0
            for val in v.values:
                words = word_tokenize(self.df.iloc[val]['text_combined'])
                count += len(words)
            if file in self.f.keys():
                self.f[file][cell_type] = (len(v.values),count)
            else:
                self.f[file] = {}
                self.f[file][cell_type] = (len(v.values),count)
            
    
    def get_notebook_metrics(self):
        self.group = self.df.groupby(['filename','cell_type'])
        self.df['text_combined'] = self.df['text'].apply(self.combine_lists_to_text)        
        self.get_metrics()
        for k,v in self.f.items():
            code_cell_count,code_tokens,markdown_cell_count,markdown_tokens = 0,0,0,0
            try:
                code_cell_count = v['code'][0]
                code_tokens = v['code'][1]
            except:
                code_cell_count = 0
                code_tokens = 0        
            try:
                try:
                    markdown_cell_count = v['markdown'][0] 
                    markdown_tokens = v['markdown'][1]
                except:
                    markdown_cell_count = v['markdown'][0]
                    markdown_tokens = v['markdown'][1]
            except:
                markdown_cell_count = 0
                markdown_tokens = 0
                
            metrics = namedtuple('metrics','file no_of_code_cells_per_nb code_tokens_per_nb no_of_markdown_cells_per_nb markdown_tokens_per_nb')
            m = metrics(k,code_cell_count,code_tokens,markdown_cell_count,markdown_tokens)
            #print(m)
            self.df_metrics = self.df_metrics.append(pd.DataFrame(data=[m]))
        
        self.df_metrics.index = range(self.df_metrics.shape[0])
        return self.df_metrics

