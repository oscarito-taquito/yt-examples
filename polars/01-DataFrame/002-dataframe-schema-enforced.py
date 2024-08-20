import polars as pl
import csv
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import data.mydata as data

schema = {
    "name": pl.String,
    "marital_status": pl.String,
    "age": pl.Int64,
    "income": pl.String,
}

csv_file_path = data.files["age_income"]

data = []

with open(csv_file_path, mode="r") as file:
    # skip the header
    next(file)
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

df = pl.DataFrame(data, schema=schema, orient="row")

print(df.head())
