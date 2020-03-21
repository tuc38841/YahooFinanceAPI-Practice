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

    #Company, Current Price, and Earnings
    stats_dict['name'] = pricing['shortName']
    stats_dict['price'] = pricing['regularMarketPrice']['raw']
    stats_dict['market_cap'] = pricing['marketCap']['fmt']
    stats_dict['trailing_EPS'] = key_statistics['trailingEps']['raw']
    stats_dict['forward_EPS'] = key_statistics['forwardEps']['raw']
    stats_dict['trailing_PE'] = summary['trailingPE']['raw']
    stats_dict['forward_PE'] = key_statistics['forwardPE']['raw']
    stats_dict['peg_ratio'] = key_statistics['pegRatio']['raw']

    #Ratios
    stats_dict['book_value'] = key_statistics['bookValue']['raw']
    stats_dict['price_to_book'] = key_statistics['priceToBook']['raw']
    stats_dict['beta'] = key_statistics['beta']['raw']
    stats_dict['quick_ratio'] = financial_data['quickRatio']['raw']

    #Financials
    stats_dict['profit_margins'] = financial_data['profitMargins']['fmt']
    stats_dict['operating_cashflow'] = financial_data['operatingCashflow']['fmt']
    stats_dict['total_revenue'] = financial_data['totalRevenue']['raw']
    stats_dict['revenue_growth'] = financial_data['revenueGrowth']['fmt']
    stats_dict['target_lowPrice'] = financial_data['targetLowPrice']['raw']
    stats_dict['target_medianPrice'] = financial_data['targetLowPrice']['raw']
    stats_dict['target_highPrice'] = financial_data['targetHighPrice']['raw']
    stats_dict['free_cashflow'] = financial_data['freeCashflow']['fmt']
    stats_dict['earnings_growth'] = financial_data['earningsGrowth']['fmt']
    stats_dict['current_ratio'] = financial_data['currentRatio']['raw']
    stats_dict['debt_to_equity'] = financial_data['debtToEquity']['raw']
    stats_dict['return_on_equity'] = financial_data['returnOnEquity']['raw']
    stats_dict['total_debt'] = financial_data['totalDebt']['fmt']

    #Dividends
    stats_dict['dividend_rate'] = summary['dividendRate']['raw']
    stats_dict['dividend_yield'] = summary['dividendYield']['fmt']
    stats_dict['five_year_div_yield'] = summary['fiveYearAvgDividendYield']['fmt']

    return stats_dict

print(get_stats('sq'))