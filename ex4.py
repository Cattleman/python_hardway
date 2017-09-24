cars = 100 #assigns value of 100 to variable 'cars'
space_in_a_car = 4.0 # assigns value of 4.0 (floating point)
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #subtracts var 'cars' from 'drivers'
cars_driven = drivers # assigns cars_driven the value of drivers
carpool_capacity = cars_driven * space_in_a_car #multiples number of cars by capacity
average_passengers_per_car = passengers / cars_driven # divides number of ppl by cars available


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
