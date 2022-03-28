import pandas as pd
import matplotlib

crude_oil_data = pd.read_csv("U.S._crude_oil_production.csv")
print(crude_oil_data.head(5))

print(crude_oil_data.columns[(crude_oil_data.sum(axis=0)) == 0])
crude_oil_data.drop(['Arizona','Virginia'], inplace=True, axis=1)
print(crude_oil_data.columns)
crude_oil_data['Date'] = pd.to_datetime(crude_oil_data['Month'])
crude_oil_data.drop("Month", inplace=True, axis=1)
crude_oil_data = crude_oil_data.rename(columns={'Federal Offshore Gulf of Mexico Crude Oil':'Mexico',
'Federal Offshore Pacific Crude Oil' : 'Pacific'})
crude_oil_data['Year'] = crude_oil_data['Date'].dt.year
print(crude_oil_data['Year'].sample(10))
crude_oil_data['Month'] = crude_oil_data['Date'].dt.month
print(crude_oil_data['Month'].sample(10))
crude_oil_data.to_csv("crude_oil_data_processed.csv", index = False)
print(crude_oil_data.describe())