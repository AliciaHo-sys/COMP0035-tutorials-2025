import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
""""
def read():

    ##Activity 1
    # This script is located in the project root, so find the path to the current file and then go to the parent of that file
    project_root = Path(__file__).parent.parent

    # Find the .csv file relative to the project root and join to that path the data folder and then the example.csv file
    xlsx_file = project_root.joinpath('activities', 'data', 'paralympics_all_raw.xlsx')
    # csv_file = project_root / 'data' / 'example.csv' # this notation would also work, even though you think the '/' is only unix/macOS

    # Check if the file exists, this will print 'true' if it exists
    print(xlsx_file.exists())

    ##Activity 2
    name_of_sheet = "medal_standings"
    read_file = pd.read_excel(xlsx_file, sheet_name= name_of_sheet)

    return read_file

    #check if object passes is a DataFrame
    if isinstance(xlsx_file, pd.DataFrame):
        print("This is a Pandas DataFrame!")
    else:
        print("This is not a Pandas DataFrame.")

"""

def describe(xlsx_file):
    ##Activity 3
    """Summary or description of the function

        Parameters:
        argument1 (int): Description of argument1

        Returns:
        int: Description of the returning value

    """
    
    print_shape = print(xlsx_file.shape) #print the no of columns and rows

    print_head = print(xlsx_file.head()) # print the first 5 rows

    print_tail = print(xlsx_file.tail()) #print the last 5

    print_col_label = print(xlsx_file.columns) #print column labels
    
    print_dtypes = print(xlsx_file.dtypes) #print data types

    print_info = xlsx_file.info() #print column, non-null count and data type

    """
    print_describe = print(xlsx_file.describe()), 
    print count → number of non-missing values
    mean → average
    std → standard deviation (spread of the data)
    min / 25% / 50% / 75% / max → percentiles (summary statistics)

    if (include='object'), print count, unique( no of no-null entries), top (most frequent value) and frequency(frequency of the top value)
    """

    pd.set_option("display.max_columns", None)


def missing(excel_file_df):
    ##Activity 4
    print(excel_file_df)
    print(excel_file_df.isnull()) #show all rows with empty value in data set as true(empty) and false(filled)
    missing_rows = excel_file_df[excel_file_df.isna().any(axis=1)] #, extract rows with empty values
    print(missing_rows)
    missing_columns = excel_file_df[excel_file_df.isna().any(axis=1)]#, extract columns with empty values
    print(missing_columns)
    pd.set_option("display.max_columns", None)

def histo_box(file_df):
    ##Activity 5
    # Create a histogram of the DataFrame
    columns = ["participants_m", "participants_f"]#, specific columns in the DataFrame
    file_df[columns].hist()

    ##Activity 6
    #All columns
    
    boxplot = file_df.boxplot()
    plt.show()

    #Only sports column
    column = ["participants_f"]
    file_df[column].boxplot()
    
    # Show the plot
    plt.show()

def line_chart(xlsx_df):
    ##Activity 7
    #rint column, non-null count and data type
    #xlsx_df.pivot(xlsx_df["year"], xlsx_df["type"], xlsx_df["participants"]).plot()

    for season, group in xlsx_df.groupby("type"):
        color = "blue" if season.lower() == "winter" else "green"
        plt.plot(group["year"], group["participants"], label= season.capitalize(), color=color)

    plt.title("Paralympics Participants by Year and Season")
    plt.xlabel("Year")
    plt.ylabel("Participants")
   
    plt.show()
    
def categorical_data_identify(df_file):
    ## Activity 8
    print("Distinct categorical values in the event 'type' column")
    print(df_file['type'].unique())
    print("\n", "Count of each distinct categorical value in the event 'type' column")
    print("", end=" ")
    print(df_file['type'].value_counts())

def data_prep(para_xlsx_file, medals_df):
    # actions and save to a xlsx file
    
        ##Activity 10, 12(removing space)

    ## Example 1: Find a row/column that matches a certain condition using loc with a query or mask
    # para_xlsx_file.query("type == 'winter '") return rows with the specified type
    # .index extracts the index values of those rows
    # para_xlsx_file.loc[] selects those rows (by their index) and targets the type column
    # = 'winter' assign the "winter " to "winter" 
    #para_xlsx_file.loc[para_xlsx_file.query("type == 'winter ' ").index, 'type'] = 'winter'  # query
    para_xlsx_file.loc[:,"type"] = para_xlsx_file.loc[:,"type"].str.strip() #Activity 12, remove all entries from space
    #print(para_xlsx_file['type'].value_counts())
    #prob = para_xlsx_file.loc[para_xlsx_file['type'] == 'winter ', 'type'] = 'winter' # mask

    # Example 2: Find the index of the row using `query`, and then use `at` to update the value.
    # NB Assumes only 1 row matches the criteria, amend to loop through all matching indices if more than one result.
    index = para_xlsx_file.query("type == 'winter'").index[0]
    para_xlsx_file.at[index, 'type'] = 'winter'
    

    # Example 3: Uses iloc which only works with integers so you need to find the row & column integer references first
    row_pos = para_xlsx_file.query("type == 'winter'").index[0]
    row_idx = para_xlsx_file.index.get_loc(row_pos)
    col_idx = para_xlsx_file.columns.get_loc('type')
    para_xlsx_file.iloc[row_idx, col_idx] = 'winter'
    #print(row_pos, row_idx, col_idx) #correct
   
        ##Activity 11, drop columns in new DataFrame
    df_prepared = para_xlsx_file.drop(columns=['URL', 'disabilities_included', 'highlights']) #drop these columns
    #print(df_prepared.columns)
        ##Activity 13, covert all entries into integer dtype and handle NaN entries 
    columns_to_change= ['countries', 'sports', 'events', 'participants_m', 'participants_f', 'participants']
    for entries in columns_to_change:
        if df_prepared[entries].isna().any(): #Check any missing values in the column
            df_prepared[columns_to_change] = df_prepared[columns_to_change].astype('Int64')  # Handles NaN without replacing values
        else:
            df_prepared[columns_to_change] = df_prepared[columns_to_change].astype(int) #converting column entries into integers
    time_column = ['start', 'end']
    for time in time_column: #change time into data time format (D-M-Y)
        df_prepared[time] = pd.to_datetime(df_prepared[time], format='%d/%m/%Y')
   
   
    ##Activity 14
    #Add a new duration column
    duration_values = (df_prepared['end'] - df_prepared['start']).dt.days.astype('Int64')
    df_prepared.insert(df_prepared.columns.get_loc('end') + 1, 'duration', duration_values)

    
    ##Activity 15, merge files with matching columns and updating the Code of each country from reading a new file
    npc_xlsx = Path(__file__).parent.parent.joinpath("activities", "data", "npc_codes.xlsx")    
    npc_xlsx_df = pd.read_excel(npc_xlsx, usecols=['Code', 'Name'])
          
    replacement_names = {
    'UK': 'Great Britain',
    'USA': 'United States of America',
    'Korea': 'Republic of Korea',
    'Russia': 'Russian Federation',
    'China': "People's Republic of China"
}
    df_prepared['country'] = df_prepared['country'].replace(replacement_names)
   
    #tell how to merge, based on country names
    merged_df = df_prepared.merge(npc_xlsx_df, how='left', left_on='country', right_on='Name')  
    merged_df = merged_df.drop(columns = ['Name'])
    print(merged_df[['country', 'Code']])
    pd.set_option("display.max_columns", None)
    
           
    
    
        


 

if __name__ == "__main__":
    # Filepath of the csv data file (you may have used importlib.resources rather than pathlib.Path)
    paralympics_xlsx = Path(__file__).parent.parent.joinpath("activities", "data", "paralympics_all_raw.xlsx")
    

    # Read the data from the file into a Pandas dataframe
    name_of_sheet = "games"
    events_xlsx_df = pd.read_excel(paralympics_xlsx, sheet_name = name_of_sheet)
    
    name_2 = "medal_standings"
    awards_xlsx_df = pd.read_excel(paralympics_xlsx, sheet_name = name_2, usecols= ['Team', 'NPC'])
    
    
    
   
    ## Call the functions
        #Activity 8
    #categorical_data_identify(events_xlsx_df)

        #Activity 9 - 15
    data_prep(events_xlsx_df, awards_xlsx_df)

       



    ####Organise into activities
    #Activity 3
    #describe(events_xlsx_df)
    #missing(events_xlsx_df)
    #histo_box(events_xlsx_df)
    #line_chart(events_xlsx_df)