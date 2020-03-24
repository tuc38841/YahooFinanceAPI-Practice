class Stock:
    def __init__(self, stats_dict):
        self.name = stats_dict['name']
        self.price = stats_dict['regularMarketPrice']
        self.market_cap = stats_dict['marketCap']
        try:
            self.trailing_EPS = stats_dict['trailingEps']
        except KeyError:
            self.trailing_EPS = 'N/A'
        try:
            self.trailing_PE = stats_dict['trailingPE']
        except KeyError:
            self.trailing_PE = 'N/A'
        try:
            self.forward_PE = stats_dict['forwardPE']
        except KeyError:
            self.forward_PE = 'N/A'
        self.peg_ratio = stats_dict['pegRatio']
        self.book_value = stats_dict['bookValue']
        try:
            self.forward_EPS = stats_dict['forwardEps']
        except KeyError:
            self.forward_EPS = 'N/A'
        self.price_to_book = stats_dict['priceToBook']
        self.beta = stats_dict['beta']
        self.quick_ratio = stats_dict['quickRatio']
        self.profit_margins = stats_dict['profitMargins']
        self.operating_cashflow = stats_dict['operatingCashflow']
        self.total_revenue = stats_dict['totalRevenue']
        self.revenue_growth = stats_dict['revenueGrowth']
        self.target_lowPrice = stats_dict['targetLowPrice']
        self.target_medianPrice = stats_dict['targetMedianPrice']
        self.target_highPrice = stats_dict['targetHighPrice']
        self.free_cashflow = stats_dict['freeCashflow']
        self.earnings_growth = stats_dict['earningsGrowth']
        self.current_ratio = stats_dict['currentRatio']
        self.debt_to_equity = stats_dict['debtToEquity']
        self.return_on_equity = stats_dict['returnOnEquity']
        self.total_cash = stats_dict['totalCash']
        self.total_debt = stats_dict['totalDebt']
        self.dividend_rate = stats_dict['dividendRate']
        self.dividend_yield = stats_dict['dividendYield']
        self.five_year_div_yield = stats_dict['fiveYearAvgDividendYield']
