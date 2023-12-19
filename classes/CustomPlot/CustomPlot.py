
# coding: utf-8

'''
This class implements necessary helper methods for generating a custom plot required for thesis report. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''
# import statements
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#data structures
import collections
from collections import Counter
from itertools import chain
from itertools import islice

class CustomPlot:
    def __init__(self,palette):
        self.palette = palette
        
    def take(self,n,iterable):
        "Return first n items of the iterable as a list"
        return list(islice(iterable, n))

    def get_top_values_from_dict(self,df,col,top_count):    
        count_all = Counter(list(df[col].values))
        count_sorted = collections.OrderedDict(sorted(count_all.items(), key=lambda kv: kv[1], reverse=True))
        count_sorted.pop("", None)
        count_sorted.pop(None,None)
        count_top = collections.OrderedDict(self.take(top_count,count_sorted.items()))
        return count_top

    def plot_seaborn_category(self,df,col,top_count,start,plotname,path,fig,axes):
        sns.set(style="darkgrid")
        total = df[col].value_counts().values.sum()
        count = self.get_top_values_from_dict(df,col,top_count)
        d = df[df[col].isin(list(count.keys())[start:])]
        if start>0:
            print("Largest set: ",collections.OrderedDict(self.take(start,count.items())))
        var = list(count.keys())[0]
        ax = sns.countplot(x=col,data=d,order=d[col].value_counts().index,palette=self.palette)
        if isinstance(var,int):
            #' \n (' +str(count[int(ax.get_xticklabels()[i].get_text())])+')'
            labels = [str(int(float(ax.get_xticklabels()[i].get_text()))) + ' \n (' +str(round(count[int(float(ax.get_xticklabels()[i].get_text()))]/total*100,2))+'%)'  for i in range(len(ax.get_xticklabels()))]
        elif isinstance(var,str): 
            #' \n (' +str(count[ax.get_xticklabels()[i].get_text()])+')'
            labels = [ax.get_xticklabels()[i].get_text() + ' \n (' +str(round(count[ax.get_xticklabels()[i].get_text()]/total*100,2))+'%)'  for i in range(len(ax.get_xticklabels()))]
        else: 
            #' \n (' +str(count[ax.get_xticklabels()[i].get_text()])+')'
            labels = [ax.get_xticklabels()[i].get_text() + ' \n (' +str(round(count[int(ax.get_xticklabels()[i].get_text())]/total*100,2))+'%)'  for i in range(len(ax.get_xticklabels()))]

        ax.set_xticklabels(labels,rotation=60)
        ax.set_title(plotname,fontsize=15,weight='bold')
        ax.set_xlabel(col,fontsize=12)

        def change_width(ax, new_value) :
            for patch in ax.patches :
                current_width = patch.get_width()
                diff = current_width - new_value

                # we change the bar width
                patch.set_width(new_value)

                # we recenter the bar
                patch.set_x(patch.get_x() + diff * .5)

        if len(labels) <=1:
            change_width(ax,.1)
        elif len(labels) <= 5 and len(labels) >1:
            change_width(ax,.5)

        for p in ax.patches:
            ax.annotate('{:}'.format(p.get_height()), (p.get_x()+0.1, p.get_height()+0.1))


        fig.tight_layout()
        if start>0:
            ax.text(.8, .8, str(collections.OrderedDict(self.take(start,count.items()))),
                    horizontalalignment='right',verticalalignment='bottom',
                    transform=ax.transAxes,size='medium', color='black')
        
        ax.figure.savefig(path+plotname+'.png')
        print("results saved in ",path+plotname+'.png')
        return ax


