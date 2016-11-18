class Mario():
    def move(self):
        print('I am moving!')

class Shroom():
    def eat_shroom(self):
        print('Now I am big!')

#Inherits from both class

class BigMario(Mario, Shroom):
    pass

#use keyword 'pass' when you don't need to write anything - avoids syntax errors

bm = BigMario()
bm.move()
bm.eat_shroom()