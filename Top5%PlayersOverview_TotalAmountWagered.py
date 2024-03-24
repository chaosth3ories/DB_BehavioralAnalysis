import pandas as pd

df = pd.read_csv('DBMaster.csv')

# Change date
df['open_date'] = pd.to_datetime(df['open_date'])

# Wagered amount per player
total_wagered_per_player = df.groupby('player')['_wagerAmount'].sum()

# Top 5%
top_5_percent_threshold_wagered = total_wagered_per_player.quantile(0.95)

top_5_percent_players_wagered = total_wagered_per_player[total_wagered_per_player >= top_5_percent_threshold_wagered].index

# Filter by top 5%
df_top_5_percent_wagered = df[df['player'].isin(top_5_percent_players_wagered)]

# Calculations
average_trades_top_5_percent_wagered = df_top_5_percent_wagered.groupby('player').size().mean()
median_trades_top_5_percent_wagered = df_top_5_percent_wagered.groupby('player').size().median()
average_wager_top_5_percent_wagered = df_top_5_percent_wagered['_wagerAmount'].mean()
median_wager_top_5_percent_wagered = df_top_5_percent_wagered['_wagerAmount'].median()
average_profit_loss_top_5_percent_wagered = df_top_5_percent_wagered['profit_loss'].mean()
median_profit_loss_top_5_percent_wagered = df_top_5_percent_wagered['profit_loss'].median()
betting_duration_per_top_5_percent_wagered = df_top_5_percent_wagered.groupby('player')['open_date'].apply(lambda x: (x.max() - x.min()).days + 1)
average_betting_duration_top_5_percent_wagered = betting_duration_per_top_5_percent_wagered.mean()
median_betting_duration_top_5_percent_wagered = betting_duration_per_top_5_percent_wagered.median()
total_wagered_per_top_5_percent_wagered = df_top_5_percent_wagered.groupby('player')['_wagerAmount'].sum()
average_total_wagered_top_5_percent_wagered = total_wagered_per_top_5_percent_wagered.mean()
median_total_wagered_top_5_percent_wagered = total_wagered_per_top_5_percent_wagered.median()

# Results
print(f"Amount of Top 5%: {len(top_5_percent_players_wagered)}")
print(f"Avg Amount of Trades: {average_trades_top_5_percent_wagered}")
print(f"Median of Trades: {median_trades_top_5_percent_wagered}")
print(f"Average total amount wagered: {average_wager_top_5_percent_wagered}")
print(f"Median total amount wagered: {median_wager_top_5_percent_wagered}")
print(f"Average PnL: {average_profit_loss_top_5_percent_wagered}")
print(f"Median PnL: {median_profit_loss_top_5_percent_wagered}")
print(f"Average duration: {average_betting_duration_top_5_percent_wagered}")
print(f"Median duration: {median_betting_duration_top_5_percent_wagered}")
print(f"Durchschnittlicher Gesamteinsatz der Top 5% Spieler nach Gesamteinsatz: {average_total_wagered_top_5_percent_wagered}")
print(f"Median des Gesamteinsatzes der Top 5% Spieler nach Gesamteinsatz: {median_total_wagered_top_5_percent_wagered}")

