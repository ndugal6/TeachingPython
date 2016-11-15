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

####Multiplying strings:
>name = "Nick"  
>print(nick * 5) -> Nick Nick Nick Nick Nick

####Length of String
>length : len("hello") -> 5
	
###Concatenation:   
* **use the '+' operator** 
>print(“You can do this” + “withoutfail”)  

	Doesn’t add implicit space between objects
	Doesn’t work for Strings with Ints or Floating ploints  
>~~print(“You can’t do this”+5)~~
* **Use a comma,** 
    
>print(‘the comma adds a’,’space’)  
>print(‘you can use integers’,5)
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

###Math
Add 				4 + 5  
Subtract 			5-4   
Multiply 			10 * 2  
Exponent	 		10 ** 2  
Division 			9 / 4  
Rounded Division (Down) 	9 // 4  
Mod				 9%4  
Order of OP			2 + 4 * 3  

###List
players = [4, 10, 62, 99]  
players[2] = 62  
players[2] = 5  
**Adding Items:**  
players + [50, 27, 34] -> 4, 10, 62, 99, 50, 27, 34  
--Temporary, **Store to new list if you want to keep**   
players.append(29) --permanently changes the list   

Can also slice using the ':' like in Strings  
players[:2]  
players[:2] = [4,5] //Replaces the first two values  
players[:2] = [] //Removes first two elements  

###If, elif
age = 20  
>if age < 21:    
  print("Can't buy beer")
name = "Lucy"
if name is "John":
	print("hello John")
elif name is "Lucy":
	print("what up Lucy")
else:
	print("who are you?")

for
foods = ['bacon', 'eggs', 'snausages', 'toast']
for f in foods:
	print(f)
	print(len(f))
Can also slice this
for f in foods[:2]
	print(f)

Range, while
for x in range(10): //x goes from 0 to 9
	print('this is awesome')
for x in range(5,12): //x goes from 5 to 11
	print(x)
for x in range(20, 50, 5): //x goes 20 to 50 in increments of 5
	print(x)
x = 5
while x < 10:
	print(x)
	x += 1
Comments and Break
Single line comments use #
#this is a comment 
Block, multiline comments, use ...
...
ignores all the 
lines of code until the 
next
...

magicNum = 26
#searches for magicNumber and stops when it's found
for n in range(101):
	if n is magicNum:
		print(n, ' is the magic number')
		break #says skip remainder of loop and exit
	else:
		print(n)

#Prints only the numbers that are available
numbersTaken = [2, 15, 4, 9, 11]
print('Here are the numbers that are still available')
for n in range(1,20):
	if n in numbersTaken:
		continue #says skip everything after this word and start next loop iteration
	print(n)






Functions: Declare with 'def', anything after the ':' is part of the function
def beef():
	print('functions are cool')
Use function by calling it:
beef()

Parameters/Arguments declared inside of parenthesis
def bitcoin_to_USD(btc):
	amount = btc * 527
	print(amount)
Use function by calling it with required parameter
bitcoin(3.85) #Prints the usd value of 3.85 bitcoin

Return Values: 
def allowed_dating_age(my_age):
	girls_age = my_age/2 + 7
	return girls_age
nicks_limit = allowed_dating_age(21)
print("Nick can date girls ", nicks_limit, "or older")
#Remember that you must use commas for concatenating strings with integers

Default Values for Arguments
def get_gender(sex='Unknown'):
	if sex is 'm':
		sex = 'Male'
	elif sex is 'f':
		sex = 'Female'
	print(sex)
get_gender('m')
get_gender('f')
get_gender()

Variable Scope
a = 7823
def corn():
	print(a)
def fudge():
	print(a)
corn()
fudge()
#Variable a declare outside of functions, so both functions can use it. 
#However, if a variable is declared inside function (or loop) then it can't be accessed outside of # it's environment

def corn():
	a = 7823
	print(a)
def fudge():
	print(a)
corn()
fudge() #throws error since fudge can't see the variable a

Keyword Arguments
def dumb_sentence(name='Nick', action='ate', item='tuna'):
	print(name, action, item)
dumb_sentence('Sally', 'farts', 'gently')
#Python reads the arguments in order, setting name = 'Sally', action = 'farts', item = 'gently'

# But what if you want them out of order? No fear. Just tell python which are which 
dumb_sentence(item='awesome')
dumb_sentence(item='awesome', action='is')

Flexible Amount of Arguments:
Ex: you want to add k amount of numbers but don't know the value of k
#Use an asterisk *, tells python you're taking a bunch of arguments, but don't know how many # so store them all in the variable args(could be named anything but it's standard for python #programmers to always name the flexible argument parameter as args)
def add_numbers(*args):
	total = 0
	for a in args:
		total += a
	print(total)
add_numbers(3)
add_numbers(3, 32)
add_numbers(3, 43, 5453, 3483948, 23)

Unpacking Arguments
def health_calculator(age, apples_ate, cigs_smoked):
	answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
	print(answer)
nicks_data = [21, 12, 0]

health_calculator(nicks_data[0], nicks_data[1], nicks_data[2])
health_calculator(*nicks_data) #astericks unpacks the list and passes all values as arguments




Sets: Think of as a collection of items, but can't have duplicates - unlike lists
	#Sets declared with { }
groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'lotion', 'beer'}
print(groceries) #Notice that beer is only printed once

if 'milk' in groceries:
	print('You already have milk')
else:
	print('You need milk')
	
Dictionary: key & value:   dictionary = {key:value, key:value}
classmates = {'Tony': 'cool but smells', 'Sally':'asks too many questions','Emma':'sits behind me'}
print(classmates)
print(classmates['Emma'])
#loop through and print
#k is the key and v is the value
for k, v in classmates.items():
	print(k + v)

##Modules
