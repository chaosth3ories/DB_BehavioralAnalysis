import pandas as pd


data = pd.read_csv('DBMaster.csv')

# Volume per perp asset
volume_per_asset = data.groupby('perpetual_asset')['volume_usd'].sum().reset_index()

# total volume
totalvolume = volume_per_asset['volume_usd'].sum()

# Share of volume
volume_per_asset['Percentage_Share'] = (volume_per_asset['volume_usd'] / totalvolume) * 100


volume_per_asset.columns = ['Perpetual Asset', 'Absolute Volume (USD)', 'Percentage (%)']

# results
print(volume_per_asset)
