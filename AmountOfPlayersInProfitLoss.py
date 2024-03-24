import pandas as pd


data = pd.read_csv('DBMaster.csv')

# Total PnL
total_profit_loss_per_player = data.groupby('player')['profit_loss'].sum()

# Players in Profit
players_in_profit = total_profit_loss_per_player[total_profit_loss_per_player > 0].count()

# Players in Loss
players_in_loss = total_profit_loss_per_player[total_profit_loss_per_player < 0].count()

# Ausgabe der Ergebnisse
print(f"Players in Profit: {players_in_profit}")
print(f"Players in Loss: {players_in_loss}")
