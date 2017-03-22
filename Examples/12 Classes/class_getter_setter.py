class Duck:
    #def __init__(self, color = ‘white’):
        #self._color = value
    def __init__(self, **kwargs):
        #self._color = kwargs.get(‘color’, ‘white’)
        self.variable = kwargs


    def quack(self):
        print("Quack!", self._v)
    def walk(self):
        print("Walks like a duck,", self._v)

    def set_color(self, color):
        #self._color = color
        self.variable['color'] = color
    def get_color(self):
        #return self._color
        return self.variable.get('color', None)

    def set_variable(self, k , v):
        self.variable[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)
def main():
    donald = Duck()
    donald = Duck(color = 'red')
    donald = Duck(feet = 2)
    print(donald._color)
    print(donald.get_color())
    donald_color = 'blue'
    donald.set_color('blue')
    print(donald.get_color())