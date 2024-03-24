import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('DBMaster.csv')

# Date change
df['open_date'] = pd.to_datetime(df['open_date']).dt.date

# Average size per trade per bet
average_wager_per_day = df.groupby('open_date')['_wagerAmount'].mean()

# Average ETH price
df_eth = df[df['perpetual_asset'] == 'ETH']
average_eth_price_per_day = df_eth.groupby('open_date')['priceOpened'].mean()


fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Average Betting Size in USD', color=color)
ax1.plot(average_wager_per_day.index, average_wager_per_day, color=color, label='Average Deposit')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('ETH Price in USD', color=color)
ax2.plot(average_eth_price_per_day.index, average_eth_price_per_day, color=color, label='ETH Price in USD')
ax2.tick_params(axis='y', labelcolor=color)

ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
fig.autofmt_xdate()

plt.title('Average Betting Size in USD per Trade and ETH Price in USD over Time')
plt.legend()
plt.show()
