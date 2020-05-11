from request import get_financials
from request import get_balance_sheet
from request import get_data
from classStock import Stock
from calculations import present_value
from calculations import equity_value

# Use stats and financial data from request.py
def value_stock():
    stock = input("Type stock ticker to evaluate: ")
    financials = get_financials(stock)
    balance_sheet = get_balance_sheet(stock)
    stock_dict = get_data(financials,balance_sheet)
    return stock_dict

# Instantiate Stock object - passing in stock_dict to create attributes of stock
stock = Stock(value_stock())

# Basic - Company, market cap, current price, book value
print('---------------RESULTS---------------')
print(
    'Company:', stock.name, '\n'
    'Market Cap: ${:,}'.format(stock.market_cap), '\n'
    'Current Price: ${:}'.format(round(stock.price, 2)), '\n'
    'Target Prices\n'
    'Low:: ${:}'.format(round(stock.target_lowPrice, 2)), '\n'
    'Median: ${:}'.format(round(stock.target_medianPrice, 2)), '\n'
    'High: ${:}'.format(round(stock.target_highPrice, 2)), '\n'
)
# Revenue - current total, growth
print('REVENUE and PROFIT')
print(
    'Total Revenue (TTM): ${:,}'.format(stock.total_revenue), '\n'
    'Revenue Growth: %{:}'.format(round(stock.revenue_growth * 100, 2)), '\n'
    'Profit Margin: %{:}'.format(round(stock.profit_margins * 100, 2)), '\n'
)
# PE Ratio - Current and forward PE
print('PE RATIO and PRICE TO BOOK')
print(
    'PE Ratio:', (round(stock.trailing_PE, 2))
                        if isinstance(stock.trailing_PE, float) else 'N/A', '\n'
    'Forward PE:', (round(stock.forward_PE,2))
                        if isinstance(stock.forward_PE, float) else 'N/A', '\n'
    'Price to Book:', round(stock.price_to_book, 2), '\n'
)
# Cashflow - operating cashflow, debt/liabilities, current ratio, total debt, debt to equity,
print('CASHFLOW and LIABILITIES')
print(
    'Operating Cashflow: ${:,}'.format(stock.operating_cashflow), '\n'
    'Free Cashflow: ${:,}'.format(stock.free_cashflow), '\n'
    'Total Debt: ${:,}'.format(stock.total_debt), '\n'
    'Debt to Equity:', stock.debt_to_equity, '\n'
)
# Earnings, PE (trailing, current, forward), PEG, targets (low,mean,high), return on equity
print('EARNINGS')
print(
    'EPS: ${:}'.format(stock.trailing_EPS), '\n'
    'Forward EPS: ${:}'.format(stock.forward_EPS), '\n'
    'Earnings Growth: %{:}'.format(round(stock.earnings_growth * 100, 2)), '\n'
)
# Dividends - amount, yield, avg 5 year
print('DIVIDENDS')
print(
    'Dividend Rate:', stock.dividend_rate, '\n'
    'Dividend Yield: %{:}'.format(stock.dividend_yield * 100), '\n'
    'Five Year Dividend Average: %{:}'.format(stock.five_year_div_yield), '\n'
)
# Balance Sheet - Cash, short-term, and long-term investments
print('CASH AND INVESTMENTS')
print(
    'Cash: ${:,}'.format(stock.cash), '\n'
    'Short Term Investments: ${:,}'.format(stock.short_term_investments), '\n'
    'Long Term Investments: ${:,}'.format(stock.long_term_investments)
)


present_values = present_value(stock.free_cashflow, stock.revenue_growth, 0.04)
estimated_value = equity_value(present_values, stock.cash, stock.short_term_investments,
                               stock.long_term_investments, stock.total_debt, stock.shares_outstanding)
print('Present Value: ${:,}'.format(present_values))
print('Estimated Stock Value: ${:,}'.format(round(estimated_value),2))
# some companies may not have shortterm or longterm investment key
# - may have to adjust to assets - liabilities for those circumstances

# need to replace stock.revenue_growth with CASHFLOW growth
#in get_financiasl - totalCashFromOperatingActivities - capitalExpenditures = free cash flow
# then look at previous years (goes back 3-4) and determine average rate