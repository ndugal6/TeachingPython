
#item = ['December 23, 2015', 'Bread Gloves', 8.51] unpacked version below
date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]
print(name)

def drop_first_last(grades):
    first, *middle, last = grades
    #the *middle stores every value inside of grades except for the initial and final value
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([94, 42, 50, 20, 33, 90])
drop_first_last([100, 20, 100])