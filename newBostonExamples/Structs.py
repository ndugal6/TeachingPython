from struct import *

#Store as bytes data
packed_data = pack('iif', 6, 19, 4.73)
#print bytes data
print(packed_data)

#print the number of bytes needed to store
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#To get bytes data back to normal
original_data = unpack('iif', packed_data)
print(original_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))