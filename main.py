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
# print(f"-  Table has {df.shape[0]} rows and {df.shape[1]} columns.\n")

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