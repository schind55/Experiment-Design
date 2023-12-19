
# coding: utf-8

'''
This class implements necessary helper methods for upsampling or downsampling from training data. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''


import pandas as pd

class ClassBalancer():
    def __init__(self,df,labels):
        self.df = df.copy()
        self.temp_df = pd.DataFrame()
        self.labels = labels
        self.down_sample_count = min(self.df['single_label'].value_counts().values)
        self.up_sample_count = max(self.df['single_label'].value_counts().values)
    
    def downsampling(self):
        print('samples for each label to be: ',self.down_sample_count)
        for label in self.labels:
            label_df = self.df[self.df['single_label']==label].sample(n=self.down_sample_count, replace=False, random_state = 500)
            self.temp_df = self.temp_df.append(label_df)
            #print(label_df.shape)
        self.temp_df.index = range(self.temp_df.shape[0])
        return self.temp_df
    
    def upsampling(self):
        print('samples for each label to be: ',self.up_sample_count)
        for label in self.labels:
            label_df = self.df[self.df['single_label']==label].sample(n=self.up_sample_count, replace=True, random_state = 500)
            self.temp_df = self.temp_df.append(label_df)
            #print(label_df.shape)
        self.temp_df.index = range(self.temp_df.shape[0])
        return self.temp_df
            
        

