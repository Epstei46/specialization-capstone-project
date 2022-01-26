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
        list
            [yr_min, yr_max]
        
        Usage / Example
        ---------------
            ps4_yr_min, ps4_yr_max = fn.year_range(df_ps4,"Year_of_Release")
    """
    yr_min = df[f"{yr_column_name}"].min() # Oldest released date for a game on this sytem
    yr_max = df[f"{yr_column_name}"].max() # Newest released date for a game on this system
    return [yr_min, yr_max]

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
        list
            [summ, minn, maxx, avg, med, mode]
        
        Usage / Example
        ---------------
            ps4_sum, ps4_min, ps4_max, ps4_avg, ps4_med, ps4_mode = aggregator(df_ps4, "Global_Sales")
    """
    summ = df[column].sum().__round__(3) # Total sales for games on this system
    minn = df[column].min() # Lowest sales for a game on this sytem
    maxx = df[column].max() # Highest sales for a game on this system
    avg = df[column].mean().__round__(3) # Average sales for games on this system
    med = df[column].median() # Median sales for games on this sytem
    mode = df[column].mode() # Most repeated value for games sales on this system
    return [summ, minn, maxx, avg, med, mode]