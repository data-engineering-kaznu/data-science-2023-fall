import pandas as pd
from datetime import datetime
df = pd.read_csv('input.csv')
def convert_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%b")
    return date_obj.strftime("%Y-%m-%d")
df['year'] = df['year'].apply(convert_date)
df.to_csv('output.csv', index=False)
