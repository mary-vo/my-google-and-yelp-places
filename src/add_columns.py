"""
Add city, state, country column to the df returned in
read_google_csv_files() and read_google_json_files()
"""
import requests
import json
# from source_dataframe import read_google_csv_files, read_google_json_files
# from remove_null_places import remove_null_name_rows
# import pandas as pd

# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)

# csv_dataframe = remove_null_name_rows(read_google_csv_files(), 'Title')

def google_csv_add_col_df(google_csv_df):
    google_csv_df['City'] =''
    google_csv_df['State'] =''
    google_csv_df['Country'] =''
    google_csv_df['cid'] = google_csv_df['URL'].str.split(':').str[-1]
    url_string = 'https://maps.googleapis.com/maps/api/place/details/json?'
    for row in google_csv_df.index:
        # print(google_csv_df['Title'][row],google_csv_df['Note'][row])
        params = {'cid':google_csv_df['cid'][row], 'key':'AIzaSyCwpEZPccfcl8cWWlfsGCauLY8s04bMy7Q'}
        r = requests.get(url = url_string, params=params)
        # print(row)
        response_dict = json.loads(r.text)
        if response_dict["status"] != "NOT_FOUND" and response_dict["status"] != "INVALID_REQUEST":
            for type in response_dict["result"]["address_components"]:
                if type["types"] == ['locality', 'political']:
                    # print(f"City:{type['long_name']}")
                    google_csv_df.loc[row,'City']=type['long_name']
                    # print(f"printing title: {google_csv_df['Title']}")
                if "administrative_area_level_1" in type["types"]:
                #     # print(f"State:{type['long_name']}")
                    google_csv_df.loc[row,'State']=type['long_name']
                if "country" in type["types"]:
                #     # print(f"Country:{type['long_name']}")
                    google_csv_df.loc[row,'Country']=type['long_name']

    return google_csv_df


# csv_result = google_csv_add_col_df(csv_dataframe)
# print(csv_result)

# json_dataframe = remove_null_name_rows(read_google_json_files(), 'properties.Location.Business Name')
# # print(json_dataframe['properties.Location.Geo Coordinates.Latitude'].dtype)

def google_json_add_col_df(google_json_df):
    google_json_df['latlng'] = google_json_df['properties.Location.Geo Coordinates.Latitude'] + "," + google_json_df['properties.Location.Geo Coordinates.Longitude']
    google_json_df['City'] =''
    google_json_df['State'] =''
    google_json_df['Country'] =''
    url_string = 'https://maps.googleapis.com/maps/api/geocode/json?'
    for row in google_json_df.index:
        params = {'latlng':google_json_df['latlng'][row], 'key':'AIzaSyCwpEZPccfcl8cWWlfsGCauLY8s04bMy7Q'}
        r = requests.get(url = url_string, params=params)
        response_dict = json.loads(r.text)
        if response_dict["status"] != "NOT_FOUND" and response_dict["status"] != "INVALID_REQUEST":
            for type in response_dict["results"][0]["address_components"]:
                if type["types"] == ['locality', 'political']:
                    google_json_df.loc[row,'City']=type['long_name']
                if "administrative_area_level_1" in type["types"]:
                    google_json_df.loc[row,'State']=type['long_name']
                if "country" in type["types"]:
                    google_json_df.loc[row,'Country']=type['long_name']

    return google_json_df

# json_result = google_json_add_col_df(json_dataframe)
# print(json_result)