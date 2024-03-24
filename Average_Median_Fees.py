import pandas as pd


data = pd.read_csv('DBMaster.csv')

# Total Fees per Trade
data['totalFees'] = data['closeFeeProtocolUsd'] + data['liquidationFeePaidUsd'] + data['totalFundingRatePaidUsd']

# Average of Fees
average_fees = data['totalFees'].mean()

# Median of Fees
median_fees = data['totalFees'].median()

# Results
print(f"Average fees per trade: {average_fees} USD")
print(f"Median fees per trade: {median_fees} USD")
