import pandas as pd

data = [
    ['bob', 'agriculture'], ['dinesh', 'agriculture'], ['jane', 'retail'],
    ['joe', 'aerospace'], ['mario', 'services'], ['mugdha', 'manufacturing'],
    ['josie', 'manufacturing'], ['oscar', 'agriculture'], ['mary', 'retail'],
    ['arnold', 'entertainment'], ['arnold', 'entertainment'], ['arnold', 'entertainment']
]

idx = [i for i in range(0, 24, 2)]
df = pd.DataFrame(data, columns=['name', 'industry'], index=idx)
print(df)
