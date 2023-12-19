
# coding: utf-8

'''
This class implements necessary methods for extracting repo, owner features from notebooks. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''


#import statements
import pandas as pd
import base64
import os 
from glob import glob 
from collections import namedtuple

class StyleFeatures:
    # init function, set df_repo, df_readme, df_owner info, path and files (list of notebooks) for which features are to be extracted 
    def __init__(self,df_repo,df_readme,df_owner,path,files):
        self.df_repo = df_repo.copy()
        self.df_readme = df_readme.copy()
        self.df_owner = df_owner.copy()
        self.path = path
        self.files = files
        self.df = pd.DataFrame()
        
    def get_help(self):
        help_text = """ This class implements necessary methods for extracting repo and owner features for notebooks. 
        Class is initialized with params: df_repo, df_readme, df_owner, path_to_folder_containing_notebooks, list_of_notebooks. 
        get_style_features() is the main method for extracting features. 
        A dataframe containing style features (all notebooks) is returned. 
        Each row in the dataframe indicates a notebook. Happy machine learning! """
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
        
    def get_readme_info(self):
        readme = {}
        for index, row in self.df_readme.iterrows():
            content_readme = []
            try:
                #row['content'] gives the read me for row['repo_id']
                if row['content']:
                    content = base64.b64decode(row['content'])
                    content_readme = content.decode("utf-8").split('\n\n')
                else:
                    content_readme = []
            except:
                content_readme = []
            readme[row['repo_id']] = content_readme
        return readme
        
    def get_owner_info(self):
        owner = {}
        for index, row in self.df_owner.iterrows():
            owner[row['repo_id']] = row['owner_id']
        return owner
    
    def get_style_features(self):   
        readme_dict = self.get_readme_info()
        owner_dict = self.get_owner_info()
        self.get_files()
        
        for each in self.files:
            filename = 'nb_'+str(each)
            repo,owner,readme = None,None,None
            try:
                repo = self.df_repo[self.df_repo.nb_id==int(each)]['repo_id'].values[0]
                #key is the repo
                #values are the notebooks belonging to the repo
                try:
                    owner = str(owner_dict[repo])
                except:
                    #print('owner for '+key+' not available')
                    pass
                try:
                    readme = readme_dict[repo]
                except:
                    #print('readme for '+key+' not available')
                    pass
            except:
                print(each," not found!")
                pass
            style = namedtuple('style',('file repo_id owner readme'))
            s = style(filename,repo,owner,readme)
            self.df = self.df.append(pd.DataFrame(data=[s]))
        self.df.index = range(self.df.shape[0])
        return self.df

