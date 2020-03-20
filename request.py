import json
import requests
import os

headers = {
    'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com',
    'X-rapidapi-key': os.environ.get("X_RAPIDAPI_KEY")
}


financials = []


def get_stats(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
    querystring = {"region":"US","symbol": stock.upper()}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = json.loads(response.text)
    #print(response.text)
    financials.append(response_json)

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


get_stats('AAPL')
get_financials(financials)
