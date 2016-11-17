first = ['Nick', 'Tom', 'Taylor']
last = ['Dugal', 'Hanks', 'Swift']

#Times two list together
names = zip(first,last)

#Shape is of names: [('Nick', 'Dugal'), ('Tom', 'Hanks'), ('Taylor', 'Swift')]

for a, b in names:
    print(a, b)