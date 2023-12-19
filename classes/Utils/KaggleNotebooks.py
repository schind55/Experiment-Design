
# coding: utf-8

'''
This class implements necessary methods to prepare a evaluation report of a classifier. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

import kaggle
import os
import pandas as pd
from collections import namedtuple

class KaggleNotebooks:
    def __init__(self,n_path,search_keyword):
        self.base_url = 'https://www.kaggle.com/' 
        self.path = n_path
        self.search_keyword = search_keyword
        self.notebook_results = None
        self.df = pd.DataFrame()
    
    def get_kaggle_notebooks(self):
        self.notebook_results = get_ipython().getoutput('kaggle kernels list -s $self.search_keyword')
        print("%d results retreived for the keyword" %len(self.notebook_results))
        kaggle_row = namedtuple('kaggle_row',('ref title author lastRunTime totalVotes'))
        
        for idx in range(1,len(self.notebook_results)):
            try:
                k = [each for each in self.notebook_results[idx].split('    ') if each!='']
                kernel = k[0]
                get_ipython().system('kaggle kernels pull $kernel -p $self.path')
                row = kaggle_row(k[0],k[1],k[2],k[3],k[4])
                self.df = self.df.append(pd.DataFrame(data=[row]))
                #print(kernel)
            except:
                pass
        
        self.df.index = range(self.df.shape[0])
        return self.df

