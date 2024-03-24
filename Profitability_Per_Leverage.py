import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Profitable trades
data['Profitable'] = data['profit_loss'] > 0

# Group by leverage, profitable, amount of trades
profitable_trades_pro_leverage = data.groupby(['leverage', 'Profitable']).size().unstack(fill_value=0)

# Share of profitable trades by leverage
profitable_trades_pro_leverage['Share of Profitable Trades (%)'] = (profitable_trades_pro_leverage[True] / (profitable_trades_pro_leverage[True] + profitable_trades_pro_leverage[False])) * 100

# Amount of Trades per leverage
profitable_trades_pro_leverage['Amount of Trades'] = profitable_trades_pro_leverage[True] + profitable_trades_pro_leverage[False]

# Sort
profitable_trades_pro_leverage = profitable_trades_pro_leverage.sort_values(by=True, ascending=False)

# Final table
final_table = profitable_trades_pro_leverage[[True, 'Share of Profitable Trades (%)', 'Amount of Trades']].rename(columns={True: 'Amount Profitable Trades'})

# Results
print(final_table)
