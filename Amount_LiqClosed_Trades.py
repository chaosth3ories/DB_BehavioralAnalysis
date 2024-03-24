import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Filter by liquidated trades
liquidated_trades = data[data['position_status'] == 'Liquidated']

# Filtered by closed trades
closed_trades = data[data['position_status'] == 'Closed']

# Calculation of absolute numbers
trades_liquidated = len(liquidated_trades)
trades_closed = len(closed_trades)

# Absolute number of trades
amount_trades = len(data)

# Berechnung der Prozentzahlen
percent_liquidated = (trades_liquidated / amount_trades) * 100
percent_closed = (trades_closed / amount_trades) * 100

# Ausgabe der Ergebnisse
print(f"Liquidated Trades: {trades_liquidated}")
print(f"Closed Trades: {trades_closed}")
print(f"Percentage liquidated: {percent_liquidated:.2f}%")
print(f"Percentage closed: {percent_closed:.2f}%")
