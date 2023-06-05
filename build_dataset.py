import pandas as pd
import time
from pathlib import Path
import os

# creates a CSV file from a list of dicts
# first converts to a dataframe.
# naming convention is by outletID and timestamp
def buildDataSet(lst, title):
	time_stamp = time.time()
	file_name = title + "_" + str(time_stamp) + ".csv"
	outlet_df = pd.DataFrame.from_dict(lst)
	outlet_df.to_csv(file_name, header=False, index=False)


