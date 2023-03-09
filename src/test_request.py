import requests
import json
import pandas as pd
from source_dataframe import read_yelp_html_files

pd.set_option("display.max_columns", None)
url = "https://api.yelp.com/v3/businesses/"

# Replace <API_KEY> with your actual API key
headers = {"Authorization": "Bearer ZaHj8pnRb-ZR7uouhmh7VBnNhHiDUxhTcL4_tYaPNJkxsCjmbE5HkX31ThpF5d_wik1aZ5mhOON8rMvIzVuc7Ezuq4DJo0wMY1Tj1Rax5-z4X8ruzGZFsgGN4lM7X3Yx"}

html_dataframe = read_yelp_html_files()
html_dataframe['endpoint']="https://api.yelp.com/v3/businesses/" + (html_dataframe['Business URL'].str.split('/').str[-1])
print(html_dataframe)


# response = requests.get(url=url, headers=headers)
# result = json.loads(response.text)
# print(result)