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

#Gather some more info
age = int(raw_input("Enter your age: "))
birthday_already = raw_input("Did you have your birthday this year already: (y/n) ")
height = raw_input("Enter your height: ")
weight = raw_input("Enter your weight: ")

#Define some internal values to use in functions
age_range = ["children","adult","senior"]
foods = {"breakfast":"sandwich", "lunch":"rice and chicken", "dinner":"milk and cereal"}
now = datetime.datetime.now()