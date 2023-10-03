import pandas as pd
df = pd.read_csv('input1.csv')
def transform_date(date_str):
    year = date_str
    month = '01'
    day = '01'
    new_date = f"{year}-{month}-{day}"
    return new_date
df['year'] = df['year'].apply(transform_date)
df.to_csv('output1.csv', index=False)
