
# coding: utf-8

'''
This class implements necessary methods to prepare a evaluation report of a classifier. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''
# import statements
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

class GetClassifierReport:
    def __init__(self,results_path,plotname,accuracy,f1score,report,matrix, confusion_matrix_result,result_df,labels):
        self.results_path = results_path
        self.plotname = plotname
        self.accuracy = accuracy
        self.f1score = f1score
        self.report = report
        self.matrix = matrix
        self.confusion_matrix_result = confusion_matrix_result
        self.result_df = result_df
        self.labels = labels
        
    def get_reports(self):
        self.result_df.to_pickle(self.results_path+self.plotname+'.pkl')
        with open(self.results_path+self.plotname+'.txt', "w") as text_file:
            #print(penalty, file=text_file)
            #print(c_value, file=text_file)
            print('\n*******Report on Test set*******\n',file=text_file)
            print(self.accuracy, file=text_file)
            print(self.f1score, file=text_file)
            print(self.report, file=text_file)
            print(self.confusion_matrix_result, file=text_file)

        fig, ax = plt.subplots(figsize=(10,10))
        sns.heatmap(self.matrix, annot=True, fmt='d')
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        ax.set_title('Confusion matrix - '+self.plotname,fontsize=15,fontweight='bold')
        ax.set_yticklabels(self.labels,rotation=0)
        ax.set_xticklabels(self.labels,rotation=60)
        fig.tight_layout()
        ax.figure.savefig(self.results_path+'Confusion matrix - '+self.plotname+'.png')
        print("results saved in ",self.results_path)
        plt.show()

