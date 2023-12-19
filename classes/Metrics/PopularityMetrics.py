
# coding: utf-8

'''
This class implements necessary methods for extracting metrics from notebooks. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

#import statements
import json
import numpy as np
import pandas as pd
import base64

import os #For os related operations
from os import listdir
from os.path import isfile, join
from glob import glob 
from collections import namedtuple

import re
import requests
from bs4 import BeautifulSoup as bs

class PopularityMetrics:
    # init function, set set df_repo, df_owner info, path (where notebook is) and files (list of notebooks) for which features are to be extracted. only for github.
    def __init__(self,df_repo,df_owner,path,files):
        self.df_repo = df_repo.copy()
        self.df_owner = df_owner.copy()
        self.path = path
        self.files = files
        self.df = pd.DataFrame()
        
    def get_help(self):
        help_text = """This class implements necessary methods for extracting popularity features like fork, star, watcher count for notebooks. 
        Class is initialized with params: df_repo, df_owner, path_to_folder_containing_notebooks, list_of_notebooks. 
        get_popularity_metrics() is the main method for extracting features. 
        A dataframe containing popularity features (all notebooks) is returned. 
        This class is only valid for GitHub notebooks.
        Each row in the dataframe indicates a notebook. Happy machine learning!"""
        return help_text
    
    def get_files(self): 
        if len(self.files) < 1:
            pfiles = glob(self.path+'\*.ipynb')
            #get file names
            for pfile in pfiles:
                self.files.append(pfile.split(os.path.sep)[-1])
        if len(self.files) < 1:
            print("No .ipynb files found")
        self.files = [file.replace('.ipynb','').replace('nb_','') for file in self.files]
            
    def findWholeWord(self,w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
        
    def get_popularity_measures(self,soup):
        fork_count, star_count, watch_count = 0,0,0
        for link in soup.find_all('li'):
            text = link.text.strip()
            try:
                if self.findWholeWord('Fork')(text):
                    fork_count = int(text.replace('Fork','').strip().replace(',',''))        
                    #print('Fork %d' %count)
                if self.findWholeWord('Star')(text):     # -> <match object>
                    star_count = int(text.replace('Star','').strip().replace(',',''))
                    #print('Start %d' %count)
                if self.findWholeWord('Watch')(text):
                    #for bigger numbers replace , with nothing so that it is easier to convert to int
                    watch_count = int(text.replace('Watch','').strip().replace(',',''))
                    #print('Watch %d' %count)
            except:
                pass
        return (int(fork_count), int(star_count), int(watch_count))
    
    def get_url_info(self):
        url = {}
        for index, row in self.df_owner.iterrows():
            url[row['repo_id']] = row['html_url']
        return url

    def get_popularity_metrics(self):   
        url_dict = self.get_url_info()
        files = []
        repos = []
        forks = []
        stars = []
        watchers = []
        
        self.get_files()
        for each in self.files:
            filename = 'nb_'+str(each)
            repo = None
            fork_count, star_count, watch_count = 0,0,0
            try:
                repo = self.df_repo[self.df_repo.nb_id==int(each)]['repo_id'].values[0]
                #key is the repo
                #values are the notebooks belonging to the repo
                try:
                    url = url_dict[repo]
                    #print(url)
                    r = requests.get(url)
                    soup = bs(r.text,"html5lib")
                    (fork_count, star_count, watch_count) = self.get_popularity_measures(soup)
                except:
                    pass
                #print(fork_count,star_count,watch_count)
            except:
                print(each," not found!")
                pass
            popularity = namedtuple('popularity',('file fork_count star_count watcher_count'))
            pop = popularity(filename,fork_count,star_count,watch_count)
            self.df = self.df.append(pd.DataFrame(data=[pop]))
        self.df.index = range(self.df.shape[0])
        return self.df

