class Animal():

    def __init__(self):
        pass

    def Legs(self):
        print("I have 4 legs")
    def Fur(self):
        print("I have no fur")
    def Eyes(self):
        print("I have 2 eyes")

#Put the super/parent class inside the sub class' parenthesis during declaration
class Dog(Animal):
    def Fur(self):
        print("Dog's lovely fur that all humans should pet!")

    def Bark(self):
        print("Ruff!")

class Duck(Animal):
    def Legs(self):
        print("Duck's have 2 legs!")

    def Quack(self):
        print("Quack Quack Quack!")

    def Fur(self):
        super().Fur()
        print("Instead, Ducks have beautiful feathers")

def main():
    Fido = Dog()
    Donald = Duck()

    Fido.Eyes()
    Donald.Eyes()
    print("\n")
    Fido.Legs()
    Donald.Legs()
    print("\n")
    Fido.Fur()
    Donald.Fur()
    print("\n")
    Fido.Bark()
    Donald.Quack()

if __name__ == "__main__": main()
