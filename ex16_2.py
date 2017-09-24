from sys import argv

script = argv

print "Hello. What file would you like to open?"
filename = raw_input(">")

print "Opening the file..."
target = open(filename, 'w')

print "Lets write three lines. "

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line3: ")
summarize = "%r\n%r\n%r" % (line1, line2, line3)

print "added following to file: \n",
print summarize

target.write(summarize)
