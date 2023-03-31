"""
TL;DR: Remove records where "Business Name" or "Title" is null

Google returns instances where a business have closed -- for these instances, 
clean the data to remove those records. These records will not
have a "Business Name" in the read_google_json_files() or "Title"
in read_google_csv_files(). 

"""

def remove_null_name_rows(df, name):
    return df.loc[df[name].notnull()]