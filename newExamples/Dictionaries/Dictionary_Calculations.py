stocks = {
    'GOOG': 434,
    'AAPL': 325,
    'FB': 54,
    'AMZN': 623,
    'F': 32,
    'MSFT': 549,
}


#Gives the min Key, which is AAPL, instead of min Value
print(min(stocks))

#Reorganize with zip and boom. There ya go
min_price = min(zip(stocks.values(),stocks.keys()))
print(min_price)
