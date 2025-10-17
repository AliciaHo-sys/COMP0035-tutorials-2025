""""
# Different hierachies
def main():
    from importlib import resources

    from activities import data

    paralympics_data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")
    print( paralympics_data_file_csv.exists())

if __name__ == "__main__":
    main()

"""

def categorical_identify(df_file):
    print("Distinct categorical values in the event 'type' column")
    print(df_file['type'].unique())
    print("\n", "Count of each distinct categorical value in the event 'type' column")
    print("", end=" ")
    print(df_file['type'].value_counts())

def data_prep(df):
    # Example 1: Find a row/column that matches a certain condition using loc with a query or mask
    df.loc[df.query("type == 'Summer'").index, 'type'] = 'summer' # query
    df.loc[df['type'] == 'Summer', 'type'] = 'summer' # mask

    # Example 2: Find the index of the row using `query`, and then use `at` to update the value.
    # NB Assumes only 1 row matches the criteria, amend to loop through all matching indices if more than one result.
    index = df.query("type == 'Summer'").index[0]
    df.at[index, 'type'] = 'summer'

    # Example 3: Uses iloc which only works with integers so you need to find the row & column integer references first
    row_pos = df.query("type == 'Summer'").index[0]
    row_idx = df.index.get_loc(row_pos)
    col_idx = df.columns.get_loc('type')
    df.iloc[row_idx, col_idx] = 'summer'

#alternate method    
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
def main():
    # This script is located in the project root, so find the path to the current file and then go to the parent of that file
    project_root = Path(__file__).parent.parent

    # Find the .csv file relative to the project root and join to that path the data folder and then the example.csv file
    csv_file = project_root.joinpath('activities', 'data', 'paralympics_raw.csv')
    # csv_file = project_root / 'data' / 'example.csv' # this notation would also work, even though you think the '/' is only unix/macOS

    # Check if the file exists, this will print 'true' if it exists
    print(csv_file.exists())
    events_csv_df = pd.read_csv(csv_file)

    
    #read_file = pd.read_csv(csv_file, sheet_name= 1)
    #categorical_identify(events_csv_df)
    data_prep(events_csv_df)
   # events_csv_df.boxplot()
    #plt.show()
    
   
if __name__ == "__main__":
    main()
