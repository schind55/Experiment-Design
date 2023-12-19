
# coding: utf-8

'''
This class implements necessary methods for preprocessing. Most of the methods are self-explanatory. Comments are available wherever necessary.
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

import nltk
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize, casual_tokenize
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))
from nltk.stem import SnowballStemmer as snows
stemmer = snows("english")
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk import pos_tag
from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()
lem = WordNetLemmatizer()
import string
from string import punctuation
import itertools

class Preprocessing:
    # init. set dataframe to be processed
    def __init__(self,df):
        self.df = df
    
    def get_help(self):
        help_text = """This class implements necessary methods for extracting preprocess various type of content.
        Class is initialized with params: cellFeatures_dataframe. 
        set_column(col, newcol) method sets col:column containing feature, newcol: name of new column to be generated. 
        process(newcol, function) method applies the preprocessing function to newcol.
        Available preprocessing function are code: 'custom_text_preprocessing' for code, 'import\_text\_preprocessing' for import statements, 'text\_preprocessing' for natural language like markdown, comments, raw text. 
        A modified dataframe containing preprocessed features in the newcol is returned. 
        Each row in the dataframe indicates a cell. Happy machine learning!"""
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
    
    # preprocessing function for import statements
    def import_text_preprocessing(self,s):
        favourite_punc = ['.','_','#']
        if s:
            for char in punctuation:
                if char not in favourite_punc:
                    s = s.replace(char, ' ')
            s = " ".join([word.split('.')[0]  if '.' in word else word for word in s.split(' ')])
            s = " ".join(['scikit-learn' if word == 'sklearn' else word for word in s.split(' ')])
            s = " ".join(['scikit-learn' if word == 'scipy' else word for word in s.split(' ')])
            s = " ".join(self.remove_stopwords(s.lower().split(' '))) #dont remove stopwords as we want to retain the relationship of as and from
            s = " ".join([word.strip() for word in s.split(' ') if len(word)>1]) #modify as needed
        return s  
    
    # preprocessing function for natural language content like markdown, comments, raw text
    def text_preprocessing(self,s):
        favourite_punc = ['.','_','#']
        if s:
            for char in punctuation:
                if char not in favourite_punc:
                    s = s.replace(char, ' ')
            #new line chars
            s = " ".join([word.replace('\n\n',' ') if '\n\n' in word else word for word in s.split(' ')])
            s = " ".join([word.replace('\n',' ') if '\n' in word else word for word in s.split(' ')])
            s = " ".join(['' if word.replace('.','').isdigit() else word for word in s.split(' ')])
            #s = " ".join(['$' if '$' in word and word.replace('$','').isnumeric() else word for word in s.split(' ')])
            s = " ".join(self.remove_stopwords(s.lower().split(' ')))
            s = " ".join([word.strip() for word in s.split(' ') if len(word)>1])
            #s = " ".join([word for word in s if word not in throw_words])
        return s
    
    def remove_stopwords(self,words):
        wordsFiltered = [w for w in words if w not in stopWords]
        return wordsFiltered

    # preprocessing function for code
    def custom_text_preprocessing(self,s):
        favourite_punc = ['.','#','_']
        if s:
            for char in punctuation:
                if char not in favourite_punc:
                    s = s.replace(char, ' ')
            s = " ".join(['' if word.replace('.','').isdigit() else word for word in s.split(' ')])
            #s = " ".join(['$' if '$' in word and word.replace('$','').isnumeric() else word for word in s.split(' ')])
            s = " ".join(self.remove_stopwords(s.lower().split(' ')))
            s = " ".join([word.strip() for word in s.split(' ') if len(word)>1])
            #s = " ".join([word for word in s if word not in throw_words])
        return s

    def set_column(self,col,newcol):
        self.df[newcol] = self.df[col].apply(self.combine_lists_to_text)
        return self.df
    
    def process(self,newcol,function):
        if function == 'import_text_preprocessing':
            self.df[newcol] = self.df[newcol].apply(self.import_text_preprocessing)
        if function == 'text_preprocessing':
            self.df[newcol] = self.df[newcol].apply(self.text_preprocessing)
        if function == 'custom_text_preprocessing':
            self.df[newcol] = self.df[newcol].apply(self.custom_text_preprocessing)
        return self.df
            
        
        

