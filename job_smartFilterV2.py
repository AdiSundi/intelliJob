#!usr/bin/python3
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import stanza

titleString = "Work From Home - Proofreaders, English Tutors, Editors, Writers needed!"
descriptionString = """Remember the days when you were a student struggling to complete your English homework? Your parents were too tied up with work and your classmates were unable to explain the answers properly. You might have found yourself staying up till the wee hours trying to complete your assignment, or ended up borrowing your friends’ worksheets to fill in the answers in a rush before your teacher showed up.

Kids today are now struggling the same way you did, and we believe that this is an issue that can be solved easily.

We are looking for someone to be our dedicated Homework Helper, a homework crusader and the answer to all their woes.

WHY YOU SHOULD APPLY:

- You are a current/ex-MOE teacher or tutor, and you want to get back into teaching sans all the heavy lifting and rigorous marking.

- You want to be a guiding light for students struggling with English

- You want a 100% WFH job. We promise to never ask you to 'come back to the office'.

JOB DESCRIPTION

- You'll be given the work smartphone to answer (by text only) all students' queries about their assignments e.g. brainstorming composition ideas or helping to check their MCQ.

- Light marking e.g. 5 Synthesis & Transformation, 10 Grammar MCQ. You will not be required to mark writing assignments or comprehension. That will be handled by our marking team!

- Quite often, our students will have admin queries. You will be provided with a template answer guide. Otherwise, you can direct them to our centre's admin to handle the case.

- You do not need to reply immediately, just within 24 hours

- Working hours: mainly in the evening and weekends

If you think that this is the job for you, here's what you need to do:

Click the ‘Apply now’ button and submit your resume. (We will only consider candidates with a resume)
We will send you an application test by email.
If you pass the application test, you will be notified via your Indeed email.
Job Type: Part-time

Salary: $300.00 per month

Job Type: Part-time

Salary: $300.00 per month

Schedule: 

Flexible hours"""

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def cleanPosting(titleString:str,descriptionString:str)->list:
    text = titleString+" "+descriptionString
    sw_nltk = stopwords.words('english')
    delimiters = ".",";"," ",":","(",")","'",'"',"{","}","[","]","|","\\","/","\n"
    regexPattern = '|'.join(map(re.escape, delimiters))
    words = [word.lower() for word in re.split(regexPattern,text) if ((word.lower() not in sw_nltk) and (word.isalpha())and(len(word)>1))]
    return words

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

print(netCleaner(titleString,descriptionString))




