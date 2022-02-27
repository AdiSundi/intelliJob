#!/usr/bin/env python3

from statistics import mode
import pandas as pd
import fasttext
import os.path

'''Model predictor which uses the cleaned bindings and trained model, to generate disability class TAGS for JOB postings on INDEED'''

list_dis=['LV', 'HI', 'MPD', 'PD', 'CP']

model_LV=None
model_HI=None
model_MPD=None
model_PD=None
model_CP=None

model_dict={'LV':model_LV, 'HI':model_HI, 'MPD':model_MPD, 'PD':model_PD, 'CP':model_CP}

# Make the model and train
for dis in list_dis:
    if os.path.isfile(dis+'.txt'):
        continue
    else:
        print ("Generating model!")
        model = fasttext.train_unsupervised(dis+'.txt', minCount=1)
        model.save_model(dis+'.bin')

# Load the model 
for dis in model_dict:
    model = fasttext.load_model(dis+'.bin')
    model_dict[dis]=model

# Read the Indeed Dataframe
indeed_df = pd.read_excel('Rated_650JobPostings_cleaned.xlsx')

indeed_df.drop(columns=indeed_df.columns[0], inplace=True)

val_dict={'LV':[], 'HI':[], 'MPD':[], 'PD':[], 'CP':[]}

# Loop through dataframe and do OHE for disability classes

# threshold for nearest neighbor is declared
thres=0.45

for index, row in indeed_df.iterrows():
  text=row['title']

  text_h=text.replace(" ", "-")

  text_s1=text_h.split("#")
  text_ss1=text_s1[0]

  text_s2=text_ss1.split("(")
  text_ss2=text_s2[0]

  text_s3=text_ss2.split("@")
  text_ss3=text_s3[0]

  text_s4=text_ss3.split("/")
  text_ss4=text_s4[0]

  # Loop thru each disability class
  for dis in list_dis:
    op=model_dict[dis].get_nearest_neighbors(text_ss4)
    # Get the best value from the o/p
    corr_val=op[0][0]
    # Add to df for now
    if (corr_val>0.45):
      val_dict[dis].append(1)
    else:
      val_dict[dis].append(0)

nearest_neighbor_df=pd.DataFrame(val_dict)

# Export the csv file for further front-end purposes to display to end user
indeed_result_df = pd.concat([indeed_df, nearest_neighbor_df], axis=1)
indeed_result_df.to_csv("indeed_ODE.csv")
