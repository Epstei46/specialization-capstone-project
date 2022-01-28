# NOTE: this file was imported with the following statement -- import functions as fn
#       so to use functions in this file, they need to be preceded with fn. Ex: fn.year_range(df,'Year')

import numpy as np
import pandas as pd

def year_range(df, yr_column_name):
    """
    Return the oldest and most recent year (yr) that a game was released
    
    Parameters
    ----------
    df : pandas object
        dataFrame from which to pull the values
    yr_column_name : string
        name of the column containing the "Year" values
    
    Returns
    -------
    list of floats
        [yr_min, yr_max]
    
    Usage / Example
    ---------------
    ps4_yr_min, ps4_yr_max = fn.year_range(df_ps4,"Year_of_Release")
    """
    yr_min = df[f"{yr_column_name}"].min() # Oldest released date for a game on this sytem
    yr_max = df[f"{yr_column_name}"].max() # Newest released date for a game on this system
    return [yr_min, yr_max]

def counter(df, column, ascending = False, total = True):
    """
    Return a list of lists ordered by the total count of each unique value in the column.
    
    Parameters
    ----------
    df : pandas object
        dataFrame from which to pull the values
    column : string
        column to focus on for looking for values
    ascending : bool, default False
        Order by Descending if False (default), Ascending if True
    total : bool, default True
        if True, insert ["Total_Count", integer] to the beginning of the list of lists

    Returns
    -------
    list of lists
        e.g. [[unique_value, integer_count], [unique_value, integer_count], etc]
    
    Usage / Example
    ---------------
    genre_counts_asc = fn.counter(df, "Genre", ascending=True)\ngenre_counts_desc = fn.counter(df, "Genre")
    """
    count_series = df[f"{column}"].value_counts()
    if ascending == False:
        count_list = count_series.reset_index().values.tolist()
    else:
        count_series.sort_values(inplace=True, ascending=True)
        count_list = count_series.reset_index().values.tolist()
    if total == True:
        count_list.insert(0,["Total_Count", df.shape[0]])
    else:
        pass
    return count_list

def aggregator(df, column):
    """
    Return multiple aggregate data values, compiled into a list. summ (total), minn (lowest value), maxx (highest value), avg (mean), med (median), mode (most repeated value).
    
    Parameters
    ----------
    df : pandas object
        dataFrame from which to pull the values
    column : string
        column to focus on for creating the aggregate data
    
    Returns
    -------
    list of floats
        [summ, minn, maxx, avg, med, mode]
    
    Usage / Example
    ---------------
    ps4_sum, _, ps4_max, ps4_avg, _, ps4_mode = aggregator(df_ps4, "Global_Sales")
        NOTE : values you don't want saved to an object, like min/med in above examples, were ignored by using the underscore character instead of an object name.
    """
    summ = df[column].sum().__round__(3) # Total sales for games on this system
    minn = df[column].min() # Lowest sales for a game on this sytem
    maxx = df[column].max() # Highest sales for a game on this system
    avg = df[column].mean().__round__(3) # Average sales for games on this system
    med = df[column].median() # Median sales for games on this sytem
    mode = df[column].mode() # Most repeated value for games sales on this system
    return [summ, minn, maxx, avg, med, mode]

def incomplete_check(df, clean=False, output=True):
    """
    This function checks for the following values, by column, in each cell: None, NaN, NaT, numpy.NaN, '', numpy.inf. if nulls > 0 in a column, then it will print a statement with the name of the column and number of nulls.
    
    if clean=True and the column did not have too many null values, they are replaced with a meaninful value or returned in a list of every column where there were unhandled null values. If the column was mostly null values, it is removed from the dataFrame (df).
    
    Parameters
    ----------
    df : pandas object
            dataFrame from which to pull the values
    clean : bool, default False
            if False, do not change the data. if True, try to clean the data.
    output : bool, default True
        if True, output info to Terminal. if False, no output to Terminal.
    
    Returns
    -------
    None
    
    Usage / Example
    ---------------
    fn.incomplete_check(df_ps4, clean=True, output=False)\nfn.incomplete_check(df_ps4)
    """
    bad_list = []
    removed_list = []
    
    pd.options.mode.use_inf_as_na = True
    column_names = list(df.columns)
    
    for column in column_names:
        nulls = df[f"{column}"].isnull().sum()
        if output == True and nulls > 0:
            print(f"The column '{column}' has {nulls} nulls in it. The data type is {df[f'{column}'].dtype}.")
    
    if clean == True:
        orgnl_rows, orgnl_columns = df.shape
        
        for column in column_names:
            nulls = df[f"{column}"].isnull().sum()
            if nulls > 0:
                dtype = df[f'{column}'].dtype
                if nulls > df.shape[0]/2:
                    # print(f"The table has {df.shape[0]} rows. Because most of the values in this column have a null value, {column} has been dropped from the table.")
                    removed_list.append(f"{column}")
                    df.drop(f"{column}", axis=1, inplace=True)
                elif dtype == 'bool':
                    df[f'{column}'] = df[f'{column}'].fillna(False, inplace=True)
                elif dtype == 'float64':
                    df[f'{column}'] = df[f'{column}'].fillna(np.nan, inplace=True)
                else:
                    bad_list.append(f"{column}")
        if output == True and len(bad_list) > 0:
            new_rows, new_columns = df.shape
            print(f"<>  Before cleaning, table had {orgnl_rows} rows {orgnl_columns} columns.\n\
    After cleaning, it now has {new_rows} rows {new_columns} columns.\n\
    The following columns were removed from the table because most values were NaN: {removed_list}.\n\
    The following columns had dtype=='object', which may be because there were strings, so values were left unchanged, :\n        {bad_list}.")
    print("") # spacer