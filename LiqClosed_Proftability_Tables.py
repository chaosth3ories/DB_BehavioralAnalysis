import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Profitable trades
data['Profitable'] = data['profit_loss'] > 0

# Group data
status_profit_table = data.groupby(['position_status', 'Profitable']).size().unstack(fill_value=0)

# Change numbers in %
status_profit_percent_table = status_profit_table.div(status_profit_table.sum(axis=1), axis=0) * 100

# Tables
print("Absolute numbers (Closed and Liquidated Trades profitable vs. unprofitable):")
print(status_profit_table)
print("\n% (Closed and Liquidated Trades profitable vs. unprofitable):")
print(status_profit_percent_table.round(2))
