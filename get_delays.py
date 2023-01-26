import psycopg2
import pandas as pd
from config import params
import numpy as np 

conn = psycopg2.connect(**params)

cursor = conn.cursor()
cursor.execute("SELECT * FROM real_flight WHERE cancelled = \'0\' and diverted = \'0\'")

rows = cursor.fetchall()
cursor.close()
conn.close()

# create dataframe 
df = pd.DataFrame(rows, columns=[desc.name for desc in cursor.description])

# clean datafrane -> drop NaN values 
cleaned_df = df.dropna(subset=['arr_del15','dep_del15']) # These columns did not contain NaN

# convert columns to INT type from STR 
df['arr_del15'] = df['arr_del15'].astype('int')
df['dep_del15'] = df['dep_del15'].astype('int')

# create 'delayed' columns if either 'dep_del15' or 'arr_del15' had a delay 
df['Delayed'] = np.where((df['dep_del15'] |df['arr_del15']), 1, 0)

# group by airlines & calulate average
df_delays = df.groupby('op_unique_carrier')['Delayed'].aggregate(['mean'])
df_delays.sort_values(by='mean',ascending = False, inplace = True)

# group by origin airports & calculate average
origin_delays = df.groupby('origin_airport_id')['Delayed'].aggregate(['mean'])
origin_delays.sort_values(by='mean',ascending = False, inplace = True)


