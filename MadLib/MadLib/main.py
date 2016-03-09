#importing external library to use date time functionality
import datetime

#Welcoming user
print "Welcome to my story game!"

#Gather some initial information
name = raw_input("Enter your name: ") #variable to store name entered by user when prompt
color = raw_input("Enter your favorite color: ") #variable to store color enter by user when prompt
city = raw_input("Enter the city you live in: ") #variable to store city enter by user when prompt

#Message template
message1Template = '''
   {name} you are doing great! but I wonder why would you like {color}, if you live in {city}?
   '''
#Replace place holders with values in message template
message1Template = message1Template.format(**locals())
#Print message
print message1Template

#Gather some more info
age = int(raw_input("Enter your age: ")) #variable to store age enter by user when prompt and convert to integer
birthday_already = raw_input("Did you have your birthday this year already: (y/n) ") #variable to store if birthday passed for this year enter by user when prompt
height = raw_input("Enter your height: ") #variable to store height enter by user when prompt
weight = raw_input("Enter your weight: ") #variable to weight enter by user when prompt

#Define some internal values to use in functions
age_range = ["children","adult","senior"] #list of possible age ranges
foods = {"breakfast":"sandwich", "lunch":"rice and chicken", "dinner":"milk and cereal"} #dictionary of food types 
now = datetime.datetime.now() #date and time right now

#function age range
def ageRange():
    if (age<18): #if age less than 18 it is a children
        result = age_range[0]
    elif (age>=18 and age<=55): #if age between 18 and 55 it is an adult
        result = age_range[1]
    else:
        result = age_range[2] # any other age should be a senior
    return result
print "You are ", ageRange() #print message with final age range resulted

#function year borned
def yearBorn(currentYear, age):
    if (birthday_already.upper() == "Y"): #convert to uppercase the value entered and compared if it is yes
        result = currentYear - age 
    else:
        result = currentYear - age - 1 #if you already had a birthday this year, substract it also from the amount
    return result
print "You were born in ", yearBorn(now.year, age) #print message with resulting value

#function to determine food type based on time of day
def foodType():
    if(now.hour<12): #if it is less than 12, you should have breakfast
        result = foods["breakfast"]
    elif(now.hour>=12 and now.hour<15): #if it is 12 or later but earlier than 3pm, you should have lunch
        result = foods["lunch"]
    else:
        result = foods["dinner"]  #after 3pm, you should have dinner
    return result
print "You should be eating " + foodType() + " at this time" #Print message

#function to display some funny message
def funnyMessage(age, weight, height): #function definition accepting parameters
    result = "Based on your age of {age}, weight of {weight}, and height of {height}, you are in excellent shape!"
    result = result.format(**locals())#substitude place holders with local variables values
    print result #print result
    print "well... some sort of shape!" #print extra message
funnyMessage(age, weight, height)

#to say good bye several times
for i in range(1,4): #repeat where "i" is in range
     print "The End, in  ", i   #print message
     i+=1 #increment counter

#reference
#print now.year, now.month, now.day, now.hour, now.minute, now.second
#print now.hour