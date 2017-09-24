print "How old are you?",
age = raw_input() #raw_input() prompts for a value in terminal
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#we've put values into the above variables, so this next line
# calls those values to complete our print.

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
