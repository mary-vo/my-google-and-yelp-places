"""
TL;DR: Remove records where "Business Name" or "Title" is null

After getting a source dataframe for each type of data file
(csv, json, and html), the Google specific data needs to be cleansed.
Google is returning instances where business have closed -- for these instances, 
clean the data to remove those records. These records will not
have a "Business Name" in the read_google_json_files() or "Title"
in read_google_csv_files(). 

"""

import pandas as pd
import source_dataframe

# pd.set_option('display.max_columns', None)

"""
Remove rows with null / empty "Business Name" or "Title"
"""
def remove_null_name_rows(df, name):
    return df.loc[df[name].notnull()]

# print(remove_null_name_rows(source_dataframe.read_google_json_files(), 
#                       'properties.Location.Business Name'))
# result = remove_null_name_rows(source_dataframe.read_google_json_files(), 
#                       'properties.Location.Business Name')
# result.to_excel("google_json_remove_null.xlsx", index=False)

# print(remove_null_name_rows(source_dataframe.read_google_csv_files(), 
#                       'Title'))
# result = remove_null_name_rows(source_dataframe.read_google_csv_files(), 
#                       'Title')
# result.to_excel("google_csv_remove_null.xlsx", index=False)
