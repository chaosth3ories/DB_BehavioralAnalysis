import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('DBMaster.csv')

# Change of date
df['open_date'] = pd.to_datetime(df['open_date'])

df['hour_of_day'] = df['open_date'].dt.hour

# Trades per hour
trades_per_hour = df.groupby('hour_of_day').size()

# Bet size per hour
average_wager_per_hour = df.groupby('hour_of_day')['_wagerAmount'].mean()

# Plot
fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('Hours')
ax1.set_ylabel('Amount of Trades', color=color)
ax1.bar(trades_per_hour.index, trades_per_hour, color=color, alpha=0.6, label='Amount of Trades')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Average Betting Size in USD', color=color)
ax2.plot(average_wager_per_hour.index, average_wager_per_hour, color=color, marker='o', linestyle='-', linewidth=2, markersize=5, label='Average Betting Size')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Amount of Trades and Average Betting Size per Hour')
plt.xticks(trades_per_hour.index)
plt.legend()
plt.show()
