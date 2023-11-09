import pandas as pd

data = pd.read_csv("hotel_bookings.csv")
print('\nBefore')
data.info()
# 1. remove duplicate
data.drop_duplicates(inplace=True)

# 2. Fill na, replace value and Convert data to right format
data['reservation_status_date'] = pd.to_datetime(data['reservation_status_date'])
l = ['children', 'agent', 'adr', 'company']
for c in l:
    data[c] = data[c].fillna(0)
    if (data[c].astype(int) == data[c]).all():
        data[c] = data[c].astype(int)

data['country'] = data['country'].fillna('NC')

print(data['reservation_status'].unique())
# Set Check-Out to 0, Canceled to 1, No-Show to 2
s = data['reservation_status'].unique()
for i in range(3):
    data.loc[data['reservation_status'] == s[i], 'reservation_status'] = i
data['reservation_status'] = data['reservation_status'].astype(int)


# 3. Merge and drop column
# Arrival date
data['arrival_date_month'].replace(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], inplace=True)

data['arrival_date'] = pd.to_datetime(data['arrival_date_month'].astype(str) + '/' +
                                      data['arrival_date_day_of_month'].astype(str) + '/' + data['arrival_date_year'].astype(str))

data.drop(['arrival_date_month', 'arrival_date_day_of_month', 'arrival_date_year'], axis=1, inplace=True)

# total nights
data['total_nights'] = data['stays_in_weekend_nights'] + data['stays_in_week_nights']

# Family members
data['family_members'] = data['adults'] + data['children'] + data['babies']

# total number of previous bookings
data['previous_bookings'] = data['previous_cancellations'] + data['previous_bookings_not_canceled']

print('\nAfter')
data.info()
