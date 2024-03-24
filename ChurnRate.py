import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Trades per player
trades_per_player = data.groupby('player')['order_id'].nunique()

# Players with one trade
single_trade_players = trades_per_player[trades_per_player == 1]

# Churn rate
churn_rate = len(single_trade_players) / len(trades_per_player)

print(f"Churn-Rate: {churn_rate:.2%}")
