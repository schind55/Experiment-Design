
# coding: utf-8

'''
This class implements necessary helper methods for selecting features from a dataframe. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

import pandas as pd
import numpy as np

class FeatureSelector:
    def __init__(self,df):
        self.df = df
    
    def lexical(self,features):
        new_text = []
        for idx,row in self.df.iterrows():
            l = []
            for each in features:
                if isinstance(row[each], list):
                    l = l + row[each]
                else:
                    l = l + [row[each]]
            new_text.append(l)
        self.df['new_text'] = new_text
        return self.df
    
    def statistical(self,features,X):
        X_copy = X.toarray().copy()
        
        for each in features:
            X_copy = np.c_[ X_copy, self.df[each].values] 
            print("taking feature ",each, " ",X_copy.shape)
        
        return X_copy

