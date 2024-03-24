import pandas as pd


df = pd.read_csv('DBMaster.csv')

# Total deposit per player
total_wagered_per_player = df.groupby('player')['_wagerAmount'].sum()

# Total net outcome per player
net_profit_loss_per_player = df.groupby('player')['profit_loss'].sum()

# Net loss per player
net_loss_per_player = net_profit_loss_per_player.clip(upper=0).abs()

# Percentage Loss per player
percentage_loss_per_player = (net_loss_per_player / total_wagered_per_player) * 100

percentage_loss_per_player = percentage_loss_per_player.clip(lower=0, upper=100)

# Average and Median
average_percentage_loss = percentage_loss_per_player.mean()
median_percentage_loss = percentage_loss_per_player.median()

# Results
print(f"Average percent loss per player: {average_percentage_loss}%")
print(f"Median percent loss per player: {median_percentage_loss}%")
