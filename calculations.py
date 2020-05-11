# with dividends
# without dividends

# with eps
# with - eps (no profit)


# FreeCashflow

def present_value(cashflow, cashflow_growth, terminal_growth, discount=0.1):
    years_out = [2,3,4,5,6]
    sum_of_present_value = 0
    cashflow_updated = cashflow
    terminal_year_cf = 0
    for year in years_out:
        cashflow_updated *= (1.0 + cashflow_growth) #(1.05 = 5%)
        present_value_at_year_i = (cashflow_updated / (1.0 + discount)**(year-1))
        sum_of_present_value += present_value_at_year_i
        if year == years_out[-1]:
            terminal_year_cf += cashflow_updated * (1.0 + cashflow_growth)
    terminal_value = terminal_year_cf / ((1.0 + discount) - (1.0 + terminal_growth))
    terminal_present_value = terminal_value / (1.0 + discount)**(len(years_out))
    all_present_values = sum_of_present_value + terminal_present_value
    return all_present_values

def equity_value(present_values, cash, short_invest, long_invest, debt, shares):
    net_debt = (cash + short_invest + long_invest) - debt
    equity_per_share = (present_values + net_debt) / shares
    return equity_per_share



#test = present_value(46089, 0.05, .04)

#***in total sum of Present Values + PV of terminal

# all_present_values + (assets - liabilities) then divide by shares outstanding
# assets: cash/cash eq + shorterminvestments + longterminvestments (investments and advances)
# divide by shares outstanding
