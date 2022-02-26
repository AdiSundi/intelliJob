#!/usr/bin/env python3

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

'''Write to txt files'''
def write_to_txt():
    for class_dis in list(dict_keywords.keys()):
        with open(str(class_dis)+'.txt', 'w') as f: 
            f.write(' '.join(dict_op_words[class_dis]))

# Use model to predict

model = fasttext.train_unsupervised('trainingList.txt', minCount=1)

if __name__=="__main__":
    get_op_words()
    write_to_txt()

#model = fasttext.train_unsupervised('trainingList.txt', minCount=1)