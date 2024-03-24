import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Filter data by losses
loss_trades = data[data['profit_loss'] < 0]

# Calculations
lowest_loss = loss_trades['profit_loss'].min()
highest_loss = loss_trades['profit_loss'].max()
median_loss = loss_trades['profit_loss'].median()
average_loss = loss_trades['profit_loss'].mean()

# Results
print(f"Lowest Loss: {lowest_loss} USD")
print(f"Highest Loss: {highest_loss} USD")
print(f"Median Loss: {median_loss} USD")
print(f"Average Loss: {average_loss} USD")
