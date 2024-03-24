import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('DBMaster.csv')

# Change date
df['open_date'] = pd.to_datetime(df['open_date'])

# ETH price
df_correct_eth = df[df['perpetual_asset'] == 'ETH']

# Group by month and amount of traders
monthly_players = df.groupby(df['open_date'].dt.to_period('M'))['player'].nunique().to_timestamp()

# Group by month and ETH price
monthly_eth_price_correct = df_correct_eth.groupby(df_correct_eth['open_date'].dt.to_period('M'))['priceOpened'].mean().to_timestamp()

# Diagram
fig, ax1 = plt.subplots(figsize=(14, 8))


ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=10))  # Jeden 10. Tag markieren
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Amount of Traders
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Number of Players', color=color)
ax1.plot(monthly_players.index, monthly_players, color=color, label='Number of Players')
ax1.tick_params(axis='y', labelcolor=color)

# ETH Price
ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('ETH Price (USD)', color=color)
ax2.plot(monthly_eth_price_correct.index, monthly_eth_price_correct, color=color, label='ETH Price')
ax2.tick_params(axis='y', labelcolor=color)


players_min, players_max = monthly_players.min(), monthly_players.max()
eth_price_min, eth_price_max = monthly_eth_price_correct.min(), monthly_eth_price_correct.max()
ax1.set_ylim(players_min - (players_max - players_min) * 0.1, players_max + (players_max - players_min) * 0.1)
ax2.set_ylim(eth_price_min - (eth_price_max - eth_price_min) * 0.1, eth_price_max + (eth_price_max - eth_price_min) * 0.1)

fig.autofmt_xdate()  
plt.title('Number of Players and ETH Price Over Time - Granular View')
plt.show()
