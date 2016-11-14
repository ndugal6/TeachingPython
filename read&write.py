fw = open('sample.txt', 'w') #opens file and writes to it (that's what the w does)
fw.write('Writing some stuff in my text file\n')
fw.write('I miss the Mountains\n') #remember thaat \n gives you a newline
fw.close() #closes it and frees up some memory

fr = open('sample.txt', 'r') #use 'r' so it reads vs the above 'w'
text = fr.read() #This will read everything in file and store in variable text
print(text)
fr.close()