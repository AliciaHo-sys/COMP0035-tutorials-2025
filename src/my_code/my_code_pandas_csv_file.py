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

    events_csv_df.boxplot()
    plt.show()
    
   
if __name__ == "__main__":
    main()
