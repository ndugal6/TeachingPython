from operator import attrgetter
class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    #This is called when the object is being printed
    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users = [
    User('Nick', 40),
    User('Taylor', 5),
    User('Andrew', 23),
    User('Lynn', 62),
    User('John', 31)
]
for user in users:
    print(user)

print("----------")
for user in sorted(users, key=attrgetter("name")):
    print(user)

print("----------")

for user in sorted(users, key=attrgetter('user_id')):
    print(user)