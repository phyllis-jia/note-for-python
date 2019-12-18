# pandas
most of it is in import data and clean data

import pandas as pd

pd.DataFrame()(for empty intial just keep () empty)

for large data: chunk, pd.read_csv(filename, chunksize=n) ----- (create an iterable reader object) (can't use [], only can use next())

cars['cars_per_cap']: the **single bracket version** gives a **pandas series** (series has no column)
cars[['cars_per_cap']]: the **double bracket version** gives a **pandas DataFrame**

pd.to_datatime

pd.to_msgpack

pd.to_numeric

pd.to_pickle

pd.to_timedelta