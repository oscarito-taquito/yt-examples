import pandas as pd
import glob

files = glob.glob('../data/city*.csv')

print(files)

dfs = []

for f in files:
	df = pd.read_csv(f)
	print(df) # for preview
	dfs.append(df)

combined = pd.concat(dfs)

print(combined.head())
print(combined.tail())