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

    