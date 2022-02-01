import numpy as np
import pandas as pd
import functions as fn

df = pd.read_csv('Video_Games.csv') # reading the initial data and storing in a dataFrame

# below line is removing the following columns: 4 Publisher, 6 EU_Sales, 7 JP_Sales, 8 Other_Sales, 10 Critic_Score, 11 Critic_Count, 12 User_Score, 13 User_Count, 14 Developer, 15 Rating
# This can be modified to keep some of those columns or commented out to keep all
df.drop(df.columns[[4,6,7,8,10,11,12,13,14,15]], axis=1, inplace=True)
# the following columns will be kept: Name, Platform, Year_of_Release, Genre, NA_Sales, Global_Sales


"""CREATE SUBSETS"""
# all below lines are selecting rows where the value in the specified column is == to specified value
df_ps4 = df.loc[df['Platform'] == 'PS4']
df_xone = df.loc[df['Platform'] == 'XOne']
df_ps3 = df.loc[df['Platform'] == 'PS3']
df_x360 = df.loc[df['Platform'] == 'X360']
df_wii = df.loc[df['Platform'] == 'Wii']
df_pc = df.loc[df['Platform'] == 'PC']
df_psp = df.loc[df['Platform'] == 'PSP']
df_ds = df.loc[df['Platform'] == 'DS']
del df # deleting original dataFrame because it is no longer needed



"""DATA CLEANING"""
# Below function checks for empty values. Can output info and be modified for cleaning
# Currently only set up to clean columns with dtype of 'bool' or 'float64'.
fn.try_or(lambda: fn.incomplete_check(df_ps4, clean=True, output=False))
fn.try_or(lambda: fn.incomplete_check(df_xone, clean=True, output=False))

df_ps4.drop(df_ps4.loc[df_ps4['Year_of_Release']==2017].index, inplace=True) # drop 1 row with 2017 game
df_ds.drop(df_ds.loc[df_ds['Year_of_Release']==1985].index, inplace=True) # drop 1 row with 1985 game
df_ds.drop(df_ds.loc[df_ds['Year_of_Release']==2020].index, inplace=True) # drop 1 row with 2020 game



"""DATA EXPLORATION"""
# print(f"DataFrame df_ps4 has {df_ps4.shape[0]} rows/games and {df_ps4.shape[1]} columns.\n")

# This creates a list of lists [[list,dtype],[],[]]
columns_list = [[column, df_ps4[f"{column}"].dtypes] for column in df_ps4.columns]
# print(f"<>  The table includes the following [[columns, data_types], ...] ('O'==Object, likely a string):\n{columns_list}.\n")

genre_count = df_ps4["Genre"].value_counts().reset_index().values.tolist() # Ordered (DESC) count of games in each genre. Converted pandas.Series to list
# print(f"Genre Count: {genre_count}.\n")

best_sellers = [name for name in df_ps4.nlargest(5,"Global_Sales")["Name"]] # List of strings, top 5 best sellers
# print(f"Best Sellers: {best_sellers}.\n")

# print(df['Platform'].value_counts()) # Most games: DS > PS3 > Wii > X360 > PC > PSP > PS4 > XOne



"""DATA WRANGLING"""
ps4_yr_min, ps4_yr_max = fn.try_or(lambda: fn.year_range(df_ps4,"Year_of_Release")) # 2013-2017
xone_yr_min, xone_yr_max = fn.try_or(lambda: fn.year_range(df_xone,"Year_of_Release")) # 2013-2016
ps3_yr_min, ps3_yr_max = fn.try_or(lambda: fn.year_range(df_ps3,"Year_of_Release")) # 2006-2016
x360_yr_min, x360_yr_max = fn.try_or(lambda: fn.year_range(df_x360,"Year_of_Release")) # 2005-2016
wii_yr_min, wii_yr_max = fn.try_or(lambda: fn.year_range(df_wii,"Year_of_Release")) # 2006-2016
ds_yr_min, ds_yr_max = fn.try_or(lambda: fn.year_range(df_ds,"Year_of_Release")) #1985-2020 OR 2004-2016
psp_yr_min, psp_yr_max = fn.try_or(lambda: fn.year_range(df_psp,"Year_of_Release")) # 2004-2015
pc_yr_min, pc_yr_max = fn.try_or(lambda: fn.year_range(df_pc,"Year_of_Release")) # 1985-2016
# NOTE: Data Cleaning: PS4 (1 game from 2017), DS (1 game from 2020 & 1 game from 1985), PC (has an advantage based on year range for games released)
year_comparisons = f"<>  Date range by system for games released:\n\
    PS4 'Year_of_Release' range from {ps4_yr_min} to {ps4_yr_max}.\n\
    Xbox One 'Year_of_Release' range from {xone_yr_min} to {xone_yr_max}.\n\
    PS3 'Year_of_Release' range from {ps3_yr_min} to {ps3_yr_max}.\n\
    Xbox 360 'Year_of_Release' range from {x360_yr_min} to {x360_yr_max}.\n\
    Wii 'Year_of_Release' range from {wii_yr_min} to {wii_yr_max}.\n\
    DS 'Year_of_Release' range from {ds_yr_min} to {ds_yr_max}.\n\
    PSP 'Year_of_Release' range from {psp_yr_min} to {psp_yr_max}.\n\
    PC 'Year_of_Release' range from {pc_yr_min} to {pc_yr_max}.\n"
# print(year_comparisons)

ps4_genre_counts = fn.try_or(lambda: fn.counter(df_ps4, "Genre"))
xone_genre_counts = fn.try_or(lambda: fn.counter(df_xone, "Genre"))
ps3_genre_counts = fn.try_or(lambda: fn.counter(df_ps3, "Genre"))
x360_genre_counts = fn.try_or(lambda: fn.counter(df_x360, "Genre"))
wii_genre_counts = fn.try_or(lambda: fn.counter(df_wii, "Genre"))
ds_genre_counts = fn.try_or(lambda: fn.counter(df_ds, "Genre"))
psp_genre_counts = fn.try_or(lambda: fn.counter(df_psp, "Genre"))
pc_genre_counts = fn.try_or(lambda: fn.counter(df_pc, "Genre"))
# NOTE: Xbox One only has 253 games and PS4 has 400 games. All other systems have ~1000 or more games
genre_count_comparisons = f"<>  Genre count by console, most to least:\n\
    PS4 genre counts: {ps4_genre_counts}.\n\
    Xbox One genre counts: {xone_genre_counts}.\n\
    PS3 genre counts: {ps3_genre_counts}.\n\
    Xbox 360 genre counts: {x360_genre_counts}.\n\
    Wii genre counts: {wii_genre_counts}.\n\
    DS genre counts: {ds_genre_counts}.\n\
    PSP genre counts: {psp_genre_counts}.\n\
    PC genre counts: {pc_genre_counts}\n"
# print(genre_count_comparisons)



"""DATA ANALYSIS"""
ps4_sum, ps4_min, ps4_max, ps4_avg, ps4_med, ps4_mode = fn.try_or(lambda: fn.aggregator(df_ps4, "Global_Sales"))
xone_sum, xone_min, xone_max, xone_avg, xone_med, xone_mode = fn.try_or(lambda: fn.aggregator(df_xone, "Global_Sales"))
ps3_sum, ps3_min, ps3_max, ps3_avg, ps3_med, ps3_mode = fn.try_or(lambda: fn.aggregator(df_ps3, "Global_Sales"))
x360_sum, x360_min, x360_max, x360_avg, x360_med, x360_mode = fn.try_or(lambda: fn.aggregator(df_x360, "Global_Sales"))
wii_sum, wii_min, wii_max, wii_avg, wii_med, wii_mode = fn.try_or(lambda: fn.aggregator(df_wii, "Global_Sales"))
ds_sum, ds_min, ds_max, ds_avg, ds_med, ds_mode = fn.try_or(lambda: fn.aggregator(df_ds, "Global_Sales"))
psp_sum, psp_min, psp_max, psp_avg, psp_med, psp_mode = fn.try_or(lambda: fn.aggregator(df_psp, "Global_Sales"))
pc_sum, pc_min, pc_max, pc_avg, pc_med, pc_mode = fn.try_or(lambda: fn.aggregator(df_pc, "Global_Sales"))
# NOTE  Total Sales for PS4, PC, PSP around $300m; Xbox One total sales at $162m.
#       Total Sales for PS3, Xbox 360, Wii, DS closer ot $900m
aggregate_comparisons = f"<>  Aggregates by system for games sold ($ in millions):\n\
    PS4: Total Sales ${ps4_sum} | Lowest Value ${ps4_min} | Highest Value ${ps4_max} | Average ${ps4_avg} | Median ${ps4_med} | Mode ${ps4_mode.loc[0]}.\n\
    Xbox One: Total Sales ${xone_sum} | Lowest Value ${xone_min} | Highest Value ${xone_max} | Average ${xone_avg} | Median ${xone_med} | Mode ${xone_mode.loc[0]}.\n\
    PS3: Total Sales ${ps3_sum} | Lowest Value ${ps3_min} | Highest Value ${ps3_max} | Average ${ps3_avg} | Median ${ps3_med} | Mode ${ps3_mode.loc[0]}.\n\
    Xbox 360: Total Sales ${x360_sum} | Lowest Value ${x360_min} | Highest Value ${x360_max} | Average ${x360_avg} | Median ${x360_med} | Mode ${x360_mode.loc[0]}.\n\
    Wii: Total Sales ${wii_sum} | Lowest Value ${wii_min} | Highest Value ${wii_max} | Average ${wii_avg} | Median ${wii_med} | Mode ${wii_mode.loc[0]}.\n\
    DS: Total Sales ${ds_sum} | Lowest Value ${ds_min} | Highest Value ${ds_max} | Average ${ds_avg} | Median ${ds_med} | Mode ${ds_mode.loc[0]}.\n\
    PSP: Total Sales ${psp_sum} | Lowest Value ${psp_min} | Highest Value ${psp_max} | Average ${psp_avg} | Median ${psp_med} | Mode ${psp_mode.loc[0]}.\n\
    PC: Total Sales ${pc_sum} | Lowest Value ${pc_min} | Highest Value ${pc_max} | Average ${pc_avg} | Median ${pc_med} | Mode ${pc_mode.loc[0]}.\n"
# print(aggregate_comparisons)

genre_by_count = df_ps4.groupby(["Genre"]).agg({"Genre":"count", "Global_Sales":["sum","mean","median","max","min"]}).round(3).sort_values(by=[("Genre","count")], inplace=False, ascending=False)
# print(f"Genre_Sales ordered by count [[genre, games_count, sales_sum, mean, median, max, min], [...]]:\n{genre_by_count.reset_index().values.tolist()}.") # convert DataFrame to list of lists for each genre
genre_by_sales = genre_by_count.sort_values(by=[("Global_Sales","mean")], inplace=False, ascending=False) # mean or median makes the most sense because count varies
# print(f"Genre_Sales ordered by mean sales [[genre, games_count, sales_sum, mean, median, max, min], [...]]:\n{genre_by_sales.reset_index().values.tolist()}.") # convert DataFrame to list of lists for each genre

# below converts ps4_genre_counts & xone_genre_counts to a percentage of total games, compared by printing both.
ps4_genre_counts_pct = [[list[0],round(list[1]/398*100,2)] for list in ps4_genre_counts]
xone_genre_counts_pct = [[list[0],round(list[1]/253*100,2)] for list in xone_genre_counts]
# print(ps4_genre_counts_pct); print(""); print(xone_genre_counts_pct)



"""CREATING CHARTS"""
# Below fn.plotter() function creates a chart showing Xbox One vs PS4, % of Total Games by Genre. 
top_genres = ["Action", "Role Playing", "Sports", "Shooter", "Adventure", "Fighting"] # labels for each set of grouped bars (on x-axis)
PS4 = [36.43,13.32,11.81,10.55,7.04,4.52] # values for 1st bar in each set of grouped bars
Xbox_One = [35.18,5.53,15.02,15.42,5.53,2.77] # values for 2nd bar in each set of grouped bars
# fn.try_or(lambda: fn.plotter(top_genres, PS4, Xbox_One, "PS4", "Xbox One", "Genres", "% of Total Games", "Xbox One vs PS4, % of Total Games by Genre"))

# Below fn.plotter() function creates a chart showing Xbox One vs PS4, # of Games by Genre. 
PS4 = [145,53,47,42,28,18] # values for 1st bar in each set of grouped bars
Xbox_One = [89,14,38,39,14,7] # values for 2nd bar in each set of grouped bars
# fn.try_or(lambda: fn.plotter(top_genres, PS4, Xbox_One, "PS4", "Xbox One", "Genres", "# of Total Games", "Xbox One vs PS4, # of Games by Genre"))

# Below fn.plotter() function creates a chart showing Xbox One vs PS4, Total Sales by Genre.
top_genres = ["Shooter", "Sports", "Role Playing", "Action", "Racing", "Platform", "Fighting"] 
PS4 = [89.17,56.23,36.67,96.8,12.16,7.7,8.65] # values for 1st bar in each set of grouped bars
Xbox_One = [61.03,26.77,10.55,38.6,10.43,0.94,2.41] # values for 2nd bar in each set of grouped bars
# fn.try_or(lambda: fn.plotter(top_genres, PS4, Xbox_One, "PS4", "Xbox One", "Genres", "Total Sales (in millions)", "Xbox One vs PS4, Total Sales by Genre"))

# Below fn.plotter() function creates a chart showing Xbox One vs PS4, Mean Sales by Genre.
top_genres = ["Shooter", "Sports", "Role Playing", "Action", "Racing", "Platform", "Fighting"] 
PS4 = [2.123,1.196,0.692,0.668,0.64,0.642,0.481] # values for 1st bar in each set of grouped bars
Xbox_One = [1.565,0.704,0.754,0.434,0.497,0.188,0.344] # values for 2nd bar in each set of grouped bars
# fn.try_or(lambda: fn.plotter(top_genres, PS4, Xbox_One, "PS4", "Xbox One", "Genres", "Mean Sales (in millions)", "Xbox One vs PS4, Mean Sales by Genre"))