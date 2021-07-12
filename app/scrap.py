
import pandas as pd



df = pd.read_html('http://www.nepalstock.com/')

nepseIndex = df[13]
otherIndex = df[14]

print(otherIndex)
