import pandas as pd

data = pd.read_csv('DBMaster.csv')

# Total fees
total_fees = data[['closeFeeProtocolUsd', 'liquidationFeePaidUsd', 'totalFundingRatePaidUsd']].sum().sum()

print(f"Total fees: {total_fees} USD")
