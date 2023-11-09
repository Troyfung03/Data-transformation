import pandas as pd
import numpy as np

data = pd.read_csv("hotel_bookings.csv")
# remove duplicate
data.drop_duplicates(inplace=True)

# Convert data to right format
data['reservation_status_date'] = pd.to_datetime(data['reservation_status_date'])

# Merge and drop column
# Arrival date
data['arrival_date_month'].replace(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],inplace=True)
data['arrival_date'] = pd.to_datetime(data['arrival_date_month'].astype(str) + '/' + data['arrival_date_day_of_month'].astype(str)+ '/' + data['arrival_date_year'].astype(str))

data.drop(['arrival_date_month', 'arrival_date_day_of_month', 'arrival_date_year'], axis=1)


# total nights
data['total_night'] = data['stays_in_weekend_nights'] + data['stays_in_week_nights']



print("...")
