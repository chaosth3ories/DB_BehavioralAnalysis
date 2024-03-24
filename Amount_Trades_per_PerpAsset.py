import pandas as pd


data = pd.read_csv('DBMaster.csv')

# Amount of Trades per Perp Asset
trades_per_asset = data.groupby('perpetual_asset').size().reset_index(name='Amount of Trades')

# Amount of Trades
amount_trades = trades_per_asset['Amount of Trades'].sum()

# Share per Perp Asset
trades_per_asset['Percentage per Asset'] = (trades_per_asset['Amount of Trades'] / amount_trades) * 100

trades_per_asset.columns = ['Perpetual Asset', 'Amount of Trades', 'Percentage (%)']

# Sort by share desc
trades_per_asset = trades_per_asset.sort_values(by='Percentage (%)', ascending=False)

# Results
print(trades_per_asset)

