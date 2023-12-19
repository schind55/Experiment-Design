
# coding: utf-8

'''
This class implements necessary methods for extracting description/man_page information of all the libraries imported in the given data. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

#Import statements
import json
import numpy as np
import os #For os related operations
from os import listdir
from os.path import isfile, join
import pandas as pd

import math
from collections import Counter
from itertools import islice

import string
from string import punctuation
import itertools

class PypiPackagesInformationFeatures:
    # init function, set dataframe for which features man-pages are to be extracted 
    # pypi is the dataframe containing all information of libraries and its man-page information.  
    def __init__(self,df,pypi):
        self.df = df
        self.pypi = pypi.copy()
        
    def get_help(self):
        help_text = """This class implements necessary methods for extracting man-pages information for libraries appearing in each cell of a notebook. 
        Class is initialized with params: dataframe_of_notebook_cells, man_page_libraries_dataframe.
        get_pypi_packages_information_features() is the main method for extracting features and takes as parameters column_to_be_processed which contains the libraries information column_to_store_results. 
        A .pkl for each notebook separetly is stored in store_path specified. Returns the modified dataframe. 
        Happy machine learning!"""
        return help_text
    
    # process the man_page info if necessary
    def pypi_text_preprocessing(self,obj):        
        text = []
        if obj:
            for o in obj:
                #new line chars
                o = " ".join([word.replace('\n\n',' ') if '\n\n' in word else word for word in o.split(' ')])
                o = " ".join([word.replace('\n',' ') if '\n' in word else word for word in o.split(' ')])
                text.append(o)
        return text
    
    # find the package description if exists for each library
    def add_packages_description(self,obj):
        text = []
        if obj:
            for package in obj.split(' '):
                try:
                    desc = self.pypi[self.pypi.package_name == package]['package_description'].values[0]
                except:
                    desc = package
                    #print(package , ' is not there')
                    #print(self.pypi[self.pypi.package_name == package]['package_description'])
                if desc:
                    text.append(desc)
                else:
                    pass
        return text
            
    def get_pypi_packages_information_features(self,col,newcol):
        self.df[newcol] = self.df[col].apply(self.add_packages_description)
        self.df[newcol] = self.df[newcol].apply(self.pypi_text_preprocessing)
        return self.df
    

