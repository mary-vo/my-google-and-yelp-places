# Background on Project: The Why?

The purpose of this project is to clean, combine, and display Google and Yelp data that I have saved through the years. The idea is to store the data in a more tabular format for ease of readability and filtering by location and notes.

Over the years, I have created quite a list of places on both platforms. However, this "list" is not easily sortable. See examples below, evidenced by the fact that I'd have to select each heart to view personal notes (if any available):

![image](https://user-images.githubusercontent.com/91100579/221379047-9c043274-21b4-4610-b61e-dcaa60215449.png)
![image](https://user-images.githubusercontent.com/91100579/221379020-0fc90bb4-bbb8-4e89-ad53-60e4f95e6f17.png)

The notes sometimes offer handy information such as: dishes to try, price, happy hour, etc. It varies by place. As mentioned previously, these places and notes are stored across two platforms (Google and Yelp). It would be ideal to have it in a single location.

For a better idea of the project plan that details steps taken to complete the project, view [Project Plan Diagram](/Project%20plan%20diagram.png).

# Background on the code

First, I gathered all my Google and Yelp data. These are stored under [source-data-files](source-data-files) directory. There are six total files ranging in csv, json, or html format. I left them in the original format they were provided to me.

## [source_dataframe.py](src/source_dataframe.py) `<br />`

Purpose: Read all the data files into dataframes.

Outcome: I chose to read the files and return them in three dataframes; separated by file format: csv, json, and html dataframe. Note, there are three functions, one for each dataframe.

## [remove_null_places.py](src/remove_null_places.py) `<br />`

Purpose: I discovered that there were "null" business/titles in some of the dataframes. This occurs when a business has permanently closed.

Outcome: Created a function to remove null Business Name or Title from csv and json dataframe returned in [source_dataframe.py](src/source_dataframe.py).

## [add_remove_columns.py](src/add_remove_columns.py) `<br />`

Purpose: The downloaded Google and Yelp data was missing location information (City, State, and Country).

Outcome: A lookup against Google Maps API and Yelp API helped return City, State, Country information for each business. Additionally, unnecessary columns were dropped in the return statement of each function.

## [main.py](src/main.py) `<br />`

Purpose: This is where all the above programs are combined to return a single output file.

Outcome: A single output file that is used for data analysis. Interpretation to follow below.

## [analysis.ipynb](data-analysis/analysis.ipynb) `<br />`

Purpose: At this point, I can start viewing and analyzing the data.

Outcome: I was able to view my data and identified areas where additional cleansing is required.

# Features Used

1. Read data in
   * Read in HTML, json, and csv files + json file is parsed, returned as dictionary, and flattened into a flat table as seen here: [source_dataframe.py](src/source_dataframe.py)
   * Use Google Maps API and Yelp API as seen here: [add_remove_columns.py](src/add_remove_columns.py)
2. Manipulate and clean your data
   * Remove null records as seen here: [remove_null_places.py](src/remove_null_places.py)
   * Add and drop columns as seen here: [add_remove_columns.py](src/add_remove_columns.py)
3. Analyze your data: [analysis.ipynb](data-analysis/analysis.ipynb)
   * Used info() and describe() to get basic information about the data
   * Used nunique() to return unique/distinct for each column in the dataframe
   * Used filtering in dataframes to return only places in the United States
   * Merged dataframe (for map visualization)
   * Use len() to return the count of records in dataframe
   * Used str.contains() to complete a string search in a column
4. Visualize your data

* Created a choropleth map
* Create a bar chart

5. Interpret your data
   * Please view interpretation of data throughout the markdown in Juypter notebook

# Usage

Follow these steps to run the program on your local machine:

* Clone project:
  * Open desired terminal
  * cd to desired location
  * run `git clone git@github.com:mary-vo/my-google-and-yelp-places.git`
* Open project in Visual Studio:
  * Open Visual Studio > File > Open Folder... > Navigate to location where project was cloned > click "Select Folder"
* Create and activate a virtual environment
  1. In terminal, type: `python -m venv venv`
  2. Activate the virtual environment, commands vary based on terminal:
     * bash: `source venv/Scripts/activate`
     * powershell: `.\venv\Scripts\activate`
     * command prompt: `venv\Scripts\activate`
* While in the root directory, run `pip install -r requirements.txt`
* Add API Keys in [add_remove_columns.py](src/add_remove_columns.py), on lines: 24, 53, 70 (see text file provided via Slack)
* In the terminal, cd to `src` > run `python main.py`. Note: Project can take ~18 minutes to run. If you want to reduce run time, limit data by making the following modifications in [source_dataframe.py](src/source_dataframe.py):
  * Line 19, 31, and 43: df = pd.concat(df_list,ignore_index=True)**.head(200)**
* Upon completion a file called "curated_data.xlsx" will be created under data-analysis folder
* Run [analysis.ipynb](src/analysis.ipynb)
  * You may need to choose your environment. Run All > Python Environments > choose Python environment (or venv)
