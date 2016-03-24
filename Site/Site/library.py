'''
name: Angel Valdes
date: 3/24/2016
class: Design Patterns for Web Programming
assignment: Dynamic Site
instructor: REBECCA CARROLL
'''
#importing external library to use date time functionality
import datetime

class Utility(object): #utility library class
    def __init__(self): #initialization method
        pass
    #method to return formatted date in US format
    def get_date(self):
        today = datetime.datetime.today()
        return today.strftime("%m/%d/%y")
