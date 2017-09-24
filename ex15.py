from sys import argv #gets the argv module

script, filename = argv #assigns values

txt = open(filename) #opens the 'filename' var and puts it into the 'txt' var

print "here's your file %r:" % filename
print txt.read() # prints the txt file

print "Type the filename agian:"
file_agian = raw_input(">") #prompts for the filename

txt_again = open(file_agian)

print txt_again.read() #Boom!
