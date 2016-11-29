squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)
squares = [x**2 for x in range(10 )]
print(squares)

square_tuples = [(x,y) for x in range(5) for y in (1,4,2) if x != y]
print(square_tuples)
#This is the same as below:

x = []
for i in range(5):
    for e in (1,4,2):
        if i != e:
            x.append((i,e))
print(x.sort())
x.reverse()
print(x)

#Flatten a list using 2 for in
vec = [[1,2,3],[4,5,6],[7,8,9]]
flattened_vec = [num for elem in vec for num in elem]
print(flattened_vec)

#transposing a matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)
#Equals
transposed.clear()
for i in range(4):
    transposed.append(row[i] for row in matrix)
print(transposed)

unpacked = list(zip(*matrix))
print(unpacked)
