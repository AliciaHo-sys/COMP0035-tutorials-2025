import pandas as pd
from pathlib import Path
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
    
    #print_shape = print(xlsx_file.shape), print the no of columns and rows

    #print_head = print(xlsx_file.head()), print the first 5 rows

    #print_tail = print(xlsx_file.tail()), print the last 5

    #print_col_label = print(xlsx_file.columns), print column labels
    
    #print_dtypes = print(xlsx_file.dtypes), print data types

    #print_info = xlsx_file.info(), print column, non-null count and data type

    """
    print_describe = print(xlsx_file.describe()), 
    print count → number of non-missing values
    mean → average
    std → standard deviation (spread of the data)
    min / 25% / 50% / 75% / max → percentiles (summary statistics)

    if (include='object'), print count, unique( no of no-null entries), top (most frequent value) and frequency(frequency of the top value)
    """

    pd.set_option("display.max_columns", None)
   
if __name__ == "__main__":
    # Filepath of the csv data file (you may have used importlib.resources rather than pathlib.Path)
    paralympics_xlsx = Path(__file__).parent.parent.joinpath("activities", "data", "paralympics_all_raw.xlsx")

    # Read the data from the file into a Pandas dataframe
    name_of_sheet = "games"
    events_xlsx_df = pd.read_excel(paralympics_xlsx, sheet_name= name_of_sheet)
   
    # Call the function named 'describe_dataframe' - you may have a different name for your function
    describe(events_xlsx_df)