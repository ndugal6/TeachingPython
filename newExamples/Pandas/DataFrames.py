# Making dataframes frmo series objects, python dicts, and Numpy arrays
# Setting Indexes
# Selecting, combining, and creating columns
# Performing relational joins on DataFrames

import  pandas as pd
pop2014 = pd.Series([100,99,95.5,93.5, 92.4, 84.8, 84.5,78.9,74.3, 72.8],
                    index=['Java', 'C', 'C++','Python', 'C#', 'PHP', 'JavaScript','Ruby','R','MatLab'])

pop2015 = pd.Series([100,99.9,99.4,96.5, 91.3, 84.5, 83.0,76.2,84.8, 72.4],
                    index=['Java', 'C', 'C++','Python', 'C#', 'PHP', 'JavaScript','Ruby','R','MatLab'])

twoyears = pd.DataFrame({'2014':pop2014, '2015':pop2015})
print(twoyears)

twoyears = twoyears.sort('2015', ascending=False)
print(twoyears)

print(twoyears.index)
print(twoyears.columns)

twoyears['2014']

twoyears.iloc[0:2]

twoyears.loc['C':'Python']

twoyears['avg'] = 0.5*(twoyears['2014'] + twoyears['2015'])

print(('-'*50 + '\n')*2)
print(twoyears)