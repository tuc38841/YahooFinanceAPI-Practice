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
    financials.append(response_json)
    return financials

def get_financials(financials):

    stats_dict = {}

    #response_json keys
    pricing = financials[0]['price']
    key_statistics = financials[0]['defaultKeyStatistics']
    financial_data = financials[0]['financialData']
    summary = financials[0]['summaryDetail']

    #response_json keys list
    keys_list = [pricing, key_statistics, financial_data, summary]
    #Stats in each group
    pricing_stats = ['regularMarketPrice','marketCap']
    key_statisitics_stats = ['bookValue','priceToBook','beta','trailingEps','forwardEps','forwardPE','pegRatio']
    financial_data_stats = ['profitMargins','operatingCashflow','totalRevenue','revenueGrowth','targetLowPrice',
                            'targetMedianPrice','targetHighPrice','freeCashflow','freeCashflow','earningsGrowth',
                            'currentRatio','debtToEquity','returnOnEquity','totalDebt','quickRatio']
    summary_stats = ['dividendRate','dividendYield','fiveYearAvgDividendYield','trailingPE']

    #From Pricing dict
    for stat in pricing_stats:
        try:
            stats_dict[stat] = pricing[stat]['raw']
        except KeyError:
            stats_dict[stat] = 'N/A'

    #From key_statistics dict
    for stat in key_statisitics_stats:
        try:
            stats_dict[stat] = key_statistics[stat]['raw']
        except KeyError:
            stats_dict[stat] = 'N/A'

    #From financial_data dict
    for stat in financial_data_stats:
        try:
            stats_dict[stat] = financial_data[stat]['raw']
        except KeyError:
            stats_dict[stat] = 'N/A'

    #From Summary dict
    for stat in summary_stats:
        try:
            stats_dict[stat] = summary[stat]['raw']
        except KeyError:
            stats_dict[stat] = 'N/A'

    return stats_dict


#NEED TRY BLOCK OR SOME LOOP TO MONITOR IF FINANCIAL DICT HAS EMPTY KEY VALUE PAIRS