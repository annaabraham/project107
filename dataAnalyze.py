import csv
import pandas as pd 
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
