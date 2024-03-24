import pandas as pd


data = pd.read_csv('DBMaster.csv')

# Filter by win trades
profit_trades = data[data['profit_loss'] > 0]

# Leverage
most_used_leverage = profit_trades['leverage'].mode().iloc[0]

# Perp Asset
most_used_perp_asset = profit_trades['perpetual_asset'].mode().iloc[0]

# Volume per player
total_volume_per_player = profit_trades.groupby('player')['volume_usd'].sum()

# Avg volume per player
average_volume_per_player = total_volume_per_player.mean()

# Avg amount of trades per player
average_trades_per_player = profit_trades.groupby('player').size().mean()

# Collateral
most_used_collateral = profit_trades['collateral_symbol'].mode().iloc[0]

# Long short
long_trades_percent = (profit_trades['direction'] == 'Long').mean() * 100
short_trades_percent = (profit_trades['direction'] == 'Short').mean() * 100

# Ausgabe der Ergebnisse
print(f"Most used leverage: {most_used_leverage}")
print(f"Most used Perp_Asset: {most_used_perp_asset}")
print(f"Avg Volume: {average_volume_per_player} USD")
print(f"Avg Trades per Gambler: {average_trades_per_player}")
print(f"Most used Collateral: {most_used_collateral}")
print(f"Share Long Trades: {long_trades_percent:.2f}%")
print(f"Share Short Trades: {short_trades_percent:.2f}%")
