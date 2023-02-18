import os
import pandas as pd

yelp_path = os.path.join('..','data_files','yelp')

# How can I just iterate through both files: bookmark.html and collection.html? Should i?
# with open(yelp_path + '\\bookmark_shortened.html', "r") as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, 'html.parser')

    
    
# Return the header for dataframe
# def get_header():
#     fields = soup.find_all('th')
#     header_list = [] 
#     for field in fields:
#         header_list.append(field.text)
#     return header_list
# print(get_header())

# Return Date column for dataframe
# def get_datecol():
#     fields = soup.find_all('tbody')
#     # print(fields)
#     datecol_list = []
#     for field in fields:
#         datecol_list.append(field.text)
#     return datecol_list
# print(get_datecol())


# read the HTML table into a list of DataFrames
# for subdir, dirs, files in os.walk(top=yelp_path):
#     for file in files:
#         print(file)
table_list = pd.read_html(yelp_path + '\\bookmark_shortened.html')
print(table_list)
# # select the first table and convert it to a DataFrame
# df = pd.DataFrame(table_list[0])

# # Export dataframe to csv
# # df.to_csv("test.csv", index=False)

# # # print the DataFrame
# print(df)




# Read the HTML file and extract the table
# tables = pd.read_html(yelp_path + '\\bookmark_shortened.html')

# # The table we want is the first one in the list of tables
# df = tables[0]

# # Print the dataframe
# print(df)

