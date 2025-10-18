""" Examples of docstring styles and functions and class that are un-documented. """
import sqlite3

import pandas as pd
from matplotlib import pyplot as plt


# Google-style docstring specification: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
def get_column_names_g(db_path: str, table_name: str) -> list:
    """Retrieves a list of column names for the specified database table.

    Args:
        db_path: Path to the database file
        table_name: Name of the table

    Returns:
        col_names: List of column names
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Numpy-style docstring: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
def get_column_names_n(db_path: str, table_name: str) -> list:
    """
        Retrieves a list of column names for the specified database table.

        Parameters
        ----------
        db_path : str
            Path to the database file.
        table_name : str
            Name of the table.

        Returns
        -------
        col_names: list
            List of column names.
        """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Sphinx/reStructuredText style docstring: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
# AI prompt:   /doc Sphinx format docstring
def get_column_names_s(db_path: str, table_name: str) -> list:
    """
        Retrieves a list of column names for the specified database table.

        :param db_path: Path to the database file.
        :type db_path: str
        :param table_name: Name of the table.
        :type table_name: str
        :return: List of column names.
        :rtype: list
        """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Copilot in VSCode / PyCharm
# Place the cursor under the function name and generate a docstring e.g. '/doc Google-style docstring'
def generate_histogram(df: pd.DataFrame):
    """
    Generate and save histograms for a pandas DataFrame.
    This function creates and saves three sets of histogram plots:
    1. Histograms for all columns in the DataFrame that have plottable numeric types.
        Saved to "output/histogram_df.png".
    2. Histograms for the specific columns "participants_m" and "participants_f".
        Saved to "output/histogram_participants.png".
    3. Histograms for rows filtered where the "type" column equals "summer".
        Saved to "output/histogram_summer.png".
    Args:
         df (pd.DataFrame): Input DataFrame containing the data to visualize. Numeric
              columns will be plotted in the general histogram. For the specialized
              histograms this function expects (but does not require at call time)
              columns named "participants_m", "participants_f", and "type" to exist.
    Returns:
         None: The function writes PNG files to the "output/" directory as described
         above and does not return a value.
    Raises:
         ValueError: If `df` is None or empty.
         KeyError: If "participants_m" or "participants_f" are missing when attempting
              to create the participants-specific histogram, or if "type" is missing
              when attempting to create the filtered (summer) histogram.
         ImportError: If required plotting libraries (e.g., matplotlib or pandas)
              are not available in the environment.
         OSError: If the function is unable to write files to the "output/" directory
              (for example, due to missing directory or filesystem permissions).
    Notes:
         - The function relies on pandas.DataFrame.hist and matplotlib.pyplot.savefig.
         - It saves files but does not explicitly close or clear matplotlib figures;
            callers may want to ensure figures are closed (e.g., plt.close()) if
            generating many plots in a long-running process to avoid memory growth.
         - It is recommended to ensure that the "output/" directory exists and is
            writable before calling this function.
    Examples:
         >>> import pandas as pd
         >>> df = pd.DataFrame({
         ...     "participants_m": [10, 12, 9],
         ...     "participants_f": [8, 11, 7],
         ...     "type": ["summer", "winter", "summer"],
         ...     "score": [1.2, 3.4, 2.1]
         ... })
         >>> generate_histogram(df)
         # -> Writes output/histogram_df.png, output/histogram_participants.png,
         #    and output/histogram_summer.png
    """
    

    # Histogram of any columns with values of a data type that can be plotted
    df.hist(
        sharey=False,  # defines whether y-axes will be shared among subplots.
        figsize=(12, 8)  # a tuple (width, height) in inches
    )
    plt.savefig("output/histogram_df.png")

    # Histograms of specific columns only
    df[["participants_m", "participants_f"]].hist()
    plt.savefig("output/histogram_participants.png")

    # Histograms based on filtered values
    summer_df = df[df['type'] == 'summer']
    summer_df.hist(sharey=False, figsize=(12, 8))
    plt.savefig("output/histogram_summer.png")


# Copilot in VSCode / PyCharm
# If you are happy to use gen-AI tools, place the cursor under the docstring and ask the AI to generate the code
def describe(csv_data_file: str) -> dict:
    """Opens the data as a pandas DataFrame applies pandas functions to describe the data.

    Applies the following pandas functions to the DataFrame and prints the output to file instead of terminal:
        df.shape
        dd.head(num)
        df.tail(num)
        df.columns
        df.dtypes
        df.describe()
        df.info()

       Args:
       csv_data_file (str): File path of the .csv format data file.

    """
    df = pd.read_csv(csv_data_file)
    description = {
        "shape": df.shape,
        "head": df.head(),
        "tail": df.tail(),
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.to_dict(),
        "describe": df.describe().to_dict(),
        "info": df.info()
    }
    return description  
    pass
