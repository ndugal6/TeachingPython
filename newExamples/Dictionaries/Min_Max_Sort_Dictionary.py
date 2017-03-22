stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZON': 306.21,
    'AAPL': 99.76
}
#can't sort a dictionary by default, but you can sort a zip
#zip is sorted by whichever list is given first upon zip init
print(min(zip(stocks.values(),stocks.keys())))

print(max(zip(stocks.values(),stocks.keys())))

print(sorted(zip(stocks.values(),stocks.keys())))

print(sorted(zip(stocks.keys(),stocks.values())))