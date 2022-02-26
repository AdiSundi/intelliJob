#!/usr/bin/env python3

import pandas as pd
import json

def ruleset_func():

    url = 'https://www.enableacademy.org/resources/jobs-done-by-persons-with-disability/'

    df=pd.read_html(url)[0]

    # Make list of roles for LV impairment
    dict_table={'LV':{}, 'HI': {}, 'MPD': {}, 'PD': {}, 'CP': {}, 'SCI': {}, 'ASD': {}}
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

    return dict_overall