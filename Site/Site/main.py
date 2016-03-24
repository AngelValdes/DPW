'''
name: Angel Valdes
date: 3/24/2016
class: Design Patterns for Web Programming
assignment: Dynamic Site
instructor: REBECCA CARROLL
'''
import webapp2 #use the webapp2 library


class MainHandler(webapp2.RequestHandler):    
    def get(self):# main function     
       pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
