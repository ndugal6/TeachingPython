class Animal():
    def Legs(self):
        print("111 Animal Leg::I have 4 legs")
    def Fur(self):
        print("222 Animal Fur :I have no fur")
    def Eyes(self):
        print("333 Animal Eye:I have 2 eyes")

#Put the super/parent class inside the sub class' parenthesis during declaration
class Dog(Animal):
    def Fur(self):
        print("444 Dog Fur: Dog's lovely fur that all humans should pet!")

    def Bark(self):
        print("555 Dog Bark:Ruff!")

class Duck(Animal):
    def DuckLegs(self):
        print("666 Duck Leg:Duck's have 2 legs!")

    def Quack(self):
        print("777 Duck Quack:Quack Quack Quack!")

    def Fur(self):
        super().Fur()
        print("888 Duck Fur: Instead, Ducks have beautiful feathers")

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