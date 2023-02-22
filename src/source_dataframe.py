import os
import pandas as pd
import json

def read_yelp_html_files():
    yelp_path = os.path.join('..','data_files','yelp\\')
    # print(f"printing path: {yelp_path}")
    dir = os.listdir(yelp_path)
    # print(f"print dir: {dir}")
    df_list=[]
    for i in range(len(dir)):
        data = pd.read_html(yelp_path + dir[i])
        # print(data)
        # print(len(data))
        df_list.append(data[0])
    df = pd.concat(df_list)
    print(df)
        # final_dataframe = pd.concat(data)
    # dataframe = pd.concat(df_list)
    # print(dataframe)
    df.to_excel("combined_yelp_data.xlsx", index=False)
    return df

google_path = os.path.join('..','data_files','google\\')

def read_google_csv_files():
    df_list=[]
    for file in os.listdir(google_path):
        if file.endswith(".csv"):
            data = pd.read_csv(google_path + file)
            df_list.append(data)
        df = pd.concat(df_list)
        df.to_excel("combined_google_csv_data.xlsx", index=False)
    return df
        
def read_google_json_files():
    df_list=[]
    for file in os.listdir(google_path):
        if file.endswith(".json"):
            with open(os.path.join(google_path,file), "r", encoding='utf-8') as f:
                print(file)
                data = json.load(f)
                df_nested_list = pd.json_normalize(data,record_path=["features"])
                df_list.append(df_nested_list)
            df = pd.concat(df_list)
            df.to_excel("combined_google_json_data.xlsx", index=False)


read_yelp_html_files()
read_google_csv_files()
read_google_json_files()

