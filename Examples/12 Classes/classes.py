#!/usr/bin/python3


class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(selfself):
        print('The duck cannot bark')
    def fur(self):
        print('The duck has feathers')

class Dog:
        def bark(self):
            print('Woof!')
        def fur(selfself):
                print('The dog has brown and white fur')
        def walk(self):
            print('Walks like a dog')
        def quack(self):
            print('The dog cannot quack')


def main():
    donald = Duck()
    fido = Dog()

    #in-the_forest takes a duck object, but since dog has all methods, it can morph into needed obj and still works
    in_the_forest(donald)
    in_the_pond(fido)

    # for o in (donald, fido):
    #     o.quack()
    #     o.walk()
    #     o.bark()
    #     o.fur()

# def in_the_forest(dog):
#     dog.bark()
#     dog.fur()
def in_the_forest(cat):
    cat.bark()
    cat.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()






    # donald.quack()
    # donald.walk()
    #
    # fido = Dog()
    # fido.bark()
    # fido.fur()

if __name__ == "__main__": main()
