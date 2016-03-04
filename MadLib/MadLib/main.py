import datetime

#Welcoming user
print "Welcome to my story game!"

#Gather some initial information
name = raw_input("Enter your name: ")
color = raw_input("Enter your favorite color: ")
city = raw_input("Enter the city you live in: ")

#Message template
message1Template = '''
   {name} you are doing great! but I wonder why would you like {color}, if you live in {city}?
   '''
#Replace place holders with values in message template
message1Template = message1Template.format(**locals())
#Print message
print message1Template