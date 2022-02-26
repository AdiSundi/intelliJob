#!/usr/bin/env python3

import urllib.request
#from bs4 import BeautifulSoup
import pandas as pd
import json

user_agent = \
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'https://www.enableacademy.org/resources/jobs-done-by-persons-with-disability/'
headers = {'User-Agent': user_agent}

request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
data = response.read().decode(response.headers.get_content_charset())

df=pd.read_html(url)[0]

# Make list of roles for LV impairment
dict_table={'LV':{}, 'VI': {}, 'HI': {}}
dict_key_list=list(dict_table.keys())
for index, row in df.iterrows():
    #Get list of disabilities
    list_text=row['Disability'].split(" ")
    function=row['Function']
    list_role=row['Role'].strip().split('/')
    
    for iter in list_text:
        if iter in dict_key_list:
            if function not in dict_table[iter]: 
                dict_table[iter][function]=[]
                dict_table[iter][function].append(list_role)
            else:
                dict_table[iter][function].append(list_role)

dict_overall = {}

for key in dict_table:
    temp_list = []
    for key2 in dict_table[key]:
        for i in dict_table[key][key2]:
            temp_list.extend(i)
    dict_overall[key]=temp_list
print(json.dumps(dict_overall,indent=2))