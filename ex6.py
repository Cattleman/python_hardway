
# make some variables
x = "There are %d types of people." % 10
binary = "binary" #sting
do_not = "don't" # string
y = "Those who know %s and tose who %s." % (binary, do_not) # inputs strings

print x
print y

print "I said: %r." % x #inputs x
print "I also said: '%s'." % y

hilarious = False # assigns 'hilarious' var a bool value
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."

print w + e # joins two strings
