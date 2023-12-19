
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

#Multi layer perceptron
from sklearn import svm

import sys,os
import pandas as pd
import numpy as np
packages_path = os.getcwd()
sys.path.append(packages_path.split('classes'+os.path.sep)[0])
from classes.Utils.GetClassifierReport import GetClassifierReport

class SVC:
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
        # SVC
        svc = svm.SVC(probability=True)

        #C = np.logspace(0, 4, 10)
        C = np.array([0.1,1,10])
        tol = [1e-5,1e-3]
        hyperparameters = dict(C=C,tol=tol)

        # Create grid search using 5-fold cross validation
        clf = GridSearchCV(svc, hyperparameters, cv=self.fold, verbose=0)

        best_model = clf.fit(self.X_train, self.y_train)

        # View best hyperparameters
        penalty_value = 'Best penalty: ' + str(best_model.best_estimator_.get_params()['C'])
        tolerance_value = 'Best tolerance: ' + str(best_model.best_estimator_.get_params()['tol'])

        y_predict = best_model.predict(self.X_test)
        prob = clf.predict_proba(self.X_test)
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
        obj = pd.Series({'model':'svc','content':self.content,'accuracy':accuracy,'f1-score':f1score})

        #Set test values
        features_text_processed = self.test['text_processed'].values
        features_text = self.test['text'].values

        proba_0 = []
        proba_1 = []
        proba_2 = []
        proba_3 = []
        proba_4 = []
        proba_5 = []
        proba_6,proba_7,proba_8 = [],[],[]
        for i in range(prob.shape[0]):
            proba_0.append(prob[i][0])
            proba_1.append(prob[i][1])
            proba_2.append(prob[i][2])
            proba_3.append(prob[i][3])
            proba_4.append(prob[i][4])
            proba_5.append(prob[i][5])
            proba_6.append(prob[i][6])
            proba_7.append(prob[i][7])
            proba_8.append(prob[i][8])


        result_df = pd.DataFrame({'text':features_text,'text_processed':features_text_processed,
                                  'predicted_class':predicted_class,'true_class':true_class,
                                  'probabilities_0':proba_0,'probabilities_1':proba_1,
                                 'probabilities_2':proba_2,'probabilities_3':proba_3,
                                 'probabilities_4':proba_4,'probabilities_5':proba_5,
                                 'probabilities_6':proba_6,'probabilities_7':proba_7,
                                 'probabilities_8':proba_8})

        GetClassifierReport(self.results_path, self.plotname, accuracy, f1score, report, matrix, confusion_matrix_result, result_df, self.labels).get_reports()
        return obj,best_model,clf