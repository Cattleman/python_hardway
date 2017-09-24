from sys import argv

script, first_name, last_name = argv

print "Hello, ", first_name
print "What can I help you with Mr.", last_name,"?"

destination = raw_input("Where would you like to go? ")
time = raw_input("How long are you willing to travel (hrs)?: ")

print "%r can be reached in 2 hours" % destination

user = raw_input("User Name: ")
pswd = raw_input("Password: ")


print "Permission Granted", "." * 10
print "Welcome, %s" % user
