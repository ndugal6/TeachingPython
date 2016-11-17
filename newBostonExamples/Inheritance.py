class Parent():

    def print_last_name(self):
        print('Dugal')


#Putting class inside parenthesis allows inheritance
class Child(Parent):

    def print_first_name(self):
        print('Nick')

    #Overriding, gives me a new last name, Run then comment this out and run again to see dif
    def print_last_name(self):
        print('Snitzleberg')

nicky = Child()
nicky.print_first_name()
nicky.print_last_name()