#!/usr/bin/env python3
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import stanza
stanza.download('en')
stanza_nlp = stanza.Pipeline('en')

'''Program consisting of the NLP pipeline cleaning for generating clean rule bindings'''

'''Convert from list to String'''
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

'''Use StopWords in the NLP model'''
def cleanPosting(titleString:str,descriptionString:str)->list:
    text = titleString+" "+descriptionString
    sw_nltk = stopwords.words('english')
    delimiters = ".",";"," ",":","(",")","'",'"',"{","}","[","]","|","\\","/","\n"
    regexPattern = '|'.join(map(re.escape, delimiters))
    words = [word.lower() for word in re.split(regexPattern,text) if ((word.lower() not in sw_nltk) and (word.isalpha())and(len(word)>1))]
    return words

'''Goes through a defined nlp pipeline edit'''
def netCleaner(titleString,descriptionString):
    words = cleanPosting(titleString,descriptionString)
    print(words)
    print('\n')

    words = list(dict.fromkeys(words))
    print(words)

    wordsString = listToString(words)

    nlp = stanza.Pipeline()
    text = nlp(wordsString)

    #Lemmatization
    lemmed_words = []
    for i in text.sentences:
        for j in i.words:
            lemmed_words.append((j.lemma))
    
    return lemmed_words





