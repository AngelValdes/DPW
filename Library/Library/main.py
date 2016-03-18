'''
name: Angel Valdes
date: 3/16/2016
class: Design Patterns for Web Programming
assignment: Library
instructor: REBECCA CARROLL
'''
import webapp2 #use the webapp2 library
from pages import FormPage, ResultPage #*
from library import Car, CarInventory #*

class MainHandler(webapp2.RequestHandler):    
    def get(self):# main function
        car_inventory = CarInventory()
        car1 = Car() #instantiate an object 
        car1.year = 2014
        car1.brand_name = "Mercedes Benz"
        car1.price = 43000
        car_inventory.add_car(car1)
        car2 = Car() #instantiate an object 
        car2.year = 2008
        car2.brand_name = "Toyota"
        car2.price = 13000
        car_inventory.add_car(car2)
        car3 = Car() #instantiate an object 
        car3.year = 2016
        car3.brand_name = "BMW"
        car3.price = 83000
        car_inventory.add_car(car3)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)