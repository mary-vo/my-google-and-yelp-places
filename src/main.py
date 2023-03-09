from add_columns import google_csv_add_col_df
from remove_null_places import remove_null_name_rows
from source_dataframe import read_google_csv_files, read_google_json_files, read_yelp_html_files

def main():
    yelp_dataframe = read_yelp_html_files()
    google_csv_dataframe = read_google_csv_files()
    google_json_dataframe = read_google_json_files()

    """Remove records/rows in the following 
    dataframes where 'Business Name' or 'Title' is null"""
    print("Creating removed null record excel...")
    google_json_remove_null = remove_null_name_rows(google_json_dataframe, 'properties.Location.Business Name')
    google_csv_remove_null = remove_null_name_rows(google_csv_dataframe, 'Title')

    # google_json_remove_null.to_excel("google_json_remove_null.xlsx", index=False)
    # google_csv_remove_null.to_excel("google_csv_remove_null.xlsx", index=False)

    """Pass google_csv_df into google_csv_normalized_df() to return
    a dataframe: google_csv_df with City, State, and Country columns"""
    print("Creating normalized google csv...")
    google_csv_norm_df = google_csv_add_col_df(google_csv_remove_null)
    # google_csv_norm_df.to_excel('google_csv_normalized.xlsx', index=False)



if __name__ == "__main__":
    main()