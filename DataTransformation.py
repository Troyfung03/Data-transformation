import pandas as pd
import numpy as np

data = pd.read_csv("hotel_bookings.csv")
# remove duplicate
data.drop_duplicates(inplace=True)

# Convert data to right format
data[''] = pd.to_datetime(data[''])