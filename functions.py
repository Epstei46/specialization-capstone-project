import traceback

def try_or(func, default=None, expected_exc=(Exception,)):
    """This is a method that allows me to reduce the amount of try-except needed in my code, with the except always returning the error."""
    
    # (1) I was searching online for ways to shorten the try-except, and then (2) searched for how to catch the line where an error occurred but continue running through the code after that.
    
    # SOURCE: (1) https://stackoverflow.com/a/56137232 & (2) https://stackoverflow.com/a/47659065
    
    try:
        return func()
    
    except expected_exc:
        print("--  RAN INTO AN ISSUE HERE! SEE THE ERROR BELOW:")
        print(traceback.format_exc())
        return default

def exploratory_info(df):
    """Using pandas to print basic information about your dataset such as number of rows, averages for numeric columns, and any other useful explanatory information about your dataset."""
    
    print(f"-  Table has {df.shape[0]} rows and {df.shape[1]} columns.\n")
    
    # This creates a list of lists [[list,dtype],[],[]]
    # columns_list = [[column, df[f"{column}"].dtypes] for column in df.columns]
    print(f"-  The table includes the following columns:\n{df.dtypes}.\n")
    
    minn = df["Year_of_Release"].min()
    maxx = df["Year_of_Release"].max()
    print(f"-  Years tracked range from {minn} to {maxx}.\n")
    

    
    # count = df["Community Focus: Disabled"].value_counts() #.fillna(False) if NaN values
    # true_counts = df[["Community Focus: African American","Community Focus: Asian American","Community Focus: Disabled","Community Focus: Immigrant","Community Focus: L/G/B/T/Q","Community Focus: Latino American","Community Focus: Multiple People of Color","Community Focus: Native","Community Focus: Native American","Community Focus: Pacific Islander","Community Focus: Transgender","Community Focus: Women","Community Focus: No specified focus"]].sum()
    # print(f"    Below is a list of the number of applicants with the specified Community Focus:\n{true_counts}\n")