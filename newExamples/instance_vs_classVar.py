class Girl:
    #Class variable gender. means all girl objects have gender of female
    gender = 'female'

    def __init__(self, name):
        #Instanec variable name is unique to each object of class Girl, unlike gender
        self.name = name

r = Girl('Rachel')
s= Girl("Stacey")
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)

