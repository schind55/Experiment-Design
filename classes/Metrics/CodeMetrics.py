
# coding: utf-8

'''
This class implements necessary methods for extracting code metrics using RADON library from notebooks. Most of the methods are self-explanatory. Comments are available wherever necessary.
'''

# import statements
import radon
from radon.raw import analyze
from radon import metrics,complexity
from radon.complexity import cc_visit, cc_visit_ast, cc_rank
import math,os
from os import listdir
from os.path import isfile, join
from glob import glob 
from collections import namedtuple
import pandas as pd

class CodeMetrics:    
    # init function, set path (where notebook is) and files (list of .py files) for which features are to be extracted 
    def __init__(self,path,files):
        self.path = path
        self.files = files
        self.programs = {}
        self.df = pd.DataFrame()
    
    def get_help(self):
        help_text = """This class implements necessary methods for extracting code metrics from notebooks. 
        Class is initialized with params: path_to_folder_containing_notebooks, list_of_notebooks. 
        get_code_metrics() is the main method for extracting metrics based features. 
        A dataframe containing all features (all notebooks) is returned. 
        Each row in the dataframe indicates a notebook. 
        Happy machine learning!"""
        return help_text
    
    def get_code_string(self): 
        if len(self.files) < 1:
            pfiles = glob(self.path+'\*.py')
            #get file names
            for pfile in pfiles:
                self.files.append(pfile.split(os.path.sep)[-1])
        if len(self.files) < 1:
            print("No .py files found")
        else:
            #get file content
            for file in self.files:
                #cmd = 'futurize --stage1 -w '+file
                #print(cmd)
                #!cmd
                with open(os.path.join(self.path,file),'r',encoding='utf-8') as f:
                    self.programs[file] = f.read()
        
    def get_code_metrics(self):
        self.get_code_string()
        if len(self.files) < 1:
            return None
        else:
            for file,code in self.programs.items():
                loc,sloc,comments,multi,blank,single_comments,distinct_operators,distinct_operands = 0,0,0,0,0,0,0,0
                total_operators,total_operands,vocabulary,length,calculated_length,difficulty,effort,time,bugs = 0,0,0,0,0,0,0,0,0
                halstead_volume,lloc,percentage_of_lines_of_comment = 0,0,0
                maintainability_index,maintainability_rank,cyclomatic_complexity,cyclomatic_complexity_rank = 0,0,0,0

                try:
                    try:
                        #raw metrics
                        raw_metrics = analyze(code)
                        print("********",file,"********")
                        loc = raw_metrics.loc
                        sloc = raw_metrics.sloc
                        comments = raw_metrics.comments
                        multi = raw_metrics.multi
                        blank = raw_metrics.blank
                        single_comments = raw_metrics.single_comments
                        #print(raw_metrics)
                        #sloc+blanks+multi+singlecomments=loc 
                        #print(raw_metrics.sloc+raw_metrics.blank+raw_metrics.multi+raw_metrics.single_comments,raw_metrics.loc)
                    except Exception as e:
                        pass
                        print(e)
                        print("unable to retrieve raw metrics")

                    try:
                        #halstead metrics
                        halstead_r = metrics.h_visit_ast(radon.metrics.h_visit(code))
                        halstead_report = radon.metrics.h_visit(code)
                        #print(halstead_r)
                        #print(halstead_report)
                        distinct_operators = halstead_report.total.h1
                        distinct_operands = halstead_report.total.h2
                        total_operators = halstead_report.total.N1
                        total_operands = halstead_report.total.N2
                        vocabulary = halstead_report.total.h1 + halstead_report.total.h2
                        length = halstead_report.total.N1 + halstead_report.total.N2
                        calculated_length = halstead_report.total.h1 * math.log2(halstead_report.total.h1) + halstead_report.total.h2 * math.log2(halstead_report.total.h2)
                        volume = length * math.log2(vocabulary)
                        difficulty = halstead_report.total.h1 / 2 * halstead_report.total.N2 / halstead_report.total.h2
                        effort = difficulty * volume
                        time = effort / 18 #seconds
                        bugs = volume / 3000 #an estimate of the errors in the implementation

                        (halstead_volume,cyclomatic_complexity,lloc,percentage_of_lines_of_comment) = radon.metrics.mi_parameters(code, count_multi=False)
                        #print(halstead_volume,cyclomatic_complexity,lloc,percentage_of_lines_of_comment)
                    except Exception as e:
                        pass
                        print(e)
                        print("unable to retrieve halstead info")
                    
                    try:
                        #maintainability index
                        '''
                        A if score>19;
                        B if 9<score≤19;
                        C if score≤9.
                        '''
                        maintainability_index = metrics.mi_visit(code,multi=True)
                        maintainability_rank = metrics.mi_rank(maintainability_index)
                        #print(maintainability_index,maintainability_rank)
                    except Exception as e:
                        pass
                        print(e)
                        print("unable to retrieve maintainability index")

                    try:
                        #cyclomatic complexity
                        '''
                        1 - 5 	A (low risk - simple block)
                        6 - 10 	B (low risk - well structured and stable block)
                        11 - 20 	C (moderate risk - slightly complex block)
                        21 - 30 	D (more than moderate risk - more complex block)
                        31 - 40 	E (high risk - complex block, alarming)
                        41+ 	F (very high risk - error-prone, unstable block)
                        '''
                        #print(radon.complexity.cc_visit(code))
                        cyclomatic_complexity_rank = complexity.cc_rank(cyclomatic_complexity)
                        #print(cyclomatic_complexity,cyclomatic_complexity_rank)
                    except Exception as e:
                        pass
                        print(e)
                        print("unable to retrieve complexity index")

                    code_metrics = namedtuple('code_metrics','file loc sloc comments multi blank_lines single_comments distinct_operators distinct_operands total_operators total_operands program_vocabulary program_length calculated_length difficulty effort time bugs halstead_volume lloc percentage_of_lines_of_comment maintainability_index maintainability_rank cyclomatic_complexity cyclomatic_complexity_rank')
                    cm = code_metrics(file,loc,sloc,comments,multi,blank,single_comments,distinct_operators,distinct_operands,total_operators,total_operands,vocabulary,length,calculated_length,difficulty,effort,time,bugs,halstead_volume,lloc,percentage_of_lines_of_comment,maintainability_index,maintainability_rank,cyclomatic_complexity,cyclomatic_complexity_rank)
                    #print(cm)
                    self.df = self.df.append(pd.DataFrame(data=[cm]))
                    #print(self.df)
                except:
                    pass
                    #print("not supported python version")
            self.df.index = range(self.df.shape[0])
            return self.df

