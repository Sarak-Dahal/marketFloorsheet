import csv
import sqlite3
import pandas as pd
conn = sqlite3.connect('company.sqlite')


cursor = conn.cursor()
sql_query = """ Create table companyRsi (companyCode text, companyName text,companySector text,rsiValue BLOB)"""
cursor.execute(sql_query)

a_file = open('bingo.csv')
rows = csv.reader(a_file)
conn.executemany('INSERT INTO companyRsi VALUES (?,?,?,?)',rows)

conn.commit()
conn.close()