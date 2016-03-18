from sys import argv

script, filename = argv

txt = open(filename, 'a+')

print "Here's your file %r: " % filename
print txt.readline()
print "-- Done reading the first line. --"
print txt.read()

txt.write("Adding this 4th line to the text file (I think).")
txt.close()

print "Type the filename again: " 
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
