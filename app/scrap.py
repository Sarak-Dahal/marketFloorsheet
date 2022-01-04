import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl
import sqlite3
import csv
import html5lib

conn = sqlite3.connect('company.sqlite')
cursor = conn.cursor()

sql_query = """ SELECT * FROM listedStocks """
cursor.execute(sql_query)
data = cursor.fetchall()

with open('bingo.csv', 'a',newline='') as f:
    wtr = csv.writer(f,delimiter=',')
    for i in range(len(data)):
        companyName = data[i][1]
        companyCode = data[i][2]
        companySector = data[i][3]
        print(companyCode)
        url = 'https://nepalstockinfo.com/companyhistory/' + companyCode + ''
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find_all(class_='table table-bordered stripe row-border order-column example_datatable_fixedcolumn')

        dataFrame = pd.read_html(str(table))[0]

        dataFrame.to_csv('table.csv')
        dataFrame = pd.read_csv('table.csv', nrows=15)

        # Cleaning CSV File
        del dataFrame["Unnamed: 0"]
        del dataFrame["S.N"]

        # Reversing Dataframe to reverse order
        dataFrame = dataFrame.reindex(index=dataFrame.index[::-1])


        change = dataFrame['Price'].diff()
        change.dropna(inplace=True)
        #print(change)

        changeUp = change.copy()
        changeDown = change.copy()

        changeUp[changeUp<0]=0
        changeDown[changeDown>0]=0

        #print(change == changeDown+changeUp)

        avgUp = changeUp.rolling(14).mean()
        avgDown = changeDown.rolling(14).mean().abs()
        rs = avgUp/avgDown
        #rsi = 100 * (avgUp / (avgUp+avgDown))
        rsi = rs.apply(lambda x: 100-(100/(x+1)))

        #print(rsi[0])

        try:
            gotdata = rsi[0]
            companyRsi = gotdata
            #print(gotdata)
        except IndexError:
            companyRsi = 'null'
            #print('Error')

        wtr.writerow([companyCode,companyName,companySector,companyRsi])


f.close()





