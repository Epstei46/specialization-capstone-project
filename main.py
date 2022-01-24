from re import A
import numpy as np
import pandas as pd
import functions as fn

df = pd.read_csv('Video_Games.csv')

"""DATA EXPLORATION"""
fn.try_or(lambda: fn.exploratory_info(df))
try:
    pass
    avg = df["Global_Sales"].mean().__round__(2)
    median = df["Global_Sales"].median().__round__(2)
    minn = df["Global_Sales"].min().__round__(2)
    maxx = df["Global_Sales"].max().__round__(2)
    print(f"-  Analysis of Global_Sales Amounts:\nAverage of ${avg}\nMedian of ${median}\nMinimum of ${minn}\nMaximum of ${maxx}\n")
except:
    pass