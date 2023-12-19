
# coding: utf-8
'''
This class implements necessary methods for training the classifiers and prediction the labels on test set. Prediction labels and evaluation results are returned. Most of the methods are self-explanatory. Comments are available wherever encessary.
'''

# TF-IDF Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split  
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, roc_curve  
from sklearn.metrics import accuracy_score,f1_score

# LinearSVC Classifier
from sklearn.svm import LinearSVC,SVC #multiclass

import sys,os
import pandas as pd
import numpy as np
packages_path = os.getcwd()
sys.path.append(packages_path.split('classes'+os.path.sep)[0])
from classes.Utils.GetClassifierReport import GetClassifierReport

class LSVC:
    def __init__(self,X_train,y_train,X_test,y_test,indices_train,indices_test,test,labels,results_path,plotname,content,fold):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.indices_train = indices_train
        self.indices_test = indices_test
        self.test = test.copy()
        self.labels = labels
        self.results_path = results_path
        self.plotname = plotname
        self.content = content
        self.fold = fold

    def run(self):
        # linearsvc
        lsvc = LinearSVC(random_state=500)
        #C = np.logspace(0, 4, 10)
        penalty = ['l2']
        C = np.array([0.1,1,10])
        tol = [1e-5,1e-3]
        multi_class = ['ovr']
        hyperparameters = dict(C=C,tol=tol,multi_class=multi_class,penalty=penalty)

        # Create grid search using 5-fold cross validation
        clf = GridSearchCV(lsvc, hyperparameters, cv=self.fold, verbose=0)

        best_model = clf.fit(self.X_train, self.y_train)

        # View best hyperparameters
        penalty = 'Best Penalty: ' + str(best_model.best_estimator_.get_params()['penalty'])
        c_value = 'Best C: ' + str(best_model.best_estimator_.get_params()['C'])
        tol_value = 'Best tolerance: ' + str(best_model.best_estimator_.get_params()['tol'])
        multi_class_value = 'Best multi_class strategy: ' + str(best_model.best_estimator_.get_params()['multi_class'])

        y_predict = best_model.predict(self.X_test)
        true_class = list(self.y_test)
        predicted_class = list(y_predict)

        acc = accuracy_score(self.y_test, y_predict)
        accuracy = 'Accuracy: ' + str(acc)    
        #F1 score being 1 is best
        f1 = f1_score(self.y_test, y_predict,average=None)  #micro
        f1score = "F1 score: " + str(f1)
        report = metrics.classification_report(self.y_test, y_predict, target_names=self.labels)
        matrix = confusion_matrix(self.y_test,y_predict)
        confusion_matrix_result = "Confusion matrix"+"\n"+ str(matrix)

        print(accuracy)
        print(f1score)
        print(report)
        print(confusion_matrix_result)
        obj = pd.Series({'model':'linearsvc','content':self.content,'accuracy':accuracy,'f1-score':f1score})

        #Set test values
        features_text_processed = self.test['text_processed'].values
        features_text = self.test['text'].values          

        result_df = pd.DataFrame({'text':features_text,'text_processed':features_text_processed,
                                  'predicted_class':predicted_class,'true_class':true_class})

        GetClassifierReport(self.results_path, self.plotname, accuracy, f1score, report, matrix, confusion_matrix_result, result_df, self.labels).get_reports()
        return obj,best_model,clf

