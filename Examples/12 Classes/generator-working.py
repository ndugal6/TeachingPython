#!/usr/bin/python3







class inclusive_range:
    #Constructor
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    #Makes object iterable
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step






def main():
    #range only requires one arguement, but 3 possible: start, stop, step: only need start
    #think of range [start, stop)

    #o = range(5, 25, 2)
    # o = range(25)
    # for i in o: print(i, end = ' ')

    # gen0 = inclusive_range()
    gen1 = inclusive_range(10)
    gen2 = inclusive_range(10,20)
    gen3 = inclusive_range(10,30,5)
    #gen4 = inclusive_range(10,30,5,1)
    for g in gen1:
        print(g)
    for i in inclusive_range(10,30,5): print(i, end = ' ')
if __name__ == "__main__": main()
