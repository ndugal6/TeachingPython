#!/usr/bin/python3


class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    def del_property(self,key):
        del self.properties[key]
    #Turns into accessor with following decorator
    @property
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']


def main():
    donald = Duck(color = 'blue',head = 'round')
    print(donald.get_properties())
    print(donald.get_property("head"))
    donald = Duck()
    donald.color = 'blue'
    print(donald.color)
    donald.del_property('color')
    # donald.__delattr__('color')
    print(donald.color)
    donald.properties = {'head' : 'square'}
    print(donald.get_properties())
    #print(donald.get_property('color'))

    # dic = dict(data=[1,2], target=[])
    # datas = dic['data']
    # dic.update(data=datas+[3,4])
    # print(dic)

if __name__ == "__main__": main()
