def main():
    fin = open('utf8.txt', 'r', encoding='utf_8')
    fout = open('utf8.html', 'w')
    #Muttable list of bytes
    outbytes = bytearray()
    for line in fin:
        for c in line:
            #ord(c) gives us the integer value of character
            if ord(c) > 127:
                #bytes() are immutable array of bytes
                # if byte is out of normal ascii range, we encode it with xml entity allowing us to see fancy image
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
            else: outbytes.append(ord(c))
        outstr = str(outbytes, encoding = 'utf_8')
        print(outstr, file = fout)
        print(outstr)
        print('Done.')
        #Printed are the unicode values for the fancy characters
        #The beauty of a byte array we can operate on characters since characters are bytes,

if __name__ == "__main__": main()
