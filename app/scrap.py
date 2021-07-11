
import pandas as pd



df = pd.read_html('http://www.nepalstock.com/')

marketStatus = df[8]
nepseIndex = df[9]
otherIndex = df[10]

print(marketStatus)
marketStatus.to_csv('csvFiles/market.csv', header=True, index=False)