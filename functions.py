def year_range(df, yr_column_name):
    """
        Return the oldest and most recent year that a game was released.

        Parameters
        ----------
        df : pandas object
            dataFrame from which to pull the values.
        yr_column_name : string
            name of the column containing the "Year" values.

        Returns
        -------
        list
            [yr_min, yr_max].
    """
    yr_min = df[f"{yr_column_name}"].min() # Oldest released date for a game on this sytem
    yr_max = df[f"{yr_column_name}"].max() # Newest released date for a game on this system
    return [yr_min,yr_max]