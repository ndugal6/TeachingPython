from operator import itemgetter

users = [
    {'fname': 'Nick', 'lname': 'Dugal'},
    {'fname': 'Steve', 'lname': 'Dugal'},
    {'fname': 'Tom', 'lname': 'Hanks'},
    {'fname': 'Tyler', 'lname': 'Gettys'},
    {'fname': 'Jackie', 'lname': 'Chan'},
    {'fname': 'Steve', 'lname': 'Jobs'},
    {'fname': 'Julius', 'lname': 'Ceasar'},
    {'fname': 'Anne', 'lname': 'Hathaway'},
    {'fname': 'Steve', 'lname': 'Holt'},
    {'fname': 'TheyTookOur', 'lname': 'Jobs'}
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('-----------')
#first sort by first name, then sort further by last name
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)
