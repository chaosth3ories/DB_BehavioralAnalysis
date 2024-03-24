import pandas as pd
import matplotlib.pyplot as plt

# Einlesen der Daten
data = pd.read_csv('DBMaster.csv')

# Sicherstellen, dass 'open_date' im korrekten Format ist
data['open_date'] = pd.to_datetime(data['open_date'])

# Filtern der Daten für Long Trades
long_trades = data[data['direction'] == 'Long']

# Filtern der Daten für Short Trades
short_trades = data[data['direction'] == 'Short']

# Gruppierung und Summierung des Volumens pro Tag für Long Trades
daily_volume_long = long_trades.groupby(long_trades['open_date'].dt.date)['volume_usd'].sum()

# Gruppierung und Summierung des Volumens pro Tag für Short Trades
daily_volume_short = short_trades.groupby(short_trades['open_date'].dt.date)['volume_usd'].sum()

# Erstellung des Graphen
plt.figure(figsize=(14, 7))

# Umwandlung der Indexe (Datum) zurück zu datetime, da groupby dt.date das Datum in string konvertiert
dates_long = pd.to_datetime(daily_volume_long.index)
dates_short = pd.to_datetime(daily_volume_short.index)

plt.plot(dates_long, daily_volume_long, label='Long Trades', linestyle='-', color='blue')
plt.plot(dates_short, daily_volume_short, label='Short Trades', linestyle='-', color='red')

plt.title('Tägliches Volumen für Long und Short Trades')
plt.xlabel('Datum')
plt.ylabel('Volumen in USD')
plt.legend()
plt.grid(True)

# Anzeigen des Graphen
plt.show()

