import csv
import pandas as pd
import plotly.graph_objects as go


df=pd.read_csv("data.csv")
df.to_csv('dataEach.csv',index=False)
studentId=df.loc[df["student_id"]=="TRL_987"]
print(studentId.groupby("level")["attempt"].mean())
fig=go.Figure(go.Scatter(
    x=studentId.groupby("level")["attempt"].mean(),
    y=['level1','level2','level3','level4']
    ))
fig.show()

