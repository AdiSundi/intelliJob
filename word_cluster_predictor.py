#!/usr/bin/env python3

'''Program to generate txt files consisting of clean rule bindings by training an NLP model after NLP pipeline cleaning'''

# Import libraries
from matplotlib.pyplot import cla
import nltk
nltk.download('stopwords')
import pandas as pd
import gensim
import re
from nltk.corpus import stopwords
import stanza
import job_smartFilter as filter
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import fasttext
import os

#Import the ruleset file
from ruleset import ruleset_func
  
warnings.filterwarnings(action = 'ignore')

# Global variables
# Compiled list of jobs accessible to classes of disabilities scraped from a website
dict_keywords = ruleset_func()
temp_list=[]
dict_op_words = {}

'''Get output word semantics for each class'''
def get_op_words():
    for class_dis in list(dict_keywords.keys()):
        dict_op_words[class_dis]=[]
        temp_list=[]

        for i in dict_keywords[class_dis]:
            temp_list.append(filter.netCleaner(i,""))

        for i in temp_list:
            temp_str = ''
            for j in i:
                temp_str+=(j+'-')
            dict_op_words[class_dis].append(temp_str[0:-1])

'''Create directory for txt files'''
if not os.path.exists('ruletext'):
    os.makedirs('ruletext')

'''Write to txt files'''
def write_to_txt():
    for class_dis in list(dict_keywords.keys()):
        with open('ruletext/'+str(class_dis)+'.txt', 'w') as f: 
            f.write(' '.join(dict_op_words[class_dis]))

if __name__=="__main__":
    get_op_words()
    write_to_txt()
