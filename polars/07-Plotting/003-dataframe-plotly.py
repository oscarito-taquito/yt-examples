import polars as pl
import plotly.graph_objs as go
import numpy as np

df = pl.read_csv(
    "https://raw.githubusercontent.com/oscarito-taquito/yt-examples/main/data/age_income.csv"
)


data = [
    go.Scatter(
        x=df["Age"],
        y=df["Income"],
        mode="markers",
        marker=dict(size=14, color="oldlace", symbol="circle", line={"width": 2}),
    )
]
layout = go.Layout(
    title="Scatter Plot",
    xaxis=dict(title=f"{df.columns[2]}"),
    yaxis=dict(title=f"{df.columns[3]}"),
)

fig = go.Figure(data=data, layout=layout)
fig.show()
