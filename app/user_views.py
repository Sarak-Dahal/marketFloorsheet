from flask import render_template, request, session
import pandas as pd
from app import app
import csv

global session


@app.route('/')
def home():
    return render_template('login.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST' and 'un' in request.form and 'ps' in request.form:
        un = request.form['un']
        ps = request.form['ps']
        if (un=="sarak" and ps=="sarak@45"):
            session['loggedin'] = True
            url = "http://www.nepalstock.com/main/floorsheet/index/1/stock-symbol/asc/YTo1OntzOjExOiJjb250cmFjdC1ubyI7czowOiIiO3M6MTI6InN0b2NrLXN5bWJvbCI7czowOiIiO3M6NToiYnV5ZXIiO3M6MjoiNTgiO3M6Njoic2VsbGVyIjtzOjA6IiI7czo2OiJfbGltaXQiO3M6MzoiNTAwIjt9?contract-no=&stock-symbol=&buyer=&seller="
            df = pd.read_html(url, header=1)
            data = df[0]
            data = data.iloc[:-3]
            del data['S.N.']
            del data['Contract No']
            del data['Unnamed: 8']
            del data['Unnamed: 9']
            data.to_csv('csvFiles/floorsheet.csv')
            result = []
            tData = open('csvFiles/floorsheet.csv')
            reader = csv.DictReader(tData)
            for row in reader:
                result.append(dict(row))
            fieldnames = [key for key in result[0].keys()]

            return render_template('index.html', result=result, fieldnames=fieldnames, len=len)
        else:
            msg="Enter Correct Username or Password"
            return render_template('login.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form Correctly!'
        return render_template('login.html', msg=msg)
    return render_template('login.html')


@app.route("/floorsheet",methods=['GET','POST'])
def floorsheet():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        buy = request.form['buyer']
        sell = request.form['seller']

        url = "http://www.nepalstock.com/main/floorsheet/index/1/stock-symbol/asc/YTo1OntzOjExOiJjb250cmFjdC1ubyI7czowOiIiO3M6MTI6InN0b2NrLXN5bWJvbCI7czowOiIiO3M6NToiYnV5ZXIiO3M6MjoiNTgiO3M6Njoic2VsbGVyIjtzOjA6IiI7czo2OiJfbGltaXQiO3M6MzoiNTAwIjt9?contract-no=&stock-symbol=&buyer=" + buy + "&seller=" + sell + "&_limit=50000000000000"
        df = pd.read_html(url, header=1)
        data = df[0]
        data = data.iloc[:-3]
        del data['S.N.']
        del data['Contract No']
        del data['Unnamed: 8']
        del data['Unnamed: 9']
        del data['Rate']
        data.to_csv('csvFiles/floorsheet.csv')
        data.to_csv('csvFiles/modification.csv')
        result = []

        data['Quantity']=data['Quantity'].astype(float)

        a=data.groupby('Stock Symbol')['Amount'].sum()
        a.to_csv('csvFiles/output.csv')


        tData = open('csvFiles/output.csv')
        reader = csv.DictReader(tData)
        for row in reader:
            result.append(dict(row))
        fieldnames = [key for key in result[0].keys()]

        if buy=="":
            buy=0
        if sell=="":
            sell=0
        return render_template('index.html', result=result, fieldnames=fieldnames, len=len,buy=buy,sell=sell)


@app.route("/logout")
def logout():
    session['loggedin'] = False
    return render_template('login.html')
