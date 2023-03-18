"""
Add city, state, country column to the df returned in
read_google_csv_files() and read_google_json_files()

Return df with newly added columns and remove un-necessary columns
to set up for final union
"""
import requests
import json
# import pandas as pd
# from source_dataframe import read_google_csv_files, read_google_json_files, read_yelp_html_files
# from remove_null_places import remove_null_name_rows


def google_csv_add_col_df(google_csv_df):
    google_csv_df['City'] =''
    google_csv_df['State'] =''
    google_csv_df['Country'] =''
    google_csv_df['cid'] = google_csv_df['URL'].str.split(':').str[-1]
    url_string = 'https://maps.googleapis.com/maps/api/place/details/json?'
    for row in google_csv_df.index:
        # print(google_csv_df['Title'][row],google_csv_df['Note'][row])
        params = {'cid':google_csv_df['cid'][row], 'key':''}
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

    return google_csv_df.drop(['URL','Comment','cid'], axis=1).rename(columns={'Title':'Business Name'})


def google_json_add_col_df(google_json_df):
    google_json_df=google_json_df.copy()
    google_json_df['latlng'] = google_json_df['properties.Location.Geo Coordinates.Latitude'] + "," + google_json_df['properties.Location.Geo Coordinates.Longitude']
    google_json_df['City'] =''
    google_json_df['State'] =''
    google_json_df['Country'] =''
    google_json_df['Note'] = ''
    url_string = 'https://maps.googleapis.com/maps/api/geocode/json?'
    for row in google_json_df.index:
        params = {'latlng':google_json_df['latlng'][row], 'key':}
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

    return google_json_df.drop(google_json_df.columns[[0,1,2,3,4,5,6,7,8,9,11,12]], axis=1).\
        rename(columns={'properties.Location.Business Name':'Business Name'})


def yelp_html_add_col_df(yelp_html_df):
    headers = {"Accept": "*/*", "Authorization": "Bearer "}
    yelp_html_df['City']=''
    yelp_html_df['State'] =''
    yelp_html_df['Country'] =''
    yelp_html_df['endpoint']="https://api.yelp.com/v3/businesses/" + (yelp_html_df['Business URL'].str.split('/').str[-1])
    # yelp_html_df.to_excel("yelp_html_endpoint.xlsx", index=False)
    for row in yelp_html_df.index:
        # try:
        #     raise requests.exceptions.RequestException
        r = requests.get(url=yelp_html_df['endpoint'][row], headers=headers)
        # print(yelp_html_df['endpoint'][row])
        response_dict = json.loads(r.text)
        # print(response_dict)
        if r.status_code != 403: 
            yelp_html_df['City'][row] = response_dict['location']['city']
            yelp_html_df['State'][row] = response_dict['location']['state']
            yelp_html_df['Country'][row] = response_dict['location']['country']
            # yelp_html_df.to_excel("yelp_html_add_cols.xlsx", index=False)
        # except requests.exceptions.RequestException as e:
        #     raise SystemExit(e)
    return yelp_html_df.drop(yelp_html_df.columns[[0,2,4,5,6,10]], axis=1)


"""Testing/calling the functions above"""
# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)

# csv_dataframe = remove_null_name_rows(read_google_csv_files(), 'Title')
# csv_result = google_csv_add_col_df(csv_dataframe)
# print(csv_result)
# csv_result.to_excel('csv_dataframe_return.xlsx',index=False)

# json_dataframe = remove_null_name_rows(read_google_json_files(), 'properties.Location.Business Name')
# # print(json_dataframe['properties.Location.Geo Coordinates.Latitude'].dtype)
# json_result = google_json_add_col_df(json_dataframe)
# print(json_result)

# yelp_dataframe = read_yelp_html_files()
# print(yelp_html_add_col_df(yelp_dataframe))