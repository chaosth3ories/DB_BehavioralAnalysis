import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Group by collateral
trades_per_collateral = data.groupby('collateral_symbol').size().reset_index(name='Amount of Trades')

# Volume per collateral
volumen_per_collateral = data.groupby('collateral_symbol')['volume_usd'].sum().reset_index(name='Absolute Volume (USD)')

# Merge of results
results = pd.merge(trades_per_collateral, volumen_per_collateral, on='collateral_symbol')

# Amount of trades and volume
amount_trades = results['Amount of Trades'].sum()
volume = results['Absolute Volume (USD)'].sum()

# Percentages
results['Percentage Trades (%)'] = (results['Amount of Trades'] / amount_trades) * 100
results['Percentage Volume (%)'] = (results['Absolute Volume (USD)'] / volume) * 100

# Results
print(results)
