from sys import argv
from os.path import exists

script, from_file, to_file = argv # arguments for script

print "Copying from %s to %s" % (from_file, to_file)

# we could do thse two on oneline, too how?
in_file = open(from_file)
indata = in_file.read() # puts the file in the var indata

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file) #returns T / F if file exists
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input(">")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close() # not alsways needed, but useful if script is complicated
in_file.close()
