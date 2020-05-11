import json
import requests
import os

headers = {
    'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com',
    'X-rapidapi-key': os.environ.get("X_RAPIDAPI_KEY")
    }

financials = []
balance_sheet = []

def get_financials(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
    querystring = {"region":"US","symbol": stock.upper()}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = json.loads(response.text)
    financials.append(response_json)
    return financials

def get_balance_sheet(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-balance-sheet"
    querystring = {"symbol": stock.upper()}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = json.loads(response.text)
    balance_sheet.append(response_json)
    return balance_sheet


def get_data(financials, balance_sheet):
    stats_dict = {}

    # response_json keys
    pricing = financials[0]['price']
    key_statistics = financials[0]['defaultKeyStatistics']
    financial_data = financials[0]['financialData']
    summary = financials[0]['summaryDetail']
    balance_quarterly = balance_sheet[0]['balanceSheetHistoryQuarterly']['balanceSheetStatements'][0]

    # Stats in each group
    pricing_stats = ['regularMarketPrice','marketCap']
    key_statistics_stats = ['bookValue','priceToBook','beta','trailingEps','forwardEps','forwardPE','pegRatio',
                            'sharesOutstanding','beta']
    financial_data_stats = ['profitMargins','operatingCashflow','totalRevenue','revenueGrowth','targetLowPrice',
                            'targetMedianPrice','targetHighPrice','freeCashflow','earningsGrowth',
                            'currentRatio','debtToEquity','returnOnEquity', 'totalCash','totalDebt','quickRatio']
    summary_stats = ['dividendRate','dividendYield','fiveYearAvgDividendYield','trailingPE']
    balance_stats = ['cash','longTermInvestments','shortTermInvestments',]

    # Lists of keys and stats
    keys_list = [pricing, key_statistics, financial_data, summary, balance_quarterly]
    stats_list = pricing_stats + key_statistics_stats + financial_data_stats + summary_stats + balance_stats

    # Create dict for stats to obtain
    stats_dict['name'] = pricing['shortName']
    for key in keys_list:
        for stat in stats_list:
            if stat in key.keys():
                try:
                    stats_dict[stat] = key[stat]['raw']
                except KeyError:
                    stats_dict[stat] = 0
    return stats_dict
