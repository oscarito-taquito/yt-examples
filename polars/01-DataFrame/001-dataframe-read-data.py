import polars as pl
import csv
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import data.mydata as data

csv_file_path = data.files["age_income"]


df = pl.read_csv(csv_file_path)

print(df.head())
