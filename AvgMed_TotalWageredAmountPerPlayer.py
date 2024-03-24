import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DBMaster.csv')

# Aggregating data
total_wagered_per_player = df.groupby('player')['_wagerAmount'].sum()

# Average and Median values
avg_wagered = total_wagered_per_player.mean()
median_wagered = total_wagered_per_player.median()

# Results
print(f"Average total amount wagered per player: {avg_wagered}")
print(f"Median total amount wagered per player: {median_wagered}")
