import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Group by leverage and amount of trades
trades_pro_leverage = data.groupby('leverage').size().reset_index(name='Absolute Amount of Trades')

# Percentage shares
trades_pro_leverage['Percentage (%)'] = (trades_pro_leverage['Absolute Amount of Trades'] / trades_pro_leverage['Absolute Amount of Trades'].sum()) * 100

# Sort by total amount of trades
trades_pro_leverage = trades_pro_leverage.sort_values(by='Absolute Amount of Trades', ascending=False)

# Results
print(trades_pro_leverage)

