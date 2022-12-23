import pandas as pd
## sample data
data = [
    ['bob', 'agriculture'], ['dinesh', 'agriculture'], ['jane', 'retail'],
    ['joe', 'aerospace'], ['mario', 'services'], ['mugdha', 'manufacturing'],
    ['josie', 'manufacturing'], ['oscar', 'agriculture'], ['mary', 'retail'],
    ['arnold', 'entertainment'], ['arnold', 'entertainment'], ['arnold', 'entertainment']
]

df = pd.DataFrame(data, columns=['name', 'industry'])
# print(df.head(15))

# # removes the 2 records for 'arnold'
# print(df.drop_duplicates())

# # removes all records for 'arnold' using False arg
# print(df.drop_duplicates(keep=False))

# # keep unique records based on industry
print(df.drop_duplicates(subset=['industry']))

