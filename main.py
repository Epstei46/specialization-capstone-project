import numpy as np
import pandas as pd
import functions as fn
import matplotlib.pyplot  as plt

df = pd.read_csv('Video_Games.csv') # reading the initial data and storing in a dataFrame

"""CREATE SUBSETS"""
df_ps4 = df.loc[df['Platform'] == 'PS4']
df_xone = df.loc[df['Platform'] == 'XOne']
df_ps3 = df.loc[df['Platform'] == 'PS3']
df_x360 = df.loc[df['Platform'] == 'X360']
df_wii = df.loc[df['Platform'] == 'Wii']
df_pc = df.loc[df['Platform'] == 'PC']
df_psp = df.loc[df['Platform'] == 'PSP']
df_ds = df.loc[df['Platform'] == 'DS']
del df



"""DATA CLEANING"""
fn.incomplete_check(df_ps4, clean=True)
fn.incomplete_check(df_xone, clean=True)



"""DATA EXPLORATION"""
# print(f"DataFrame df_ps4 has {df_ps4.shape[0]} rows/games and {df_ps4.shape[1]} columns.\n")

# This creates a list of lists [[list,dtype],[],[]]
columns_list = [[column, df_ps4[f"{column}"].dtypes] for column in df_ps4.columns]
# print(f"<>  The table includes the following [[columns, data_types], ...] ('O'==Object, likely a string):\n{columns_list}.\n")

genre_count = df_ps4["Genre"].value_counts().reset_index().values.tolist() # Ordered (DESC) count of games in each genre. Converted pandas.Series to list.
# print(f"Genre Count: {genre_count}.\n")

best_sellers = [name for name in df_ps4.nlargest(5,"Global_Sales")["Name"]] # List of strings, top 5 best sellers
# print(f"Best Sellers: {best_sellers}.\n")

# print(df['Platform'].value_counts()) # Most games: DS > PS3 > Wii > X360 > PC > PSP > PS4 > XOne



"""DATA ANALYSIS"""
ps4_yr_min, ps4_yr_max = fn.year_range(df_ps4,"Year_of_Release") # 2013-2017
xone_yr_min, xone_yr_max = fn.year_range(df_xone,"Year_of_Release") # 2013-2016
ps3_yr_min, ps3_yr_max = fn.year_range(df_ps3,"Year_of_Release") # 2006-2016
x360_yr_min, x360_yr_max = fn.year_range(df_x360,"Year_of_Release") # 2005-2016
wii_yr_min, wii_yr_max = fn.year_range(df_wii,"Year_of_Release") # 2006-2016
ds_yr_min, ds_yr_max = fn.year_range(df_ds,"Year_of_Release") #1985-2020 OR 2004-2016
psp_yr_min, psp_yr_max = fn.year_range(df_psp,"Year_of_Release") # 2004-2015
pc_yr_min, pc_yr_max = fn.year_range(df_pc,"Year_of_Release") # 1985-2016
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

ps4_genre_counts = fn.counter(df_ps4, "Genre")
xone_genre_counts = fn.counter(df_xone, "Genre")
ps3_genre_counts = fn.counter(df_ps3, "Genre")
x360_genre_counts = fn.counter(df_x360, "Genre")
wii_genre_counts = fn.counter(df_wii, "Genre")
ds_genre_counts = fn.counter(df_ds, "Genre")
psp_genre_counts = fn.counter(df_psp, "Genre")
pc_genre_counts = fn.counter(df_pc, "Genre")
# NOTE: Xbox One only has 253 games and PS4 has 400 games. All other systems have ~1000 or more games.
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

ps4_sum, ps4_min, ps4_max, ps4_avg, ps4_med, ps4_mode = fn.aggregator(df_ps4, "Global_Sales")
xone_sum, xone_min, xone_max, xone_avg, xone_med, xone_mode = fn.aggregator(df_xone, "Global_Sales")
ps3_sum, ps3_min, ps3_max, ps3_avg, ps3_med, ps3_mode = fn.aggregator(df_ps3, "Global_Sales")
x360_sum, x360_min, x360_max, x360_avg, x360_med, x360_mode = fn.aggregator(df_x360, "Global_Sales")
wii_sum, wii_min, wii_max, wii_avg, wii_med, wii_mode = fn.aggregator(df_wii, "Global_Sales")
ds_sum, ds_min, ds_max, ds_avg, ds_med, ds_mode = fn.aggregator(df_ds, "Global_Sales")
psp_sum, psp_min, psp_max, psp_avg, psp_med, psp_mode = fn.aggregator(df_psp, "Global_Sales")
pc_sum, pc_min, pc_max, pc_avg, pc_med, pc_mode = fn.aggregator(df_pc, "Global_Sales")
# NOTE  Total Sales for PS4, PC, PSP around #300m; Xbox One total sales at $162m.
#       Total Sales for PS3, Xbox 360, Wii, DS closer oto 900m
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
# print(f"Genre_Sales ordered by count [[genre, games_count, sales_sum, mean, median, max, min], [...]]:\n{genre_by_sales.reset_index().values.tolist()}.") # convert DataFrame to list of lists for each genre



"""CREATING CHARTS"""
w = 0.2 # width
x = ["A", "B", "C"] # labels for each set of grouped bars (x1 & x2)
x1 = [1,2,3] # values for each column label in 1st set of grouped bars
x2 = [0.75,1.5,2] # values for each column label in 2nd set of grouped bars

bar1 = np.arange(len(x)) # [0,1,2] because length of x is 3
bar2 = [i+w for i in bar1] # moves each bar over so adjacent with bar1
# bar3 = [i+w for i in bar2] # moves each bar over so adjacent with bar2

plt.bar(bar1,x1,w,label="x1") # number of bars, height from values, width, bar label used in legend
plt.bar(bar2,x2,w,label="x2") # number of bars, height from values, width, bar label used in legend

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Y-Axis vs X-Axis")
plt.xticks(bar1+w/2,x) # change tick labels from numeric (e.g. 0,1,2) to match labels in list object x AND move ticks to be between both bars
plt.legend() # generates legend for x1 x2
# plt.show()