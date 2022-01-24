from re import A
import numpy as np
import pandas as pd

"""CREATE SUBSETS"""
df = pd.read_csv('Video_Games.csv')
# print(df['Platform'].value_counts()) # Most games: DS > PS3 > Wii > X360 > PC > PSP > PS4 > XOne
df_ps4 = df.loc[df['Platform'] == 'PS4']
df_xone = df.loc[df['Platform'] == 'XOne']
df_ps3 = df.loc[df['Platform'] == 'PS3']
df_x360 = df.loc[df['Platform'] == 'X360']
df_wii = df.loc[df['Platform'] == 'Wii']
df_pc = df.loc[df['Platform'] == 'PC']
df_psp = df.loc[df['Platform'] == 'PSP']
df_ds = df.loc[df['Platform'] == 'DS']
del df

"""DATA EXPLORATION"""
yr_min = df_ps4["Year_of_Release"].min() # Oldest released date for a game on this sytem
yr_max = df_ps4["Year_of_Release"].max() # Newest released date for a game on this system
prc_min = df_ps4["Global_Sales"].min() # Lowest sales for a game on this sytem
prc_max = df_ps4["Global_Sales"].max() # Highest sales for a game on this system
prc_avg = df_ps4["Global_Sales"].mean().__round__(2) # Average sales for games on this system
prc_med = df_ps4["Global_Sales"].median() # Median sales for games on this sytem
prc_sum = df_ps4["Global_Sales"].sum().__round__(2) # Total sales for games on this system
best_sellers = [name for name in df_ps4.nlargest(5,'Global_Sales')['Name']] # List of strings, top 5 best sellers
genre_count = df_ps4['Genre'].value_counts().reset_index().values.tolist() # Count of games in each genre
print(f"<>  PS4: # of games, date range, sales data, best sellers, & genre count:\n\
    DataFrame has {df_ps4.shape[0]} rows/games and {df_ps4.shape[1]} columns.\n\
    'Year_of_Release' range from {yr_min} to {yr_max}.\n\
    'Global_Sales' (in millions) range from {prc_min} to {prc_max} with an average of {prc_avg} and median of {prc_med} and total of {prc_sum}.\n\
    Best Sellers: {best_sellers}\n\
    Genre Count: {genre_count}")

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