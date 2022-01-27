# NOTE: this file was imported with the following statement -- import functions as fn
#       so to use functions in this file, they need to be preceded with fn. Ex: fn.year_range(df,'Year')

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
            genre_counts_asc = fn.counter(df, "Genre", ascending=True)
            genre_counts_desc = fn.counter(df, "Genre")
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