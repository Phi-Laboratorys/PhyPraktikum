import pandas as pd

data = ''

if '.csv' in data:
    filename = data
else:
    filename = data + '.csv'

print(filename)
df = pd.read_csv(filename)

if '.csv' in data:
    data = data.replace('.csv', '.tex')
else:
    data = data + '.tex'

df.to_latex(data)
print(df.to_latex())