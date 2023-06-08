"""
This program reads in all the data files (6 files in total). 
The goal is to load each type of file into a single dateframe.
For example, all CSV data will be in a single dataframe; 
all html records will be in its own dataframe.
"""

import os
import pandas as pd
import json

def read_yelp_html_files():
    yelp_path = os.path.join('..','source-data-files','yelp\\')
    dir = os.listdir(yelp_path)
    df_list=[]
    for i in range(len(dir)):
        data = pd.read_html(yelp_path + dir[i])
        df_list.append(data[0])
    df = pd.concat(df_list,ignore_index=True)
    return df

google_path = os.path.join('..','source-data-files','google\\')

def read_google_csv_files():
    df_list=[]
    for file in os.listdir(google_path):
        if file.endswith(".csv"):
            data = pd.read_csv(google_path + file)
            df_list.append(data)
    df = pd.concat(df_list,ignore_index=True)
    return df
        
def read_google_json_files():
    df_list=[]
    for file in os.listdir(google_path):
        if file.endswith(".json"):
            with open(os.path.join(google_path,file), "r", encoding='utf-8') as f:
                data = json.load(f)
                df_nested_list = pd.json_normalize(data,record_path=["features"])
                df_list.append(df_nested_list)
    df = pd.concat(df_list,ignore_index=True)
    return df    

read_yelp_html_files().to_excel("data/yelp_html.xlsx")
read_google_csv_files().to_excel("data/google_csv.xlsx")
read_google_json_files().to_excel("data/google_json.xlsx")