import pandas as pd


data = pd.read_csv('DBMaster.csv')

# Avg and Median Profit Loss
average_profit_loss = data['profit_loss'].mean()

median_profit_loss = data['profit_loss'].median()

# Results
print(f"Average Profit/Loss per Trade: {average_profit_loss:.2f} USD")
print(f"Median Profit/Loss per Trade: {median_profit_loss:.2f} USD")
