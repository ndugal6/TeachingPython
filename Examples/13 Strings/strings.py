#!/usr/bin/python3

def main():
    s = 'this Is A string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print('This is a string'.upper())
    print('This is a string {}'.format(42))
    print(s.swapcase())
    #returns first occurance
    print(s.find('is'))
    print(s.replace('this', 'that'))
    s = '        this is a string          '
    #Commonly used for removing used lines, but strip removes any white spcae before and after string
    print(s.strip())
    #Just remove white space from end of string, us .rstrip()
    print(s.rstrip())
    s1 = '   This is a string  \n'
    print(s1.rstrip('\n'))
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())

#String format methods

    a, b = 5, 42
    print(a, b)

#important to note that c is entirely neew string, string are immutable

    c = 'this is {}, that is {}'
    print(c.format(a,b))
    new = c.format(a,b)
    print(id(c))
    print(id(new))


#More formatting with Strings using Format
a, b = 40, 10
'This is {1}, that is {0}, this is also {1}'.format(a,b)
'this is {bob}, that is {fred}'.format(bob=a, fred=b)
d = dict(bob=a, fred=b)
'this is {bob}, that is {fred}'.format(**d)


if __name__ == "__main__": main()
