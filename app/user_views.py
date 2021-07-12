from flask import render_template, request, session, redirect
import pandas as pd
from app import app
import csv

global session


@app.route('/')
def start():
    return render_template('login.html')


@app.route('/home')
def home():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        headerTitle = 'Dashboard'

        df = pd.read_html('http://www.nepalstock.com/')
        marketStatus = df[8]
        nepseIndex = df[13]
        otherIndex = df[14]

        marketStatus.to_csv('csvFiles/marketStatus.csv', header=True, index=False)
        del nepseIndex['Unnamed: 4']
        del nepseIndex['Unnamed: 5']
        nepseIndex.to_csv('csvFiles/nepseIndex.csv', header=True, index=False)
        del otherIndex['Unnamed: 4']
        otherIndex.to_csv('csvFiles/otherIndex.csv', header=True, index=False)

        nepseData = pd.read_csv('csvFiles/nepseIndex.csv')
        nepse = nepseData.values.tolist()

        otherData = pd.read_csv('csvFiles/otherIndex.csv')
        other = otherData.values.tolist()

        # NEPSE Index
        nepseIndexData = nepse[0][1]
        nepsePC = nepse[0][2]
        nepsePerC = nepse[0][3]
        if nepsePC > 0.00:
            nepseColor = 'green'
        elif nepsePC == 0.00:
            nepseColor = 'blue'
        else:
            nepseColor = 'red'

        # Sensitive Index
        sensitive = nepse[1][1]
        sensitivePC = nepse[1][2]
        sensitivePerC = nepse[1][3]
        if sensitivePC > 0.00:
            sensColor = 'green'
        elif sensitivePC == 0.00:
            sensColor = 'blue'
        else:
            sensColor = 'red'

        # Float Index
        nepseFloat = nepse[2][1]
        nepseFloatPC = nepse[2][2]
        nepseFloatPerC = nepse[2][3]
        if nepseFloatPC > 0.00:
            floatColor = 'green'
        elif nepseFloatPC == 0.00:
            floatColor = 'blue'
        else:
            floatColor = 'red'

        # Sen. Float
        senFloat = nepse[3][1]
        senFloatPC = nepse[3][2]
        senFloatPerC = nepse[3][3]
        if senFloatPC > 0.00:
            floatSensColor = 'green'
        elif senFloatPC == 0.00:
            floatSensColor = 'blue'
        else:
            floatSensColor = 'red'

        # Banking Index
        bank = other[0][1]
        bankPC = other[0][2]
        bankPerC = other[0][3]
        if bankPC > 0.00:
            bankColor = 'green'
        elif bankPC == 0.00:
            bankColor = 'blue'
        else:
            bankColor = 'red'
            
        # Trading Index
        trading = other[1][1]
        tradingPC = other[1][2]
        tradingPerC = other[1][3]
        if tradingPC > 0.00:
            tradingColor = 'green'
        elif tradingPC == 0.00:
            tradingColor = 'blue'
        else:
            tradingColor = 'red'

        
        # Hotel and Tourism
        hotel = other[2][1]
        hotelPC = other[2][2]
        hotelPerC = other[2][3]
        if hotelPC > 0.00:
            hotelColor = 'green'
        elif hotelPC == 0.00:
            hotelColor = 'blue'
        else:
            hotelColor = 'red'


        # Development Bank Index
        devBank = other[3][1]
        devBankPC = other[3][2]
        devBankPerC = other[3][3]
        if devBankPC > 0.00:
            devBankColor = 'green'
        elif devBankPC == 0.00:
            devBankColor = 'blue'
        else:
            devBankColor = 'red'


        # Hydropower Index
        hydro = other[4][1]
        hydroPC = other[4][2]
        hydroPerC = other[4][3]
        if hydroPC > 0.00:
            hydroColor = 'green'
        elif hydroPC == 0.00:
            hydroColor = 'blue'
        else:
            hydroColor = 'red'


        # Finance Index
        finance = other[5][1]
        financePC = other[5][2]
        financePerC = other[5][3]
        if financePC > 0.00:
            financeColor = 'green'
        elif financePC == 0.00:
            financeColor = 'blue'
        else:
            financeColor = 'red'


        # Life Insurance
        lifeInsurance = other[10][1]
        lifeInsurancePC = other[10][2]
        lifeInsurancePerC = other[10][3]
        if lifeInsurancePC > 0.00:
            lifeInsuranceColor = 'green'
        elif lifeInsurancePC == 0.00:
            lifeInsuranceColor = 'blue'
        else:
            lifeInsuranceColor = 'red'


        # Non-Life Insurance
        nonLifeInsurance = other[6][1]
        nonLifeInsurancePC = other[6][2]
        nonLifeInsurancePerC = other[6][3]
        if nonLifeInsurancePC > 0.00:
            nonLifeInsuranceColor = 'green'
        elif nonLifeInsurancePC == 0.00:
            nonLifeInsuranceColor = 'blue'
        else:
            nonLifeInsuranceColor = 'red'



        # Manufacture
        manufacture = other[7][1]
        manufacturePC = other[7][2]
        manufacturePerC = other[7][3]
        if manufacturePC > 0.00:
            manufactureColor = 'green'
        elif manufacturePC == 0.00:
            manufactureColor = 'blue'
        else:
            manufactureColor = 'red'


        # Other
        otherIndex = other[8][1]
        otherIndexPC = other[7][1]
        otherIndexPerC = other[8][3]
        if otherIndexPC > 0.00:
            otherIndexColor = 'green'
        elif otherIndexPC == 0.00:
            otherIndexColor = 'blue'
        else:
            otherIndexColor = 'red'


        # Microfinance
        microfinance = other[9][1]
        microfinancePC = other[9][2]
        microfinancePerC = other[9][3]
        if microfinancePC > 0.00:
            microfinanceColor = 'green'
        elif microfinancePC == 0.00:
            microfinanceColor = 'blue'
        else:
            microfinanceColor = 'red'


        # Mutual Fund
        mutualFund = other[11][1]
        mutualFundPC = other[11][2]
        mutualFundPerC = other[11][3]
        if mutualFundPC > 0.00:
            mutualFundColor = 'green'
        elif mutualFundPC == 0.00:
            mutualFundColor = 'blue'
        else:
            mutualFundColor = 'red'

        # For top gainers and losers
        df = pd.read_html('https://merolagani.com/LatestMarket.aspx')
        data = df[0].head(1000)
        del data['High']
        del data['Low']
        del data['Open']
        del data['Qty.']
        del data['Unnamed: 7']
        del data['Unnamed: 8']

        gainSort = data.sort_values(by=["% Change"], ascending=False)
        gainTab = gainSort.head(10)
        gainTab.to_csv('csvFiles/gainTab.csv', header=True, index=False)
        gain = []
        tGain = open('csvFiles/gainTab.csv')
        reader = csv.DictReader(tGain)
        for row in reader:
            gain.append(dict(row))
        finalGain = [key for key in gain[0].keys()]

        loseSort = data.sort_values(by=["% Change"], ascending=True)
        loseTab = loseSort.head(10)
        loseTab.to_csv('csvFiles/loseTab.csv', header=True, index=False)
        lose = []
        tLose = open('csvFiles/loseTab.csv')
        reader = csv.DictReader(tLose)
        for row in reader:
            lose.append(dict(row))
        finalLose = [key for key in lose[0].keys()]

        return render_template('home.html', headerTitle=headerTitle, gain=gain, finalGain=finalGain, lose=lose,
                               finalLose=finalLose,
                               len=len, nepseIndexData=nepseIndexData, nepsePC=nepsePC, nepsePerC=nepsePerC,
                               nepseColor=nepseColor, sensitive=sensitive, sensitivePC=sensitivePC,
                               sensitivePerC=sensitivePerC, sensColor=sensColor, nepseFloat=nepseFloat,
                               nepseFloatPC=nepseFloatPC, nepseFloatPerC=nepseFloatPerC, senFloat=senFloat
                               , senFloatPC=senFloatPC, senFloatPerC=senFloatPerC, floatColor=floatColor,
                               floatSensColor=floatSensColor,bank=bank,bankPC=bankPC,bankPerC=bankPerC,bankColor=bankColor,
                               trading=trading,tradingPC=tradingPC,tradingPerC=tradingPerC,tradingColor=tradingColor,hotel = hotel,
                               hotelPC = hotelPC,hotelPerC = hotelPerC, hotelColor = hotelColor,devBank = devBank,
                               devBankPC = devBankPC, devBankPerC = devBankPerC, devBankColor = devBankColor,hydro = hydro,
                               hydroPC = hydroPC, hydroPerC = hydroPerC, hydroColor = hydroColor,finance = finance,
                               financePC = financePC, financePerC = financePerC, financeColor = financeColor,
                               lifeInsurance = lifeInsurance, lifeInsurancePC = lifeInsurancePC, lifeInsurancePerC = lifeInsurancePerC,
                               lifeInsuranceColor = lifeInsuranceColor,nonLifeInsurance = nonLifeInsurance, nonLifeInsurancePC = nonLifeInsurancePC,
                               nonLifeInsurancePerC = nonLifeInsurancePerC, nonLifeInsuranceColor = nonLifeInsuranceColor,manufacture = manufacture,
                               manufacturePC = manufacturePC, manufacturePerC = manufacturePerC, manufactureColor = manufactureColor,
                               otherIndex = otherIndex, otherIndexPC = otherIndexPC, otherIndexPerC = otherIndexPerC, otherIndexColor = otherIndexColor,
                               microfinance = microfinance, microfinancePC = microfinancePC, microfinancePerC = microfinancePerC, microfinanceColor = microfinanceColor,
                               mutualFund = mutualFund, mutualFundPC = mutualFundPC, mutualFundPerC = mutualFundPerC, mutualFundColor = mutualFundColor)



@app.route('/news')
def news():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        headerTitle = 'Stock News - Comming Soon...'
        return render_template('news.html', headerTitle=headerTitle)


@app.route('/myPortfolio')
def marketDepth():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        headerTitle = 'My Portfolio'
        return render_template('myPortfolio.html', headerTitle=headerTitle)


@app.route('/stockPrice')
def stockPrice():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        headerTitle = 'Stock Price'
        return render_template('stockPrice.html', headerTitle=headerTitle)


@app.route('/calculator')
def calculator():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        headerTitle = 'Calculator'
        return render_template('calculator.html', headerTitle=headerTitle)


@app.route('/myAccount')
def myAccount():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        headerTitle = 'My Account'
        return render_template('myAccount.html', headerTitle=headerTitle)




@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'un' in request.form and 'ps' in request.form:
        un = request.form['un']
        ps = request.form['ps']
        if (un == "sarak" and ps == "sarak@45"):
            session['loggedin'] = True
            session['id'] = un
            return redirect('floorsheet')
        else:
            msg = "Enter Correct Username or Password"
            return render_template('login.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form Correctly!'
        return render_template('login.html', msg=msg)
    return render_template('login.html')


@app.route("/floorsheet")
def startFloorsheet():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
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
        headerTitle = 'Floorsheet'
        return render_template('floorsheet.html', result=result, fieldnames=fieldnames, len=len,
                               headerTitle=headerTitle)


@app.route("/floorsheet", methods=['GET', 'POST'])
def floorsheet():
    headerTitle = 'Floorsheet'

    loginChecker()

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

    data['Quantity'] = data['Quantity'].astype(float)

    a = data.groupby('Stock Symbol')['Amount'].sum()
    a.to_csv('csvFiles/output.csv')

    tData = open('csvFiles/output.csv')
    reader = csv.DictReader(tData)
    for row in reader:
        result.append(dict(row))
    fieldnames = [key for key in result[0].keys()]

    if buy == "":
        buy = 0
    if sell == "":
        sell = 0

    return render_template('floorsheet.html', result=result, fieldnames=fieldnames, len=len, buy=buy, sell=sell,
                           headerTitle=headerTitle)


@app.route("/logout")
def logout():
    session['loggedin'] = False
    return redirect('login')


def loginChecker():
    if session['loggedin'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
