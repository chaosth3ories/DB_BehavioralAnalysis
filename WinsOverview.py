import pandas as pd


data = pd.read_csv('DBMaster.csv')

# Filter by Win-Trades
profit_trades = data[data['profit_loss'] > 0]

# Calculations
lowest_profit = profit_trades['profit_loss'].min()
highest_profit = profit_trades['profit_loss'].max()
median_profit = profit_trades['profit_loss'].median()
average_profit = profit_trades['profit_loss'].mean()

# Results
print(f"Lowest win: {lowest_profit} USD")
print(f"Highest Gewinn: {highest_profit} USD")
print(f"Median Win: {median_profit} USD")
print(f"Average Win: {average_profit} USD")
