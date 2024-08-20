import polars as pl
import plotly.graph_objs as go
import random


df = pl.read_csv(
    "https://raw.githubusercontent.com/oscarito-taquito/yt-examples/main/data/age_income.csv"
)

# get average income by age
df = df.group_by("Age").agg(pl.col("Income").mean().alias("Income"))
df = df.with_columns((pl.col("Income") * random.random()).alias("Adjusted Income"))

df = df.sort("Age")


trace = go.Scatter(
    x=df["Age"],
    y=df["Income"],
    mode="lines",
    name="Average Income",
)
trace2 = go.Scatter(
    x=df["Age"],
    y=df["Adjusted Income"] * random.random(),
    mode="lines",
    name="Adjusted Income",
    marker=dict(size=14, color="green", line={"width": 2}),
)

data = [trace, trace2]
layout = go.Layout(
    title="Average Income by Age",
    xaxis=dict(title=f"{df.columns[0]}"),
    yaxis=dict(title=f"{df.columns[1]}"),
)

fig = go.Figure(data=data, layout=layout)
fig.show()
