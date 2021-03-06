#Strings
   **Either single or double quotes:**

    print(‘Single quote’) 
    print(“Double quotes”)

**For Quotes inside of quotes, use the opposite:**

    Right: print(“He’s a great guy”) -> He’s a great guy
    Wrong: print(‘He’s a great guy’) -> Error 
    Right: print(‘She said, “Hello”’) -> She said, “Hello”
    
   **For same style quotes within each other: use \ to escape character**
>print(‘She said, “he\’s a great guy”’) - > She  said, “he’s a great guy”

**Escape Character \ : Using ‘\’ indicates special meaning, could be problematic:**
	
* \n = newline 
* \t = tab
* \b = backspace
* \a = alert/bell
* \v = vertical tab
* \e = escape
* \s = space
* \r = return
 
 **Example issue** *printing a file path*  

    print(‘C:\HDD\Users\Nick’) -> C:\HDD\Users
	                              ick
>Solve by using ‘r’ : means print raw string

    print(r’C:\HDD\Users\Nick’) -> C:\HDD\Users\Nick

#####Multiplying strings:
>name = "Nick"  
>print(nick * 5) -> Nick Nick Nick Nick Nick

#####Length of String
>length : len("hello") -> 5
	
#####Concatenation:   
* use the '+' operator 
>print(“You can do this” + “withoutfail”)  

	Doesn’t add implicit space between objects
	Doesn’t work for Strings with Ints or Floating ploints  
>~~print(“You can’t do this”+5)~~
* **Use a comma,** 
    
>print(‘the comma adds a’,’space’)  
>print(‘you can use integers’,5)
___
###Slicing
>user = "Bacon King"  
user[0] -> B   
user[6] -> K  
user[10] -> g  
user[-1] -> g  
user[:7] -> Bacon K  
user[6:9] -> Kin  
user[6:] -> King  
user[:] -> Bacon King  
___

###Math
| Math   |      Expression      | 
|----------|:-------------:|
| Add |  4 + 5 |
| Subtract  |    5 - 4|
| Multiply | 5 * 4 |
| Floor Division | 5 // 4 |
| Division | 5 / 4 |
| Tuple(FloorDiv, mod) | divmod(5,4) |
| Mod | 5%4 |
| Exponent | 5 ** 4 |
**Order of Operations: see file attatched** 
___
##List
players = [4, 10, 62, 99]  
players[2] = 62  
players[2] = 5  
***Adding Items:***  
players + [50, 27, 34] -> 4, 10, 62, 99, 50, 27, 34  
--Temporary, ***Store to new list if you want to keep***   
players.append(29) --permanently changes the list   

Can also slice using the ':' like in Strings  
players[:2]  
players[:2] = [4,5] //Replaces the first two values  
players[:2] = [] //Removes first two elements  
___
###If, elif
age = 20  
>if age < 21:    
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Can't buy beer")  
name = "Lucy"  
if name is "John":  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("hello John")  
elif name is "Lucy":  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("what up Lucy")  
else:  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("who are you?")  
___
###For
foods = ['bacon', 'eggs', 'snausages', 'toast']  
for f in foods:  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f)  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(len(f))  
	
**Can also slice this**  
for f in foods[:2]  
	   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f)
___
###Range, while
for x in range(10): //x goes from 0 to 9  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  print('this is awesome')  

for x in range(5,12): //x goes from 5 to 11  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(x)  
	
for x in range(20, 50, 5): //x goes 20 to 50 in increments of 5    
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(x)  
x = 5  
while x < 10:  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(x)  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x += 1  
____
###Comments and Break
Single line comments use #  
\#this is a comment  
Block, multiline comments(IDE SPECIFIC FOR PYTHON...I think?), use ...  
...
ignores all the 
lines of code until the 
next
...

magicNum = 26  
\#searches for magicNumber and stops when it's found  
for n in range(101):  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if n is magicNum:  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(n, ' is the magic number')  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break #says skip remainder of loop and exit  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(n)  

***Prints only the numbers that are available***  
numbersTaken = [2, 15, 4, 9, 11]  
print('Here are the numbers that are still available')  
for n in range(1,20):  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if n in numbersTaken:    
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue #says skip everything after this word and start next loop iteration  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(n)





____
###Functions: 
***Declare with 'def', anything after the ':' is part of the function***  
def beef():  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('functions are cool')  
Use function by calling it:
beef()

***Parameters/Arguments declared inside of parenthesis***  
def bitcoin_to_USD(btc):  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;amount = btc * 527  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(amount)  
******Use function by calling it with required parameter******  
bitcoin(3.85) #Prints the usd value of 3.85 bitcoin  

**Return Values:**   
def allowed_dating_age(my_age):  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;girls_age = my_age/2 + 7  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return girls_age    
nicks_limit = allowed_dating_age(21)  
print("Nick can date girls ", nicks_limit, "or older")    
******Remember that you must use commas for concatenating strings with integers******  
  ***... Unless***: You  cast the int to a string using str()  
   number = 10  
   print("this number is " + str(number))
__________
####Default Values for Arguments
def get_gender(sex='Unknown'):  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if sex is 'm':  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sex = 'Male'  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif sex is 'f':  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sex = 'Female'  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(sex)  
get_gender('m')  
get_gender('f')  
get_gender()  
____
**Variable Scope**  
a = 7823  
def corn():  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(a)  
def fudge():  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(a)  
corn()  
fudge()  
**Variable a** declare **outside** of functions, so both functions can use it.***   
**However**, if a variable is declared **inside** function (or loop) then it **can't be accessed outside** of # it's environment  

def corn():  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a = 7823  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(a)  
def fudge():  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(a)  
corn()  
fudge() #throws error since fudge can't see the variable a  
___
###Keyword Arguments
    def dumb_sentence(name='Nick', action='ate', item='tuna'):  
	    print(name, action, item)  
    dumb_sentence('Sally', 'farts', 'gently')  
***Python reads the arguments in order, setting name = 'Sally', action = 'farts', item = 'gently'***

But what if you want them *out of order*? No fear. Just tell python which are which
   
    dumb_sentence(item='awesome')  
    dumb_sentence(item='awesome', action='is')  

**Flexible Amount of Arguments:**  
Ex: you want to add k amount of numbers but don't know the value of k  
***Use an asterisk***, * tells python you're taking a bunch of arguments, but don't know how many, so store them all in the variable args  
def add_numbers(*args):
(could be named anything but it's standard for python #programmers to always name the flexible argument parameter as args)    

	total = 0
	for a in args:
		total += a
	print(total)
    add_numbers(3)
    add_numbers(3, 32)
    add_numbers(3, 43, 5453, 3483948, 23)
___
**Unpacking Arguments**  

    def health_calculator(age, apples_ate, cigs_smoked):
	    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
	    print(answer)
    nicks_data = [21, 12, 0]

    health_calculator(nicks_data[0], nicks_data[1], nicks_data[2])
    health_calculator(*nicks_data) #astericks unpacks the list and passes all values as arguments

___


###Sets 
Think of as a collection of items, but can't have duplicates - unlike lists  
Sets declared with { }  

    groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'lotion', 'beer'}
    print(groceries) #Notice that beer is only printed once

    if 'milk' in groceries:
	    print('You already have milk')
    else:
	    print('You need milk')
___	
###Dictionary: key & value:   
_dictionary = {key:value, key:value}_  

    classmates = {'Tony': 'cool but smells', 'Sally':'asks too many questions','Emma':'sits behind me'}
    print(classmates)
    print(classmates['Emma'])
***loop through and print***  
***k is the key and v is the value***

    for k, v in classmates.items():
	    print(k + v)
##Modules
***Init***

    def __init(self)__ {
        print("hello")
    }
    
#Breakkkkkkkkkkkkk (More in depth)
#-----------------------------------------------------
>Open python3 idle  
>import sys  
sys.executable   
Use file path

**Tuple**  

    x = (1, 2, 3, 4, 5)  
    print(type(x), x)  
***Tuple is immutable***
 

**List**
  
    x = [1, 2, 3, 4, 5]  
    print(type(x), x)  
    x.append(5)  
    x.insert(0, 6)  

**Dictionary:**

    d = {‘one’: 1, ‘two’: 2, ‘three’: 3}  
    for k in d:  
	    print(k, d[k])  
    for k in sorted(d.keys()):  
	    print(k, d[k])  

**also:**  

    d = dict(  
	    one = 1, two = 2, three = 3, four = 4, ‘five = ‘five’  
    )  
    d[‘seven’] = 7  
    print(d[‘seven’])  
**what if not there:**  
print(d[‘eight’])  
Error: Say:  
print(d.get(‘eight’, ‘Not in the dictionary’))  

**Finding the type and identity of an object**
  
    x = 42  
    id(42)  
    type(42)  

    id(x)  
    type(x)  

    y = 42  
    id(y)  
    y == x //Compares values for boolean  
    y is x //Compares ids for values   

    x = dict(x = 42)  
    type(x)  
    id(x)  

    y = dict(x = 42)  
    id(y)  


**Boolean Objects**  
a, b = 0, 1  
a==b  

a < b  

a > b  

a = True  
type(a)  
id(a)  
id(True)  
(Id is used to check if object are exactly the same, == is used to check if values are the same)   
**If, Else**
  
    a, b = 0, 1  
    v = ‘this is true’ if a < b else ‘this is false’  
    print(v)  


**Find at what index a value exist**
  
    s = ’this is a string’  
    for i, c in enumerate(s):  
	    #print(i, c)  
	    if (c == ’s’): print(“index {} is an s”.format(i))  

**Loop Control:**  

    s = ’this is a string’  
    for c in s:  
	    if (c == ’s’): continue  
	    print(c, end=‘ ‘)  
    for c in s:  
	    if (c == ’s’): break  
	    print(c, end=‘ ‘)    
    for c in s:  
	    print(c, end=‘ ‘)  
    else: //When the for statement is completely false aka out of stuff to iterate  
	    print(‘else’)  


    s = ’this is a string’  
    i = 0  
    while(i < len(s)):  
	    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(s[i], end=‘ ‘)  
	    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i += 1  
    else:   
	    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(‘else’)  

____
**Simple Arithmetic:**  
5 - 5  
5 + 5  
5 * 5  
5 ** 5  
12 / 5  
12 // 5 #floor division  
12 % 5 #Mod  
divmod(12, 5) #Returns tuple with floor div and mod  

num = 5  
num += 5  
num -= 5  
num *= 5  
num /= 5  
num //= 5  

___
**Operators on bitwise values**  
0b101 -> 5  
def b(n): print(‘{:08b}’.format(n))  
x, y= 0x55, 0xaa  
b(x)  
b(y)  
b(x | y) Or  
b(x & y) And  
b(x ^ y) Exclusive or  
b(x ^ 0)  
b (x << 4) Left shift  
b(x >> 4) Right shift  
b(~x) One complement operator  

**Comparing values:**  
\ >, <, >=, <=, ==, !=,   
is and is not test the id, good for immutable, mutable not so much(such as list)
Good to know if objects are exactly the same
___
**Operating on booleans**  
x = True  
print(type(x))  
**comparing booleans**  
True and False  
True and True  
True or False  
False or False   
True & True #WRONG does bitwise comparison  

    Ex:  
    a, b = 0, 1  
    x, y = ‘zero’, ‘one’  
    x < y  
    a < b  
    if a < b and x < y: print(“yes”)  
    else: print(“yes”)  
___
####Operating on parts of a container with the slice operator  

    list = []    
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    list[0] #first element starts at 0    
    list[0:5]  
    for i in range(0,10)  
	    print(i)  
    list[0:10]  
    list[:] = range(100)  
    list[27]  
    #Slice: first argument is starting point, 2nd is exclusive end, 3rd is step by  
    list[27:43]  
    list[27:43:3]  
    for i in list[27:43:3]: print(i)  
  
    list[27:43:3] = (99,99,99,99,99,99)  

**Operator precedence:**  
5 * 25 + 14 / 2 #Same as math  
5 * (25 + 14) / 2  Yo Nick, you attatched a file for this

___
**Regular Expression:** Looks for patterns or replaces patterns  
Used in python with the re module  

    fh = open(‘Raven.txt’)  
    for line in fh:  
        match = re.search(‘(Len|Nev)more’, line)  
    if match:  
        print(match.group())  
**To search and replace, use sub instead of search**  

    fh = open(‘Raven.txt’)  
    for line in fh:  
        print(re.sub(‘(Len|Neverm)ore’, ‘###’, line), end=‘ ‘)  

    for line in fh:  
        match = re.search(‘(Len|Neverm)ore’, line)  
        if match:  
            print(line.replace(match.group(), ‘###’), end=‘ ‘)  
**Precompiling regular expression to use over again**  

    pattern = re.compile(‘(Len|Neverm)ore’, re.IGNORECASE)  
    for line in fh:  
        if re.search(pattern, line):  
        #print(line, end=‘’)  
    print(pattern.sub(‘###’, line), end=‘’)  

**Exceptions:**  
***Expirations are the key method of handling errors in Python***  
“try” something, then catch an exception with “except”
raise own exceptions with “raise”  

    def main():  
    try:  
        fh = open(‘line.txt’)  
        for line in fh: print(line.strip())  
    #except:
    except IOError as e:  
        print(‘could not open the file:’, e)    
    else:  
        for line in fh: print(line.strip())  
**Raising Exceptions:**  

    def main():  
    try:  
        for line in readfile(‘lines.txt’): print(line.strip())  
    except IOError as e:  
        print(‘cannot read file:’, e)  
    except ValueError as e:    
        print(‘bad filename’, e)  

    def readfile(filename):  
        if filename.endswith(‘.txt’):  
            fh = open(filename)  
            return fh.readlines()  
        else: raise ValueError(‘Filename must end with .txt’)  


___

**Defining functions:**

    def main():  
        testfunc(42, 16)  

    #def testfunc(number, another = 43, onemore = 75):  
        #print(‘This is a test function’, number, another, onemore)    

    def testfunc(number, another = None, onemore = 75):  
        if another is None:  
            another = 112  
        print(‘This is a test function’, number, another, onemore)    
___
**Arbitrary amount of argument**  

    def main():  
        testfunc(1, 2, 3,42, 43, 45, 46)  

    def testfunc(this, that, other, *args):  
        print(this, that, other, args) #args is a tuple  
        for n in args: print(n, end=‘ ‘)

Passing named arguments from caller    

    def main():  
        testfunc(one = 1, two = 2, four = 42)  
    testfunc(5, 6, 7, 8, 9, 10one = 1, two = 2, four = 42) 
     
    #specified arguments, then tuple argument, then keyword arguments  
    
    def testfunc(this, that, other, *args, **kwargs):  
        print(‘This is a test function’,  
            this, that, other, args,  
            kwargs[‘one’], kwargs[‘two’], kwargs[‘four’])  
        for k in kwargs: print(k, kwargs[k])
___
**RETURNING VALUES FROM FUNCTIONS:**  
    
    def main():  
        print(testfun())  

    def testfunc():  
        return ‘This is a test function’ #Can return any type  
    def testfunc()  
        return range(25)  
    for n in testfunc(): print(n, end=‘ ‘)  
___
**GENERATOR**

    def main():  
        print(“this is the functions.py file.”)  
    for i in inclusive_range(0, 25, 1):  
        print(i, end=‘ ‘)  
    def inclusive_range(start, stop, step):  
        i = start  
        while i <= stop:  
            yield i  
            i += step  

___
**USE ALL WE LEARNED**  

    def main():  
        print(“this is the functions.py file.”)  
    for i in inclusive_range(25):  
        print(i, end=‘ ‘)  
    def inclusive_range(*args):  
        numargs = len(args)  
        if numargs < 1: raise TypeError(‘requires at least one argument’)  
        elif numargs == 1:  
            stop = args[0]  
            astart = 0  
            step = 1  
        elif numargs == 2:  
            (start, stop) = args  
            step = 1  
        elif numargs == 3:  
            (start, stop, step) = args  
        else: raise TypeError(‘inclusive_range expected at most 3 arguments, got {}’.format(numargs))  
        i = start  
        while i <= stop:  
            yield i  
            i += step  
___
**Constructor:**  

    class Duck:  
        def __init__(self, value):  
            self._v = value  
        def quack(self):  
            print(‘Quack!’, self._v)  
        def walk(self):  
            print(‘Walks like a duck,’, self._v)  
    def main():  
        donald = Duck(25)  
        frank = Duck(151)  
        donald.quack()  
        donald.walk()  
        frank.quack()  
        frank.walk()  
___
**Using Object Data: GETTER AND SETTER**  

    class Duck:  
        #def __init__(self, color = ‘white’):  
            #self._color = value  
        def __init__(self, **kwargs):  
            #self._color = kwargs.get(‘color’, ‘white’)  
            self.variable = kwargs


        def quack(self):  
            print(‘Quack!’, self._v)  
        def walk(self):  
            print(‘Walks like a duck,’, self._v)  

        def set_color(self, color):  
            #self._color = color  
            self.variable[‘color’] = color  
        def get_color(self):  
            #return self._color  
            return self.variable.get(‘color’, None)  

        def set_variable(self, k , v):  
            self.variable[k] = v  

        def get_variable(self, k):  
            return self.variables.get(k, None)  
    def main():  
        donald = Duck()  
        donald = Duck(color = ‘red’)  
        donald = Duck(feet = 2)  
        #print(donald._color)  
        print(donald.get_color())  
        #donald_coor = ‘blue’  
        donald.set_color(‘blue’)  
        print(donald.get_color)  
___
##Inheritence  
    class Animal:  
        def talk(self): print('Hey, I have something to say')  
        def walk(self): print('Ay, I'm walking here')  
        def clothes(self): print('I have nice clothes')  

    class Duck(Animal):  
        def quack(self):  
            print('Quack like a duck')  
        def walk(self):   
            super().walk()  
            print('Walk like a duck')  

    class Dog(Animal):  
        pass


    def main:  
        donald = Duck()  
        donald.walk()  
        donald.quack()  
___
##Polymorphism: 
 **using object of one cass as another class**  
    class Duck:  
def quack(self):  
print('Quaaack!')


  def walk(self):  
print('Walks like a duck.')

class Dog(Animal):    
  def bark(self):   
print('Woof!')  
def fur(self):    
print('the dog has white fur')


def main():  
donald = Duck()  
donald.quack()  
donald.walk()    
fido = Dog()  


#Duck Typing (poly morph vid)

