import pandas as pd

def toLatex(data):

    if '.csv' in data:
        filename = data
    else:
        filename = data + '.csv'

    df = pd.read_csv(filename)

    if '.csv' in data:
        data = data.replace('.csv', '.tex')
    else:
        data = data + '.tex'

    df.to_latex(data)
    print(df.to_latex())