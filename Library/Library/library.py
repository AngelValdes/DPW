'''
name: Angel Valdes
date: 3/16/2016
class: Design Patterns for Web Programming
assignment: Library
instructor: REBECCA CARROLL
'''
#importing external library to use date time functionality
import datetime

#car object type class to define object attributes, behaviours, and business rules
class Car(object):
    def __init__(self):
        #Initializing internal fields of object state
        self.__brand_name =""
        self.__year = 0
        self.__price = 0

    #public property brand_name setter and getter
    @property
    def brand_name(self):
        return self.__brand_name
    @brand_name.setter
    def brand_name(self, value):
        self.__brand_name = value
    #public property year setter and getter
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, value):
        if value > 1905 and value <= datetime.datetime.now().year + 1: #business rules for car year
            self.__year = value
    #public property price setter and getter
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value > 0: #business rule for price, must be positive to assign it
            self.__price = value

#utility library to manage a car inventory and do some basic functionalities and calculations
class CarInventory(object):

    def __init__(self):
        self.__car_list = [] #array of owned cars
        
    def add_car(self, car): #add car to inventory
        self.__car_list.append(car)

    def get_cars(self): #return inventory sorted by brand name
        newlist = sorted(self.__car_list, key=lambda x: x.brand_name, reverse=False)
        return newlist

    def get_inventory_value(self): #calculate inventory value, no depreciation considered
        output = 0
        for car in self.__car_list:        
            output += int(car.price)
        return output
        
    def get_most_expensive_car(self): #get the most expensive car from the inventory
        newlist = sorted(self.__car_list, key=lambda x: x.price, reverse=True)
        return newlist[0]      
       
    def get_cheapest_car(self): #get the cheapest car from the inventory
        newlist = sorted(self.__car_list, key=lambda x: x.price, reverse=False)
        return newlist[0] 
