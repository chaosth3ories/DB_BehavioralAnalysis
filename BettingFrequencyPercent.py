import pandas as pd

df = pd.read_csv('DBMaster.csv')

# Change of date
df['open_date'] = pd.to_datetime(df['open_date']).dt.date

# Betting duration
df['betting_duration'] = df.groupby('player')['open_date'].transform(lambda x: (x.max() - x.min()).days + 1)

# Betting days per player
unique_betting_days_per_player = df.groupby('player')['open_date'].nunique()

# Frequency
daily_frequency_per_player = (unique_betting_days_per_player / df.groupby('player')['betting_duration'].first()) * 100

# Average and Median
average_daily_frequency = daily_frequency_per_player.mean()
median_daily_frequency = daily_frequency_per_player.median()

print(f"Average Frequency: {average_daily_frequency}%")
print(f"Median Frequency: {median_daily_frequency}%")

