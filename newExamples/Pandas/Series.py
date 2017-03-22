# Making series objects from Python lists and dicts
# Extractiing indexes and values
# Indexing Series objects implicitly and explicitly

import pandas as pd

s = pd.Series([0,1,4,9,16,25], [0,1,2,3,4,5],dtype= 'float64', name='squares')
print(s)
print(s.index)
print(s[3:6])

pop2014 = pd.Series([100,99,95.5,93.5, 92.4, 84.8, 84.5,78.9,74.3, 72.8],
                    index=['Java', 'C', 'C++','Python', 'C#', 'PHP', 'JavaScript','Ruby','R','MatLab'])
print(pop2014)
print(pop2014[0])
print(pop2014['C++':'C#'])

print(s.iloc[0:2])

print(s[s > 4])

s2 = pd.Series(
    {'0':0, '1':1, '2':4,'3':9,'4':16,'5':25}
)

