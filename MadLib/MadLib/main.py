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

#function age range
def ageRange():
    if (age<18):
        result = age_range[0]
    elif (age>=18 and age<=55):
        result = age_range[1]
    else:
        result = age_range[2]
    return result
print "You are ", ageRange()

#function year borned
def yearBorn(currentYear, age):
    if (birthday_already.upper() == "Y"):
        result = currentYear - age 
    else:
        result = currentYear - age - 1
    return result
print "You were born in ", yearBorn(now.year, age)

#function to determine food type based on time of day
def foodType():
    if(now.hour<12):
        result = foods["breakfast"]
    elif(now.hour>=12 and now.hour<15):
        result = foods["lunch"]
    else:
        result = foods["dinner"]
    return result
print "You should be eating " + foodType() + " at this time"

#function to display some funny message
def funnyMessage(age, weight, height):
    result = "Based on your age of {age}, weight of {weight}, and height of {height}, you are in excellent shape!"
    result = result.format(**locals())
    print result
    print "well... some sort of shape!"
funnyMessage(age, weight, height)

#to say good bye several times
for i in range(1,4):
     print "The End, in  ", i 
     i+=1

#reference
#print now.year, now.month, now.day, now.hour, now.minute, now.second
#print now.hour