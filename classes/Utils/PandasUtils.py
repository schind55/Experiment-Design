
# coding: utf-8

'''
This class implements helper methods to prepare data. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

import pandas as pd

### Get pickles

class PandasUtils:
    def __init__(self):
        print("functions available: get_pickle_files_in_dataframe, get_csv_files_in_dataframe")

    def get_pickle_files_in_dataframe(pickle_path,pickle_files):
        df = pd.DataFrame()
        filecount=1
        for file in pickle_files:
            if filecount%500==0:
                print(filecount, " pickles loaded.")
            try:
                print(pickle_path+file)
                temp_df = pd.read_pickle(pickle_path+file)
                df = df.append(temp_df)
            except:
                pass
            filecount +=1
        #print("Shape of the dataframe (datapoints): ",df.shape)
        #print("View of a sample of the dataframe: ")
        #print(df.head())
        #print(df.columns.values)
        return df

    def get_csv_files_in_dataframe(csv_path,csv_files):
        df = pd.DataFrame()
        filecount=1
        for file in csv_files:
            #print(file)
            if filecount%500==0:
                print(filecount, " csvs' loaded.")
            try:
                temp_df = pd.read_csv(csv_path+file+'.csv')
                df = df.append(temp_df)
            except:
                pass
            filecount +=1
        print("Shape of the dataframe (datapoints): ",df.shape)
        #print("View of a sample of the dataframe: ")
        #print(df.head())
        print(df.columns.values)
        return df

