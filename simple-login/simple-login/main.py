'''
name:
date:
class:
assignment:
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): 
    def get(self):# main function
        self.response.write('Hello world2!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
