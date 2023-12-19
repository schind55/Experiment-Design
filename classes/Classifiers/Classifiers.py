
# coding: utf-8

'''
This class implements necessary helper methods for performing classification. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

# TF-IDF Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split  
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import MinMaxScaler

import pandas as pd
import numpy as np

import sys,os
packages_path = os.getcwd()
sys.path.append(packages_path.split('classes'+os.path.sep)[0])
from classes.Preprocessing.Preprocessing import Preprocessing
from classes.Classifiers.FeatureSelector import FeatureSelector

class Classifiers:
    def __init__(self,df,labels):
        self.df = df.copy()
        self.df_restricted = None
        self.labels = labels
        self.text_list = None
        self.indices = None
        self.train_X,self.test_X = None,None
        self.X_train_all,self.X_test_all = None,None
        self.y = None
        self.train,self.test = None,None
        self.indices_train,self.indices_test = None,None
    
    def get_restricted_dataframe(self,df,c):
        restricted_df = df[c].copy()
        print("Shape of the restricted dataframe: ",restricted_df.shape)
        print("Resetting index.")
        restricted_df.index = range(restricted_df.shape[0])
        restricted_df.index.name = 'index'
        return restricted_df

    def apply_conditions_to_dataframe(self,conditions):
        #conditions = (self_df.cell_type == 'code') & (self_df.kernel_language == 'python') 
        self.df_restricted =self.get_restricted_dataframe(self.df,conditions)
        return self.df_restricted
    
    def preprocessing(self,col):     
        processortrain = Preprocessing(self.train)
        processortrain.set_column(col,'text_processed')        
        self.train = processortrain.process('text_processed','custom_text_preprocessing')  
        processortest = Preprocessing(self.test)
        processortest.set_column(col,'text_processed')        
        self.test = processortest.process('text_processed','custom_text_preprocessing')   
        return self.train,self.test        
        
    def vectorization(self,tfidf):
        #Split the data into features (X) and classes (y)
        #y is factorised to get categorical data
        #test y
        #y = np.random.choice(self.labels,self.df_restricted.shape[0],replace=True)
        #tfidf = TfidfVectorizer(ngram_range=(1,3),use_idf=True,max_df=0.2,min_df=10,stop_words='english')
        self.X_train_all= tfidf.fit_transform(self.train.text_processed) 
        self.X_test_all = tfidf.transform(self.test.text_processed)
        print("tfidf transformation finished. shape of the feature vector: ",self.X_train_all.shape,self.X_test_all.shape)
        return self.X_train_all,self.X_test_all,tfidf
        
    def feature_selection(self,metric,k,y):
        #k is the number of features to be retained, y is the training label
        if self.X_train_all.shape[1] < k:
            k = self.X_train_all.shape[1]
        # Select features with highest chi-squared statistics
        print("Selecting %d features..." %k)
        selector = SelectKBest(metric, k=k)
        self.train_X = selector.fit_transform(self.X_train_all, y)
        self.test_X = selector.transform(self.X_test_all)
        print("train,test shape")
        print(self.train_X.shape,self.test_X.shape)
        return self.train_X,self.test_X,selector
        
    def test_train_data_selection(self,t_size):        
        # ### Split the data into test and train set
        #self.train,self.test,self.indices_train,self.indices_test = train_test_split(self.df_restricted,self.df_restricted.index.values,test_size = t_size,random_state=0,shuffle=False) 
        
        idx = int(self.df_restricted.shape[0]*(1-t_size))
        self.train = self.df_restricted[0:idx]
        self.indices_train = self.df_restricted[0:idx].index
        self.test = self.df_restricted[idx:]
        self.indices_test = self.df_restricted[idx:].index
        
        print('train.shape,test.shape')
        print(self.train.shape,self.test.shape)
        return (self.train,self.test,self.indices_train,self.indices_test)
    
    def test_train_data_set(self,test_df):
        self.train = self.df_restricted
        self.test = test_df
        self.indices_train = self.df_restricted.index
        #self.test.index = range(self.df_restricted.shape[0],self.df_restricted.shape[0]+test_df.shape[0])
        self.indices_test = test_df.index
        #self.df_restricted = self.df_restricted.append(test_df)
        print('train.shape,test.shape')
        print(self.train.shape,self.test.shape)
        return (self.train,self.test,self.indices_train,self.indices_test)
        
    def set_lexical_features(self,features):
        selector = FeatureSelector(self.train)
        self.train = selector.lexical(features)

        selector = FeatureSelector(self.test)
        self.test = selector.lexical(features)
        print("new (lexical) feature column created as 'new_text'")
        return self.train,self.test
    
    def set_statistical_features(self,stat_features,X_train_features,X_test_features):
        selector = FeatureSelector(self.train)
        train_features = selector.statistical(stat_features,X_train_features)
        
        selector = FeatureSelector(self.test)
        test_features = selector.statistical(stat_features,X_test_features)
        
        #ss = MinMaxScaler()
        #X_train_features_ = ss.fit_transform(X_train_features_)
        #X_test_features_ = ss.transform(X_test_features_)
        
        print("statistical features added")
        return train_features,test_features
