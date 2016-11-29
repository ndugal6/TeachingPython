#!/usr/bin/python3

def main():
    #Opens in read binary mode
    #f = open('olives.jpg', 'rb')

    #This copies an image, reads the original image in byte chunks and then writes those chuncks to a new file, the bytes are then properly copied aka image is gud
    buffersize = 50000
    infile = open('olives.jpg', 'rb')
    outfile = open('new.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.',end='')
        buffer = infile.read(buffersize)

#So since buffer isn't iterable, MAKE A METHOD THAT DOES JUST THAT SO I DON'T HAVE TO TYPE WHILE LOOP
    #CHALLENGE 
    print()
    print('Done')
    # for line in f:
    #     print(line, end = '')

if __name__ == "__main__": main()
