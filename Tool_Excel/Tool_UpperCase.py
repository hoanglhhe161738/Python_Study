import pandas as pd
import numpy as np
import openpyxl as openpyxl
df = pd.read_excel('J:/python.xlsx')
df["Date"].fillna("2020-12-02 00:00:00",inplace=True)
df["Pulse"].fillna(146,inplace=True)
df["Maxpulse"].fillna(200,inplace=True)
df["Calories"].fillna(180,inplace=True)
print(df.to_string())
