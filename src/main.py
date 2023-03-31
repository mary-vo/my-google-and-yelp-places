import pandas as pd
import os
from add_remove_columns import (google_csv_add_col_df, google_json_add_col_df,yelp_html_add_col_df)
from remove_null_places import remove_null_name_rows
from source_dataframe import (read_google_csv_files, read_google_json_files,read_yelp_html_files)


def main():
    yelp_dataframe = read_yelp_html_files()
    google_csv_dataframe = read_google_csv_files()
    google_json_dataframe = read_google_json_files()

    """Remove records/rows in the following 
    dataframes where 'Business Name' or 'Title' is null"""
    google_json_remove_null = remove_null_name_rows(google_json_dataframe, 'properties.Location.Business Name')
    google_csv_remove_null = remove_null_name_rows(google_csv_dataframe, 'Title')

    """Pass df into google_csv_add_col_df() to return
    a dataframe with City, State, and Country columns"""
    google_csv_cols_df = google_csv_add_col_df(google_csv_remove_null)

    """Pass df into google_json_add_col_df() to return a
    dataframe with City, State, and Country columns"""
    google_json_cols_df = google_json_add_col_df(google_json_remove_null)

    """Pass df into yelp_html_add_col_df() to rreturn a 
    dataframe with City, State, and Country columns"""
    yelp_html_cols_df = yelp_html_add_col_df(yelp_dataframe)

    """Append the three dataframes"""
    final_dataframe = pd.concat([google_csv_cols_df, google_json_cols_df, yelp_html_cols_df], ignore_index=True)
    final_dataframe.to_excel("../data-analysis/curated_data.xlsx", index=False)

    return final_dataframe


if __name__ == "__main__":
    main()