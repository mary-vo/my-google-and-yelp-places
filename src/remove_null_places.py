"""
TL;DR: Remove records where "Business Name" or "Title" is null

Google returns instances where a business have closed -- for these instances, 
clean the data to remove those records. These records will not
have a "Business Name" in the read_google_json_files() or "Title"
in read_google_csv_files(). 

"""

def remove_null_name_rows(df, name):
    return df.loc[df[name].notnull()]

# pd.set_option('display.max_columns', None)
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
