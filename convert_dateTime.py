import pandas as pd
from datetime import datetime

# read csv file
df = pd.read_csv('C:/../[raw csv file]')
print(df.head())

# convert column header that has date into '%Y-%m-%d %H:%M' format
print(df[column_header].head())
df[column_header] = pd.to_datetime(df.column_header, dayfirst=True)
newDate = df[column_header].dt.strftime('%Y-%m-%d %H:%M')

df[column_header].update(newDate)
print(df[column_header].head())

df.to_csv(r"C:/../[raw csv file]",
          index=None, header=True)
