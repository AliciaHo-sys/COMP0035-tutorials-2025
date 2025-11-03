from importlib import resources

import pandas as pd

from activities import data
from activities import starter

from pathlib import Path

import sqlite3
def read_data_to_df(data_path):
    """ Reads the data from Excel into two dataframes and returns these

    Args:
        data_path (str): Path to the raw data file

    Returns:
        df_games, df_country_codes (tuple [pd.DataFrame, pd.DataFrame]): tuple of dataframes

    Examples:

        from importlib import resources

        from activities import data

        path_raw = resources.files(data).joinpath("paralympics_all_raw.xlsx")
        df_games, df_codes = read_data_to_df(path_raw)
    """
    # Games sheet
    dict_event_dtypes = {
        'type': 'string',
        'year': 'Int64',
        'country': 'string',
        'host': 'string',
        # 'start': 'string', # Ignore, handled by parse_dates
        # 'end': 'string', # Ignore, handled by parse_dates
        'disabilities_included': 'string',
        'countries': 'Int64',
        'events': 'Int64',
        'sports': 'Int64',
        'participants_m': 'Int64',
        'participants_f': 'Int64',
        'participants': 'Int64',
        'highlights': 'string',
        'URL': 'string'
    }
    df_games = pd.read_excel(data_path, sheet_name="games", dtype=dict_event_dtypes, parse_dates=['start', 'end'])
    # Country code sheet
    dict_code_dtypes = {
        'Code': 'string',
        'Name': 'string',
        'Region': 'string',
        'SubRegion': 'string',
        'MemberType': 'string',
        'Notes': 'string'
    }
    df_country_codes = pd.read_excel(data_path, sheet_name="team_codes", dtype=dict_code_dtypes)
    return df_games, df_country_codes


def describe(games_df, codes_df):
    """ Prints data useful for the conceptual modelling activity
    
    Args:
        games_df (pd.DataFrame): Dataframe of games
        codes_df (pd.DataFrame): Dataframe of country codes

    """
    pd.set_option("display.max_columns", None)
    print("COUNTRY CODES\n")
    print("\nData types of the country codes sheet:\n", codes_df.dtypes)
    print("\nUnique values of Region\n", codes_df.Region.unique())
    print("\nUnique values of SubRegion\n", codes_df.SubRegion.unique())
    print("\nUnique values of MemberType\n", codes_df.MemberType.unique())
    print("\nGAMES\n")
    print("\nData types of the games sheet:\n", games_df.dtypes)
    # Read the contents of the disabilities_included column, split the strings using ',' as the separator, then find the
    # unique values only
    disability_category_list = pd.unique(
        games_df.disabilities_included.dropna()
        .str.split(',')
        .explode()
        .str.strip()
    )
    print("\nUnique values of disabilities_included\n", disability_category_list)
    print("\nFull contents of the games sheet\n\n", games_df)

def create_db(sql_script_path, db_path):
   connection = sqlite3.connect(db_path)
   cursor = connection.cursor()
   # Read the SQL script content from file
   with open(sql_script_path, 'r') as file:
        sql_script = file.read()
   cursor.executescript(sql_script)
   connection.commit()
   connection.close()

def main():
    """ Included to give an example of how to use the methods """
    path_para_raw = resources.files(data).joinpath("paralympics_all_raw.xlsx")
    df_games, df_codes = read_data_to_df(path_para_raw)
    describe(df_games, df_codes)
    sql_script_path = Path(__file__).parent.joinpath("paralympics_schema_starter.sql")
    db_path = Path(__file__).parent.joinpath("para_my_disa.db")
    if db_path.exists():
        db_path.unlink()  # Deletes the old database file
    create_db(sql_script_path, db_path)
    


if __name__ == '__main__':
    main()
