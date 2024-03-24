import pandas as pd


df = pd.read_csv('DBMaster.csv')

# Average deposit per player per trade
mean_bet_size_per_player = df.groupby('player')['_wagerAmount'].mean()

# Average and Median
average_mean_bet_size = mean_bet_size_per_player.mean()
median_mean_bet_size = mean_bet_size_per_player.median()

# Results
print(f"Average bet per player per trade: {average_mean_bet_size}")
print(f"Median bet per player per trade: {median_mean_bet_size}")
