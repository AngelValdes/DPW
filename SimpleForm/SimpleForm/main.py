'''
name: Angel Valdes
date: 3/9/2016
class: Design Patterns for Web Programming
assignment: Simple Form
instructor: REBECCA CARROLL
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): 
    def get(self):# main function
        self.response.write("Hello")

class Page(object): #class for page properties and behaviours
    def __init__(self): #initialization method
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
