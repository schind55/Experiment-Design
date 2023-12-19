
# coding: utf-8

'''
This class implements method for generating WordCloud image using WordCloud library. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

#visualization
from wordcloud import WordCloud
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import os
sns.set(style="darkgrid")

class WordCloudView:
    def __init__(self,c,plotname,path):
        self.c = c
        self.plotname = plotname+'.png'
        self.path = path
        
    def plot(self):
        # generate a cloud image prioritizing frequency over rank with weight 0.8
        wordcloud = WordCloud(width=800, height=600, relative_scaling=.8,background_color="white").generate_from_frequencies(self.c)
        fig = plt.figure(figsize=(12,12),frameon=False)
        # Display the image inline
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.savefig(os.path.join(self.path,self.plotname),bbox_inches='tight')
        print("results saved in ",os.path.join(self.path,self.plotname))
        plt.show()
    

