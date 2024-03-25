import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Profitable Trades
data['is_profitable'] = data['profit_loss'] > 0

# Win prob per player
winning_probability_per_player = data.groupby('player')['is_profitable'].mean()

# Avg
avg_winning_probability = winning_probability_per_player.mean()

# Med
median_winning_probability = winning_probability_per_player.median()

# Results
print(f"Avg winning prob per player: {avg_winning_probability:.2%}")
print(f"Median winning prob per player: {median_winning_probability:.2%}")