from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's pring the whole file: \n",

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file) # starts over at the begining of the file

print "Let's print three lines:"

current_line = 1 # value is 1
print_a_line(current_line, current_file)

current_line += current_line # value 1 + 1 becuase of iadd
print_a_line(current_line, current_file)

current_line = current_line + 1 # 2 + 1
print_a_line(current_line, current_file)
