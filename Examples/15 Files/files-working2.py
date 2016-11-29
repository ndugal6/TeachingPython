#!/usr/bin/python3

def main():


    buffersize = 50000
    #infile = open('lines.txt', 'r')
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt','w')
    buffer = infile.read(buffersize)

#Since we're reading a large file, lets read it in chuncks of 50000 bytes,
    #Object isn't iterable which is why we use a while loop
    while len(buffer):
        outfile.write(buffer)
        print('.', end=' ')
        buffer = infile.read(buffersize)
    print()
    print('Done')
    for line in infile:

        print(line, file = outfile, end=' ')
    print('Done.')

if __name__ == "__main__": main()
#shift+command+v allows paste from history on pycharm.... not relevant, just figured it out and want to remember