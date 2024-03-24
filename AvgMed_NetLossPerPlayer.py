import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('DBMaster.csv')

# Net loss per trade
df['net_loss'] = df['profit_loss'] - df['_wagerAmount']

# Data aggregation
net_loss_per_player = df.groupby('player')['net_loss'].sum()

# Average and Median per player
avg_net_loss = net_loss_per_player.mean()
median_net_loss = net_loss_per_player.median()

# Results
print(f"Average Net loss per player: {avg_net_loss}")
print(f"Median Net loss per player: {median_net_loss}")
