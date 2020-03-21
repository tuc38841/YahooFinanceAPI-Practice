from request import get_stats
from request import get_financials
from classStock import Stock

#use stats and financial data from request.py

def value_stock():
    stock = input("Type stock ticker to evaluate: ")
    financials = get_stats(stock)
    stock_dict = get_financials(financials)
    return stock_dict


#Instantiate Stock object
stock = Stock(value_stock())
print(stock.name)


# Basic - Company, market cap, current price, book value

# Revenue - current total, growth

# Cashflow - operating cashflow, debt/liabilities, current ratio, total debt, debt to equity,

# Earnings, PE (trailing, current, forward), PEG, targets (low,mean,high), return on equity

# Profit - margin, growth, price to book

# Dividends - amount, yield, avg 5 year


