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
        utility = Utility() #instantiate a utility object
        page = ContentPage()  #instantiate a page object
        if self.request.GET: #determine if there is any query string variables
            tools_info = ToolsInfo()
            
        else:
            #show welcome page
            page._body = """
<h2>Welcome to my tools site</h2>      
        <img src="images/airCompressor.jpg" />
        <img src="images/drill.jpg" />
        <img src="images/nailGun.jpg" />
        <img src="images/sander.jpg" />
        <img src="images/saw.jpg" />
        <hr/>
        <p>Please select one of the options from the <strong>menu above</strong> to get more information about any of my tools</p>
"""
        #use the utility extra class to display the date formatted
        page._head = page._head.replace("{date}", utility.get_date())
        #print page content
        self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
