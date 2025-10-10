
def main():
    from importlib import resources

    from activities import data

    paralympics_data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")
    print( paralympics_data_file_csv.exists())

if __name__ == "__main__":
    main()
