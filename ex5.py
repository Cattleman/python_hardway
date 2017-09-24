my_name = 'Ian F. Hensel'
my_age = 27 #not a lie
my_height = 70 # inches
my_weight = 220 # lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky thry to get it exsactly right
print "If I add %d, %d, and %d, I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "When %s goes to Europe it is helpful to convert to metric." % my_name
height_cm = my_height * 2.54
weight_kg = float(my_weight) * 0.453

print "When %s is in Europe, he is %d cm tall and %d kg heavy." % (my_name , height_cm, weight_kg)
