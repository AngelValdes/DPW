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
            #choose between the tooltypes saw, drill, aircompressor, nailgun, sander, then build the object to by used in the replace
            if self.request.GET['toolType'] == "saw":
                tool = tools_info.saw            
            elif self.request.GET['toolType'] == "drill":
                tool = tools_info.drill 
            elif self.request.GET['toolType'] == "aircompressor":
                tool = tools_info.air_compressor 
            elif self.request.GET['toolType'] == "nailgun":
                tool = tools_info.nail_gun 
            elif self.request.GET['toolType'] == "sander":
                tool = tools_info.sander 
            #replace the text placeholders with values from selected object.
            page._body = page._body.replace("{description}",tool.description).replace("{picture}",tool.image).replace("{make}",tool.make).replace("{model}",tool.model).replace("{price}",tool.price).replace("{height}",tool.height).replace("{width}",tool.width).replace("{weight}",tool.weight)
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
