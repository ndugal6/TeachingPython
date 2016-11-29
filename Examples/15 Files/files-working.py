#!/usr/bin/python3

def main():
    #r for read, w for write, a for append (special write mode that starts at end),
    # r+ is read and write
    # rt for text file mode, rb for byte mode
    f = open('lines.txt', 'r')
    for line in f.readline():
        print(line, end = '')

if __name__ == "__main__": main()
