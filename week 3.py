import pandas as pd
import numpy as np
import requests
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
response = requests.get(url)
data = StringIO(response.text)
df = pd.read_csv(data)

df = df.sort_values(by='hour_beginning')
df.reset_index(drop=True, inplace=True)
df['Date'] = pd.to_datetime(df['hour_beginning'])
# df.loc[df['events'].notnull()]
df['DayName'] = df['Date'].dt.day_name()

weekday_filter = df['DayName'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
date_filter = (df['Date'].dt.year != 2018) | ((df['Date'].dt.year == 2018) & ((df['Date'].dt.month < 8) | (df['Date'].dt.month > 12))) | ((df['Date'].dt.year == 2019) & (df['Date'].dt.month < 1))
df = df.loc[weekday_filter & date_filter]

df.reset_index(drop=True, inplace=True)
# df['temperature'] = df['temperature'].fillna(method='ffill')
# df['precipitation'] = df['precipitation'].fillna(method='ffill')
# df['Pedestrians'] = df['Pedestrians'].fillna(method='ffill')
# df['weather_summary'] = df['weather_summary'].fillna(method='ffill')

pedestrian_counts = df.groupby('Date')['Pedestrians'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=pedestrian_counts, x='Date', y='Pedestrians', marker='o')
plt.title('Pedestrian Counts for Each Day of the Week')
plt.xlabel('Date')
plt.ylabel('Pedestrian Counts')
plt.grid(True)
plt.show()

brooklyn_bridge_2019 = df.loc[(df['Date'].dt.year == 2019) & (df['location'] == 'Brooklyn Bridge')]

brooklyn_bridge_2019 = brooklyn_bridge_2019.dropna()  # Remove any remaining null or NaN values
weather_pedestrian_corr = brooklyn_bridge_2019.groupby('weather_summary')['Pedestrians'].mean().sort_values(ascending=False)

def categorize_time(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

df['Time of Day'] = df['Date'].dt.hour.apply(categorize_time)

pedestrian_activity = df.groupby('Time of Day')['Pedestrians'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=pedestrian_activity, x='Time of Day', y='Pedestrians')
plt.title('Average Pedestrian Counts by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Average Pedestrian Counts')
plt.grid(True)
plt.show()
