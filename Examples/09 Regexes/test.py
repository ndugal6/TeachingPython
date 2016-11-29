import re
here = dict(
    key = 1, five = 2)
d = {'ey':1, 'hey':2}
for he in here:
    print(he)

a, b = 0, 1
v = 'this is true' if a < b else 'this is false'



print(v)
s = "this is a string"
for i, c in enumerate(s):
    print(i, c)
    if (c == "s"): print("index {} is an s".format(i))
list = []
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list[0] #first element starts at 0
list[0:5]
for i in range(0,10):
    print(i)
list[0:10]
list[:] = range(100)
list[27]
#Slice: first argument is starting point, 2nd is exclusive end, 3rd is step by
list[27:43]
list[27:43:3]
for i in list[27:43:3]: print(i)

list[27:43:3] = (99,99,99,99,99,99)

fh = open('raven.txt')
for line in fh:
    match = re.search('(Len|Nev)more', line)
    if match:
        print(match.group())

s = 'this is a string'
for c in s:
    if (c == 's'): continue
    print(c, end=' ')
print('break')
for c in s:
    if (c == 's'): break
    print(c, end=' ')
print('nothing')
for c in s:
    print(c, end=' ')
else: #When the for statement is completely false aka out of stuff to iterate
    print('else')