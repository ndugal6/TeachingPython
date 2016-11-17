import heapq

grades = [32, 43, 654, 34, 132, 66, 99, 532]

#Gives 3 largest items in grades
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker' : 'AAPL', 'price': 201},
    {'ticker' : 'GOOG', 'price': 800},
    {'ticker' : 'F', 'price': 54},
    {'ticker' : 'MSFT', 'price': 313},
    {'ticker' : 'TUNA', 'price': 68},
]


#use lambda to sort custom class objects
print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))