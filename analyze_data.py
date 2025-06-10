import pandas as pd

def analyze_csv_data(orderlist_filepath, meta_filepath):
    """
    Reads and performs a basic analysis of OrderList.csv and meta.csv.

    Args:
        orderlist_filepath (str): The path to the OrderList.csv file.
        meta_filepath (str): The path to the meta.csv file.
    """
    print(f"--- Analyzing {orderlist_filepath} ---")
    try:
        # Read the OrderList.csv file into a pandas DataFrame
        order_list_df = pd.read_csv(orderlist_filepath)
        print("\nSuccessfully loaded OrderList.csv.")
        print("\nFirst 5 rows of OrderList.csv:")
        print(order_list_df.head())

        print("\nInformation about OrderList.csv:")
        order_list_df.info()

        print("\nDescriptive statistics for OrderList.csv:")
        print(order_list_df.describe(include='all')) # Include all columns for description
    except FileNotFoundError:
        print(f"Error: {orderlist_filepath} not found. Please ensure the file is in the correct directory.")
        return
    except Exception as e:
        print(f"An error occurred while reading {orderlist_filepath}: {e}")
        return

    print(f"\n--- Analyzing {meta_filepath} ---")
    try:
        # Read the meta.csv file into a pandas DataFrame
        meta_df = pd.read_csv(meta_filepath)
        print("\nSuccessfully loaded meta.csv.")
        print("\nFirst 5 rows of meta.csv:")
        print(meta_df.head())

        print("\nInformation about meta.csv:")
        meta_df.info()

        print("\nDescriptive statistics for meta.csv:")
        print(meta_df.describe(include='all')) # Include all columns for description
    except FileNotFoundError:
        print(f"Error: {meta_filepath} not found. Please ensure the file is in the correct directory.")
        return
    except Exception as e:
        print(f"An error occurred while reading {meta_filepath}: {e}")
        return

    print("\n--- Attempting to merge DataFrames (if common columns exist) ---")
    # Identify common columns that could be used for merging
    common_cols = list(set(order_list_df.columns) & set(meta_df.columns))

    if common_cols:
        print(f"\nCommon columns found: {common_cols}")
        # Assuming the first common column is a suitable key for merging
        # You might need to adjust 'how' and 'on' parameters based on your data's relationship
        try:
            # Attempt to merge on the first common column
            # For a more robust merge, you might need to inspect your data to find the exact join key
            merged_df = pd.merge(order_list_df, meta_df, on=common_cols[0], how='left')
            print(f"\nSuccessfully merged DataFrames on '{common_cols[0]}'.")
            print("\nFirst 5 rows of the merged DataFrame:")
            print(merged_df.head())
            print(f"\nShape of the merged DataFrame: {merged_df.shape}")
        except Exception as e:
            print(f"An error occurred during merging: {e}")
            print("Please check if the common column is suitable for merging and if data types match.")
    else:
        print("\nNo common columns found between OrderList.csv and meta.csv for a direct merge.")
        print("Manual inspection of column names may be required to find a suitable merge key.")

if __name__ == "__main__":
    # Define the file paths for your CSV files
    # Make sure these files are in the same directory as this script,
    # or provide the full path to the files.
    orderlist_file = "DBNZ_OECE_SQM Coverage_calculator.xlsx - OrderList.csv"
    meta_file = "DBNZ_OECE_SQM Coverage_calculator.xlsx - meta.csv"

    analyze_csv_data(orderlist_file, meta_file)

    print("\n--- Script finished ---")
    print("You can extend this script to perform more complex analysis, data cleaning, or visualizations.")
    print("Remember to install pandas if you haven't already: pip install pandas")
