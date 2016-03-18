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