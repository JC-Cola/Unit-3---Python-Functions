# Q1 Price Surge Alert
# 3
# 6700

# Q2 Wallet Preview
# 0x9F1aB3c

# Q3 Portfolio Value
def portfolio_value(holdings, prices):
    total_value = 0.0
    for symbol, shares in holdings.items():
        if symbol in prices:
            total_value += shares * prices[symbol]
    return round(total_value, 2)