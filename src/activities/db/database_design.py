from importlib import resources

from pathlib import Path

import pandas as pd



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

def add(games_df):
    """ Example function to add columns to the games dataframe

    Args:
        games_df (pd.DataFrame): Dataframe of games

    Returns:
        pd.DataFrame: Dataframe of games with new columns added
    """
    # Add a new gamesId column (stable string IDs)
    # If 'type' exists, insert the new column just before it; otherwise insert at position 0
    try:
        insert_pos = games_df.columns.get_loc('type') - 1
        if insert_pos < 0:
            insert_pos = 0
    except Exception:
        insert_pos = 0
    pd.set_option("display.max_columns", None)
    # Create stable string IDs using the dataframe index order: G1, G2, ...
    ids = pd.Series([f"{n}" for n in range(1, len(games_df) + 1)], index=games_df.index)

    # Insert the new column
    games_df.insert(insert_pos, 'gamesId', ids)

    # Add new dataframes
    disability = games_df['disabilities_included']
    disability_Id = pd.Series([f"{n}" for n in range(1, len(disability) + 1)], index=disability.index)
    disability_df = pd.DataFrame({'disabilityId': disability_Id, 'disability': disability})
    
    country, host = games_df['country'], games_df['host']
    country_Id = pd.Series([f"{n}" for n in range(1, len(country) + 1)], index=country.index)
    country_df = pd.DataFrame({'countryId': country_Id, 'country': country})
    host_Id = pd.Series([f"{n}" for n in range(1, len(host) + 1)], index=host.index)
    host_df = pd.DataFrame({'hostId': host_Id, 'host': host})
    #print("\nDataframe with new gamesId column added:\n", games_df)
    return games_df, disability_df, country_df, host_df

""" 
def create_db(sql_script_path, db_path):
    
    Creates a new SQLite database using the provided SQL script.

    Args:
        sql_script_path (Path): Path to the SQL script file
        db_path (Path): Path where the database should be created
    
    try:
        # Read the SQL script content
        with open(sql_script_path, 'r') as sql_file:
            sql_script = sql_file.read()

        # Create and execute the database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()

    except sqlite3.OperationalError as e:
        print(f"SQLite error: {e}")
        raise
    except FileNotFoundError:
        print(f"SQL script file not found at: {sql_script_path}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        if 'connection' in locals():
            connection.close()
"""



def main():
    """ Included to give an example of how to use the methods """
    path_para_raw = Path(__file__).parent.parent.joinpath("data", "paralympics_all_raw.xlsx")
    
    df_games, df_codes = read_data_to_df(path_para_raw)
    sql_path = Path(__file__).parent.parent.joinpath("starter", "student_schema.sql")
    #create_db(sql_path, db_path)
    #describe(df_games, df_codes)
    print(add(df_games))


if __name__ == '__main__':
    main()
