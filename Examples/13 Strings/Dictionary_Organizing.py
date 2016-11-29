d = {'one':1, 'two':2, 'three':3}
d = dict(one = 1, two=2, three=3)
x = dict(four = 4, five = 5, size = 6)
d = dict(one = 1, two=2, three=3, **x)
'four' in d
'three' in x
for k in d: print(k)
for k,v in d.items(): print(k,v)
d['three']
d.get('three','None')
del x['four']
x.pop('five')


