s = 'This is a string of words'
s.split()
'This     is     a      string       of        words.'.split()
#Folding as above only happens without arugment
s.split('i')
words = s.split()
for w in words: print(w)
new = '"'.join(words)
','.join(words)
#More documentation on string methods available at
#docs.python.org/py3k/library/stdtypes.html#string-methods

