"""
Take result df from read_google_csv_file()
and add city, state, country column
"""
import requests
import source_dataframe
import json

csv_dataframe = source_dataframe.read_google_csv_files()


def google_csv_normalized_df(csv_dataframe):
    csv_dataframe['City'] =''
    csv_dataframe['State'] =''
    csv_dataframe['Country'] =''
    csv_dataframe['cid'] = csv_dataframe['URL'].str.split(':').str[-1]
    url_string = 'https://maps.googleapis.com/maps/api/place/details/json?'
    for row in csv_dataframe.index:
        # print(csv_dataframe['Title'][row],csv_dataframe['Note'][row])
        params = {'cid':csv_dataframe['cid'][row], 'key':''}
        r = requests.get(url = url_string, params=params)

        response_dict = json.loads(r.text)
        # compound_code = dict["result"]["plus_code"]["compound_code"]
        for type in response_dict["result"]["address_components"]:
            if type["types"] == ['locality', 'political']:
                # print(f"City:{type['long_name']}")
                csv_dataframe.loc[row,'City']=type['long_name']

            if "administrative_area_level_1" in type["types"]:
            #     # print(f"State:{type['long_name']}")
                csv_dataframe.loc[row,'State']=type['long_name']

            if "country" in type["types"]:
            #     # print(f"Country:{type['long_name']}")
                csv_dataframe.loc[row,'Country']=type['long_name']
    return csv_dataframe 

