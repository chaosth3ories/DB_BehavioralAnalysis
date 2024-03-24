import pandas as pd


data = pd.read_csv('DBMaster.csv')

# Change of date
data['open_date'] = pd.to_datetime(data['open_date'])
data['close_date'] = pd.to_datetime(data['close_date'])

# Trade duration per trade
data['trade_duration'] = (data['close_date'] - data['open_date']).dt.days

# Berechnungen
amount_trader = data['player'].nunique()
amount_trades = len(data)
volume_usd = data['volume_usd'].sum()
longs = len(data[data['direction'] == 'Long'])
shorts = len(data[data['direction'] == 'Short'])
avg_tradeduration = data['trade_duration'].mean()
median_tradeduration = data['trade_duration'].median()
avg_volume_per_trade = data['volume_usd'].mean()
median_volumen_per_trade = data['volume_usd'].median()
paid_fundingrate = data['totalFundingRatePaidUsd'].sum()
unleveredvolume_usd = data['_wagerAmount'].sum()

# Ausgabe der Ergebnisse
print(f"Amount of traders: {amount_trader}")
print(f"Amount of trades: {amount_trades}")
print(f"Volume in USD: {volume_usd}")
print(f"Unlevered Volume: {unleveredvolume_usd}")
print(f"Longs: {longs}")
print(f"Shorts: {shorts}")
print(f"Average Trade Duration: {avg_tradeduration} Tage")
print(f"Median Trade duration: {median_tradeduration} Tage")
print(f"Average Volume per trade: {avg_volume_per_trade} USD")
print(f"Median Volume per trade: {median_volumen_per_trade} USD")
print(f"Total paid fundingrate: {paid_fundingrate} USD")