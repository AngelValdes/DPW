'''
name: Angel Valdes
date: 3/24/2016
class: Design Patterns for Web Programming
assignment: Dynamic Site
instructor: REBECCA CARROLL
'''
import webapp2 #use the webapp2 library
from pages import * #use the pages classes
from data import * #use the database emulation class
from library import Utility #use the extra utility class


class MainHandler(webapp2.RequestHandler):    
    def get(self):# main function     
       pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
