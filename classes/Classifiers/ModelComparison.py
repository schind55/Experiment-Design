
# coding: utf-8


'''
This class implements methods for performing Singlelabel classification using various classifiers and outputs the resulting accuracy from crossvalidation. It also produces a comparative graph plotting the accuracy. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

from sklearn.svm import LinearSVC,SVC #multiclass
from sklearn.linear_model import LogisticRegression #multiclass
from sklearn.neural_network import MLPClassifier #multilabel
from sklearn import ensemble #multiclass
from sklearn.ensemble import RandomForestClassifier #multilabel, multioutput
from sklearn.tree import DecisionTreeClassifier  #multilabel, multioutput
from sklearn.neighbors import KNeighborsClassifier  #multilabel, multioutput
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB  #multiclass

from sklearn.model_selection import cross_val_score

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

class ModelComparison:
    def __init__(self,X,y,CV):
        self.X_train = X
        self.y_train = y    
        self.CV = CV
        self.results = None
    
    def model_comparison(self):
        models = [
            SVC(kernel='poly',random_state = 500),
            DecisionTreeClassifier(random_state=500),  
            RandomForestClassifier(random_state=500),
            LinearSVC(),
            LogisticRegression(random_state=500),
            ensemble.GradientBoostingClassifier()
        ]
        
        #MLPClassifier(random_state=500),
        #MultinomialNB(),
        #KNeighborsClassifier(),
        
        cv_df = pd.DataFrame(index=range(self.CV * len(models)))

        entries = []
        for model in models:
            #print(model)
            try:
                try:
                    model_name = model.__class__.__name__ + '_' + model.get_params()['kernel']
                except:
                    model_name = model.__class__.__name__
                try:
                    accuracies = cross_val_score(model, self.X_train, self.y_train, scoring='accuracy', cv=self.CV)
                    #print(accuracies)
                    for fold_idx, accuracy in enumerate(accuracies):
                        entries.append((model_name, fold_idx, accuracy))
                        #print(model_name,fold_idx,accuracy)
                except:
                    print("model %s does not work for the data and parameters given!" % model_name)
            except:
                pass

        cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
        self.results = cv_df
        return cv_df

    def plot_model_comparison(self,results_path,title):
        plotname = "Model Accuracy Comparison - "+title+"_"+str(self.CV)
        fig, ax = plt.subplots(figsize=(15, 8))
        #sns.boxplot(x='model_name', y='accuracy', data=self.results)
        sns.stripplot(x='model_name', y='accuracy', data=self.results,size=8, jitter=True, edgecolor="gray", linewidth=2)
        ax.set_title(plotname,fontsize=15)
        ax.set_xlabel("Model",fontsize=15)
        ax.set_ylabel("Accuracy",fontsize=15)
        ax.tick_params(labelsize=12)
        plt.xticks(rotation=45)
        fig.tight_layout()
        ax.figure.savefig(results_path+plotname+'.png')
        print("results saved in ",results_path)
        plt.show()

