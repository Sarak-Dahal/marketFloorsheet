import csv
import sqlite3
import pandas as pd
conn = sqlite3.connect('company.sqlite')

cursor = conn.cursor()

sql_query = """ Create table listedStocks (id integer PRIMARY KEY AUTOINCREMENT, name text, code text, sector text)"""
cursor.execute(sql_query)

file = open('../csvFiles/nepseCompanyName.csv')
contents = csv.reader(file)


insert_records = "Insert into listedStocks (id,name,code,sector) VALUES (?,?,?,?)"

cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM listedStocks"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)
cursor.commit()
cursor.close()


df = pd.read_csv('../csvFiles/nepseCompanyName.csv')
del df['S.N.']
del df['Unnamed: 4']
del df['Unnamed: 5']


da = df.iloc[:,2].tolist()
da = list(set(da))
print(da[0])
k=[]
for i in da:
    j = i.replace(' ','')
    k.append(j)
print(k)

for i in range (len(da)):
#use one more " below to rerun the code
    sql_query = """ Create table table%s (id integer PRIMARY KEY AUTOINCREMENT, name text)"""%k[i]
    cursor.execute(sql_query)

