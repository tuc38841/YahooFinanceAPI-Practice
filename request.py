import json
import requests
import os

headers = {
    'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com',
    'X-rapidapi-key': os.environ.get("X_RAPIDAPI_KEY")
}


financials = [{'defaultKeyStatistics': {'annualHoldingsTurnover': {}, 'enterpriseToRevenue': {'raw': 4.068, 'fmt': '4.07'}, 'beta3Year': {}, 'profitMargins': {'raw': 0.21490999, 'fmt': '21.49%'}, 'enterpriseToEbitda': {'raw': 13.938, 'fmt': '13.94'}, '52WeekChange': {'raw': 0.28123522, 'fmt': '28.12%'}, 'morningStarRiskRating': {}, 'forwardEps': {'raw': 15.45, 'fmt': '15.45'}, 'revenueQuarterlyGrowth': {}, 'sharesOutstanding': {'raw': 4375479808, 'fmt': '4.38B', 'longFmt': '4,375,479,808'}, 'fundInceptionDate': {}, 'annualReportExpenseRatio': {}, 'totalAssets': {}, 'bookValue': {'raw': 20.418, 'fmt': '20.42'}, 'sharesShort': {'raw': 29008504, 'fmt': '29.01M', 'longFmt': '29,008,504'}, 'sharesPercentSharesOut': {'raw': 0.0066000004, 'fmt': '0.66%'}, 'fundFamily': None, 'lastFiscalYearEnd': {'raw': 1569628800, 'fmt': '2019-09-28'}, 'heldPercentInstitutions': {'raw': 0.61917, 'fmt': '61.92%'}, 'netIncomeToCommon': {'raw': 57527001088, 'fmt': '57.53B', 'longFmt': '57,527,001,088'}, 'trailingEps': {'raw': 12.595, 'fmt': '12.60'}, 'lastDividendValue': {}, 'SandP52WeekChange': {'raw': -0.13972175, 'fmt': '-13.97%'}, 'priceToBook': {'raw': 11.988441, 'fmt': '11.99'}, 'heldPercentInsiders': {'raw': 0.00066, 'fmt': '0.07%'}, 'nextFiscalYearEnd': {'raw': 1632787200, 'fmt': '2021-09-28'}, 'yield': {}, 'mostRecentQuarter': {'raw': 1577491200, 'fmt': '2019-12-28'}, 'shortRatio': {'raw': 0.72, 'fmt': '0.72'}, 'sharesShortPreviousMonthDate': {'raw': 1580428800, 'fmt': '2020-01-31'}, 'floatShares': {'raw': 4370579462, 'fmt': '4.37B', 'longFmt': '4,370,579,462'}, 'beta': {'raw': 1.292953, 'fmt': '1.29'}, 'enterpriseValue': {'raw': 1088888635392, 'fmt': '1.09T', 'longFmt': '1,088,888,635,392'}, 'priceHint': {'raw': 2, 'fmt': '2', 'longFmt': '2'}, 'threeYearAverageReturn': {}, 'lastSplitDate': {'raw': 1402272000, 'fmt': '2014-06-09'}, 'lastSplitFactor': '7:1', 'legalType': None, 'morningStarOverallRating': {}, 'earningsQuarterlyGrowth': {'raw': 0.114, 'fmt': '11.40%'}, 'priceToSalesTrailing12Months': {}, 'dateShortInterest': {'raw': 1582848000, 'fmt': '2020-02-28'}, 'pegRatio': {'raw': 1.77, 'fmt': '1.77'}, 'ytdReturn': {}, 'forwardPE': {'raw': 15.843366, 'fmt': '15.84'}, 'maxAge': 1, 'lastCapGain': {}, 'shortPercentOfFloat': {'raw': 0.0066000004, 'fmt': '0.66%'}, 'sharesShortPriorMonth': {'raw': 41543664, 'fmt': '41.54M', 'longFmt': '41,543,664'}, 'category': None, 'fiveYearAverageReturn': {}}, 'financialsTemplate': {'code': 'N', 'maxAge': 1}, 'price': {'quoteSourceName': 'Delayed Quote', 'regularMarketOpen': {'raw': 247.385, 'fmt': '247.38'}, 'averageDailyVolume3Month': {'raw': 45042004, 'fmt': '45.04M', 'longFmt': '45,042,004'}, 'exchange': 'NMS', 'regularMarketTime': 1584648001, 'volume24Hr': {}, 'regularMarketDayHigh': {'raw': 252.805, 'fmt': '252.80'}, 'shortName': 'Apple Inc.', 'averageDailyVolume10Day': {'raw': 79629562, 'fmt': '79.63M', 'longFmt': '79,629,562'}, 'longName': 'Apple Inc.', 'regularMarketChange': {'raw': -1.8899994, 'fmt': '-1.89'}, 'currencySymbol': '$', 'regularMarketPreviousClose': {'raw': 246.67, 'fmt': '246.67'}, 'postMarketTime': 1584662392, 'preMarketPrice': {'raw': 250.65, 'fmt': '250.65'}, 'preMarketTime': 1584708696, 'exchangeDataDelayedBy': 0, 'toCurrency': None, 'postMarketChange': {'raw': -1.5299988, 'fmt': '-1.53'}, 'postMarketPrice': {'raw': 243.25, 'fmt': '243.25'}, 'exchangeName': 'NasdaqGS', 'preMarketChange': {'raw': 5.869995, 'fmt': '5.87'}, 'circulatingSupply': {}, 'regularMarketDayLow': {'raw': 242.61, 'fmt': '242.61'}, 'priceHint': {'raw': 2, 'fmt': '2', 'longFmt': '2'}, 'currency': 'USD', 'regularMarketPrice': {'raw': 244.78, 'fmt': '244.78'}, 'regularMarketVolume': {'raw': 67964255, 'fmt': '67.96M', 'longFmt': '67,964,255.00'}, 'lastMarket': None, 'regularMarketSource': 'FREE_REALTIME', 'openInterest': {}, 'marketState': 'PRE', 'underlyingSymbol': None, 'marketCap': {'raw': 1071029944320, 'fmt': '1.07T', 'longFmt': '1,071,029,944,320.00'}, 'quoteType': 'EQUITY', 'preMarketChangePercent': {'raw': 0.0239807, 'fmt': '2.40%'}, 'volumeAllCurrencies': {}, 'postMarketSource': 'DELAYED', 'strikePrice': {}, 'symbol': 'AAPL', 'postMarketChangePercent': {'raw': -0.0062505053, 'fmt': '-0.63%'}, 'preMarketSource': 'DELAYED', 'maxAge': 1, 'fromCurrency': None, 'regularMarketChangePercent': {'raw': -0.007662056, 'fmt': '-0.77%'}}, 'financialData': {'ebitdaMargins': {'raw': 0.29184, 'fmt': '29.18%'}, 'profitMargins': {'raw': 0.21490999, 'fmt': '21.49%'}, 'grossMargins': {'raw': 0.37947, 'fmt': '37.95%'}, 'operatingCashflow': {'raw': 73216999424, 'fmt': '73.22B', 'longFmt': '73,216,999,424'}, 'revenueGrowth': {'raw': 0.089, 'fmt': '8.90%'}, 'operatingMargins': {'raw': 0.24712999, 'fmt': '24.71%'}, 'ebitda': {'raw': 78121000960, 'fmt': '78.12B', 'longFmt': '78,121,000,960'}, 'targetLowPrice': {'raw': 207.77, 'fmt': '207.77'}, 'recommendationKey': 'buy', 'grossProfits': {'raw': 98392000000, 'fmt': '98.39B', 'longFmt': '98,392,000,000'}, 'freeCashflow': {'raw': 45594251264, 'fmt': '45.59B', 'longFmt': '45,594,251,264'}, 'targetMedianPrice': {'raw': 325, 'fmt': '325.00'}, 'currentPrice': {'raw': 244.78, 'fmt': '244.78'}, 'earningsGrowth': {'raw': 0.194, 'fmt': '19.40%'}, 'currentRatio': {'raw': 1.598, 'fmt': '1.60'}, 'returnOnAssets': {'raw': 0.11576, 'fmt': '11.58%'}, 'numberOfAnalystOpinions': {'raw': 38, 'fmt': '38', 'longFmt': '38'}, 'targetMeanPrice': {'raw': 320.99, 'fmt': '320.99'}, 'debtToEquity': {'raw': 130.403, 'fmt': '130.40'}, 'returnOnEquity': {'raw': 0.55468, 'fmt': '55.47%'}, 'targetHighPrice': {'raw': 370.8, 'fmt': '370.80'}, 'totalCash': {'raw': 107162001408, 'fmt': '107.16B', 'longFmt': '107,162,001,408'}, 'totalDebt': {'raw': 116750999552, 'fmt': '116.75B', 'longFmt': '116,750,999,552'}, 'totalRevenue': {'raw': 267683004416, 'fmt': '267.68B', 'longFmt': '267,683,004,416'}, 'totalCashPerShare': {'raw': 24.491, 'fmt': '24.49'}, 'financialCurrency': 'USD', 'maxAge': 86400, 'revenuePerShare': {'raw': 58.992, 'fmt': '58.99'}, 'quickRatio': {'raw': 1.44, 'fmt': '1.44'}, 'recommendationMean': {'raw': 2, 'fmt': '2.00'}}, 'quoteType': {'exchange': 'NMS', 'shortName': 'Apple Inc.', 'longName': 'Apple Inc.', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EDT', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-14400000', 'quoteType': 'EQUITY', 'symbol': 'AAPL', 'messageBoardId': 'finmb_24937', 'market': 'us_market'}, 'calendarEvents': {'maxAge': 1, 'earnings': {'earningsDate': [{'raw': 1588032000, 'fmt': '2020-04-28'}, {'raw': 1588550400, 'fmt': '2020-05-04'}], 'earningsAverage': {'raw': 2.5, 'fmt': '2.50'}, 'earningsLow': {'raw': 1.96, 'fmt': '1.96'}, 'earningsHigh': {'raw': 3.11, 'fmt': '3.11'}, 'revenueAverage': {'raw': 58157700000, 'fmt': '58.16B', 'longFmt': '58,157,700,000'}, 'revenueLow': {'raw': 50240700000, 'fmt': '50.24B', 'longFmt': '50,240,700,000'}, 'revenueHigh': {'raw': 66545000000, 'fmt': '66.55B', 'longFmt': '66,545,000,000'}}, 'exDividendDate': {'raw': 1581033600, 'fmt': '2020-02-07'}, 'dividendDate': {'raw': 1581552000, 'fmt': '2020-02-13'}}, 'summaryDetail': {'previousClose': {'raw': 246.67, 'fmt': '246.67'}, 'regularMarketOpen': {'raw': 247.385, 'fmt': '247.38'}, 'twoHundredDayAverage': {'raw': 268.8826, 'fmt': '268.88'}, 'trailingAnnualDividendYield': {'raw': 0.012324158, 'fmt': '1.23%'}, 'payoutRatio': {'raw': 0.2394, 'fmt': '23.94%'}, 'volume24Hr': {}, 'regularMarketDayHigh': {'raw': 252.805, 'fmt': '252.80'}, 'navPrice': {}, 'averageDailyVolume10Day': {'raw': 79629562, 'fmt': '79.63M', 'longFmt': '79,629,562'}, 'totalAssets': {}, 'regularMarketPreviousClose': {'raw': 246.67, 'fmt': '246.67'}, 'fiftyDayAverage': {'raw': 296, 'fmt': '296.00'}, 'trailingAnnualDividendRate': {'raw': 3.04, 'fmt': '3.04'}, 'open': {'raw': 247.385, 'fmt': '247.38'}, 'toCurrency': None, 'averageVolume10days': {'raw': 79629562, 'fmt': '79.63M', 'longFmt': '79,629,562'}, 'expireDate': {}, 'yield': {}, 'algorithm': None, 'dividendRate': {'raw': 3.08, 'fmt': '3.08'}, 'exDividendDate': {'raw': 1581033600, 'fmt': '2020-02-07'}, 'beta': {'raw': 1.292953, 'fmt': '1.29'}, 'circulatingSupply': {}, 'startDate': {}, 'regularMarketDayLow': {'raw': 242.61, 'fmt': '242.61'}, 'priceHint': {'raw': 2, 'fmt': '2', 'longFmt': '2'}, 'currency': 'USD', 'trailingPE': {'raw': 19.434696, 'fmt': '19.43'}, 'regularMarketVolume': {'raw': 67964255, 'fmt': '67.96M', 'longFmt': '67,964,255'}, 'lastMarket': None, 'maxSupply': {}, 'openInterest': {}, 'marketCap': {'raw': 1071029944320, 'fmt': '1.07T', 'longFmt': '1,071,029,944,320'}, 'volumeAllCurrencies': {}, 'strikePrice': {}, 'averageVolume': {'raw': 45042004, 'fmt': '45.04M', 'longFmt': '45,042,004'}, 'priceToSalesTrailing12Months': {'raw': 4.001113, 'fmt': '4.00'}, 'dayLow': {'raw': 242.61, 'fmt': '242.61'}, 'ask': {'raw': 257.74, 'fmt': '257.74'}, 'ytdReturn': {}, 'askSize': {'raw': 2200, 'fmt': '2.2k', 'longFmt': '2,200'}, 'volume': {'raw': 67964255, 'fmt': '67.96M', 'longFmt': '67,964,255'}, 'fiftyTwoWeekHigh': {'raw': 327.85, 'fmt': '327.85'}, 'forwardPE': {'raw': 15.843366, 'fmt': '15.84'}, 'maxAge': 1, 'fromCurrency': None, 'fiveYearAvgDividendYield': {'raw': 1.6, 'fmt': '1.60'}, 'fiftyTwoWeekLow': {'raw': 170.27, 'fmt': '170.27'}, 'bid': {'raw': 255.55, 'fmt': '255.55'}, 'tradeable': True, 'dividendYield': {'raw': 0.0125, 'fmt': '1.25%'}, 'bidSize': {'raw': 900, 'fmt': '900', 'longFmt': '900'}, 'dayHigh': {'raw': 252.805, 'fmt': '252.80'}}, 'symbol': 'AAPL', 'pageViews': {'shortTermTrend': 'DOWN', 'midTermTrend': 'UP', 'longTermTrend': 'UP', 'maxAge': 1}, 'quoteData': {'AAPL': {'sourceInterval': 15, 'regularMarketOpen': {'raw': 247.385, 'fmt': '247.38'}, 'exchange': 'NMS', 'regularMarketTime': {'raw': 1584648001, 'fmt': '4:00PM EDT'}, 'fiftyTwoWeekRange': {'raw': '170.27 - 327.85', 'fmt': '170.27 - 327.85'}, 'sharesOutstanding': {'raw': 4375479808, 'fmt': '4.375B', 'longFmt': '4,375,479,808'}, 'regularMarketDayHigh': {'raw': 252.805, 'fmt': '252.80'}, 'shortName': 'Apple Inc.', 'longName': 'Apple Inc.', 'exchangeTimezoneName': 'America/New_York', 'regularMarketChange': {'raw': -1.8899994, 'fmt': '-1.89'}, 'regularMarketPreviousClose': {'raw': 246.67, 'fmt': '246.67'}, 'fiftyTwoWeekHighChange': {'raw': -83.07001, 'fmt': '-83.07'}, 'exchangeTimezoneShortName': 'EDT', 'fiftyTwoWeekLowChange': {'raw': 74.509995, 'fmt': '74.51'}, 'exchangeDataDelayedBy': 0, 'regularMarketDayLow': {'raw': 242.61, 'fmt': '242.61'}, 'priceHint': 2, 'currency': 'USD', 'regularMarketPrice': {'raw': 244.78, 'fmt': '244.78'}, 'regularMarketVolume': {'raw': 67964255, 'fmt': '67.964M', 'longFmt': '67,964,255'}, 'isLoading': False, 'triggerable': True, 'gmtOffSetMilliseconds': -14400000, 'firstTradeDateMilliseconds': 345459600000, 'region': 'US', 'marketState': 'PRE', 'marketCap': {'raw': 1071029944320, 'fmt': '1.071T', 'longFmt': '1,071,029,944,320'}, 'quoteType': 'EQUITY', 'invalid': False, 'symbol': 'AAPL', 'language': 'en-US', 'fiftyTwoWeekLowChangePercent': {'raw': 0.43759906, 'fmt': '43.76%'}, 'regularMarketDayRange': {'raw': '242.61 - 252.805', 'fmt': '242.61 - 252.80'}, 'messageBoardId': 'finmb_24937', 'fiftyTwoWeekHigh': {'raw': 327.85, 'fmt': '327.85'}, 'fiftyTwoWeekHighChangePercent': {'raw': -0.2533781, 'fmt': '-25.34%'}, 'uuid': '8b10e4ae-9eeb-3684-921a-9ab27e4d87aa', 'market': 'us_market', 'fiftyTwoWeekLow': {'raw': 170.27, 'fmt': '170.27'}, 'regularMarketChangePercent': {'raw': -0.7662056, 'fmt': '-0.77%'}, 'fullExchangeName': 'NasdaqGS', 'tradeable': True}}, 'mktmData': {}}]



def get_stats(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
    querystring = {"region":"US","symbol": stock.upper()}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = json.loads(response.text)
    #print(response.text)
    financials.append(response_json)
    print(financials)

def get_financials(financials):

    #Dict keys
    pricing = financials[0]['price']
    keyStatistics = financials[0]['defaultKeyStatistics']
    financialData = financials[0]['financialData']
    summary = financials[0]['summaryDetail']

    #Company, Current Price, and Earnings
    name = pricing['shortName']
    price = pricing['regularMarketPrice']['raw']
    market_cap = pricing['marketCap']['fmt']
    trailing_EPS = keyStatistics['trailingEps']['raw']
    trailing_PE = summary['trailingPE']['fmt']
    forward_PE = keyStatistics['forwardPE']['raw']
    peg_ratio = keyStatistics['pegRatio']['raw']

    #Ratios
    book_value = keyStatistics['bookValue']['raw']
    foward_EPS = keyStatistics['forwardEps']['raw']
    profit_margins = keyStatistics['profitMargins']['raw']
    price_to_book = keyStatistics['priceToBook']['raw']
    beta = keyStatistics['beta']['raw']


    #Financials
    profit_margins = financialData['profitMargins']['fmt']
    operating_cashflow = financialData['operatingCashflow']['fmt']
    revenue_growth = financialData['revenueGrowth']['fmt']
    target_lowPrice = financialData['targetLowPrice']['raw']
    free_cashflow = financialData['freeCashflow']['fmt']
    earnings_growth = financialData['earningsGrowth']['fmt']
    current_ratio = financialData['currentRatio']['raw']
    debt_to_equity = financialData['debtToEquity']['raw']

    #Dividends
    dividend_rate = summary['dividendRate']['raw']
    dividend_yield = summary['dividendYield']['fmt']
    five_year_div_yield = summary['fiveYearAvgDividendYield']['fmt']



get_financials(financials)


#Need Following:
# DefaultKeyStatistics - Book Value, forwardEPS, profitmargins
# FundFamily - trailingEPS, pricetobook, beta,
# LegalType - pegRatio, forwardPE
# Price - regularMarketOprn(OPENING PRICE) #currency - regularMarketPrice #underlyingSymbol - marketCap
# FinancialData - profitMargins, operatingCashflow, revenuegrowth, targetLowPrice, earningsGrowth, currentRatio, debttoEquity
# quoteType = longName
#summaryDetail = dividentRate, fiveYearAvgDividendYield