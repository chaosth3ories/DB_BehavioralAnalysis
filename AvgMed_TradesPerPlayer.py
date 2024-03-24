import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Trades per player
trades_per_player = data.groupby('player').size()

# Average Trades per player
average_trades_per_player = trades_per_player.mean()

# Median Trades per player
median_trades_per_player = trades_per_player.median()

# Results
print(f"Average Amount of Trades per player: {average_trades_per_player:.2f}")
print(f"Median Amount of Trades per player: {median_trades_per_player:.2f}")
