import numpy as np
import pandas as pd
import functions as fn

df = pd.read_csv('Video_Games.csv') # reading the initial data and storing in a dataFrame

"""DATA CLEANING"""



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



"""DATA EXPlORATION"""
# print(df['Platform'].value_counts()) # Most games: DS > PS3 > Wii > X360 > PC > PSP > PS4 > XOne
ps4_yr_min, ps4_yr_max = fn.year_range(df_ps4,"Year_of_Release") # 2013-2017
xone_yr_min, xone_yr_max = fn.year_range(df_xone,"Year_of_Release") # 2013-2016
ps3_yr_min, ps3_yr_max = fn.year_range(df_ps3,"Year_of_Release") # 2006-2016
x360_yr_min, x360_yr_max = fn.year_range(df_x360,"Year_of_Release") # 2005-2016
wii_yr_min, wii_yr_max = fn.year_range(df_wii,"Year_of_Release") # 2006-2016
ds_yr_min, ds_yr_max = fn.year_range(df_ds,"Year_of_Release") #1985-2020 OR 2004-2016
psp_yr_min, psp_yr_max = fn.year_range(df_psp,"Year_of_Release") # 2004-2015
pc_yr_min, pc_yr_max = fn.year_range(df_pc,"Year_of_Release") # 1985-2016
# NOTE: Data Cleaning: PS4 (1 game from 2017), DS (1 game from 2020 & 1 game from 1985), PC (has an advantage based on year range for games released)

print(f"<>  Date range by system for games released:\n\
    PS4 'Year_of_Release' range from {ps4_yr_min} to {ps4_yr_max}.\n\
    Xbox One 'Year_of_Release' range from {xone_yr_min} to {xone_yr_max}.\n\
    PS3 'Year_of_Release' range from {ps3_yr_min} to {ps3_yr_max}.\n\
    Xbox 360 'Year_of_Release' range from {x360_yr_min} to {x360_yr_max}.\n\
    Wii 'Year_of_Release' range from {wii_yr_min} to {wii_yr_max}.\n\
    DS 'Year_of_Release' range from {ds_yr_min} to {ds_yr_max}.\n\
    PSP 'Year_of_Release' range from {psp_yr_min} to {psp_yr_max}.\n\
    PC 'Year_of_Release' range from {pc_yr_min} to {pc_yr_max}.\n"
)



"""DATA ANALYSIS"""
prc_min = df_ps4["Global_Sales"].min() # Lowest sales for a game on this sytem
prc_max = df_ps4["Global_Sales"].max() # Highest sales for a game on this system
prc_avg = df_ps4["Global_Sales"].mean().__round__(3) # Average sales for games on this system
prc_med = df_ps4["Global_Sales"].median() # Median sales for games on this sytem
prc_sum = df_ps4["Global_Sales"].sum().__round__(3) # Total sales for games on this system

best_sellers = [name for name in df_ps4.nlargest(5,"Global_Sales")["Name"]] # List of strings, top 5 best sellers

# genre_count = df_ps4["Genre"].value_counts().reset_index().values.tolist() # Count of games in each genre. Removed series, included in below dataFrame instead.
genre_by_count = df_ps4.groupby(["Genre"]).agg({"Genre":"count", "Global_Sales":["sum","mean","median","max","min"]}).round(3).sort_values(by=[("Genre","count")], inplace=False, ascending=False)
genre_by_sales = genre_by_count.sort_values(by=[("Global_Sales","mean")], inplace=False, ascending=False) # mean or median makes the most sense because count varies

# NOTE below is a print statement to help visualize the above data analysis.
# print(f"<>  PS4: # of games, date range, sales data, best sellers, & genre count:\n\
#     DataFrame has {df_ps4.shape[0]} rows/games and {df_ps4.shape[1]} columns.\n\
#     'Year_of_Release' range from {ps4_yr_min} to {ps4_yr_max}.\n\
#     'Global_Sales' (in millions) range from {prc_min} to {prc_max} with an average of {prc_avg} and median of {prc_med} and total of {prc_sum}.\n\
#     Best Sellers: {best_sellers}.\n\
#     Genre_Sales ordered by count [[genre, games_count, sales_sum, mean, median, max, min], [...]]:\n{genre_by_count.reset_index().values.tolist()}." # convert DataFrame to list of lists for each genre
# )
# Genre Count: {genre_count}.\n\ # removed series, included in dataFrame instead
# Genre_Sales ordered by count [[genre, games_count, sales_sum, mean, median, max, min], [...]]:\n{genre_by_sales.reset_index().values.tolist()} # convert DataFrame to list of lists for each genre

# # This creates a list of lists [[list,dtype],[],[]]
# # columns_list = [[column, df[f"{column}"].dtypes] for column in df.columns]
# print(f"-  The table includes the following columns:\n{df.dtypes}.\n")

# minn = df["Year_of_Release"].min()
# maxx = df["Year_of_Release"].max()
# print(f"-  Years tracked range from {minn} to {maxx}.\n")

# avg = df["Global_Sales"].mean().__round__(2)
# median = df["Global_Sales"].median().__round__(2)
# minn = df["Global_Sales"].min().__round__(2)
# maxx = df["Global_Sales"].max().__round__(2)
# print(f"-  Analysis of Global_Sales Amounts:\nAverage of ${avg}\nMedian of ${median}\nMinimum of ${minn}\nMaximum of ${maxx}\n")