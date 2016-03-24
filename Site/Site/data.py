'''
name: Angel Valdes
date: 3/24/2016
class: Design Patterns for Web Programming
assignment: Dynamic Site
instructor: REBECCA CARROLL
'''
# Data object to define the tool attributes
class Tool(object):
    def __init__(self):
        self.price = ""
        self.make = ""
        self.model = ""
        self.height = ""
        self.width = ""
        self.weight = ""
        self.description = "" 

#Data class to mimic a database of information about home tools (saw, drill, aircompressor, nailgun, sander), Instantiating one of each type of tool.
class ToolsInfo(object):
    def __init__(self):
        self.saw = Tool() #instantiate saw object with values
        self.saw.price = "$399.00"
        self.saw.make = "DeWALT"
        self.saw.model = "DWS779"
        self.saw.image = "images/saw.jpg"
        self.saw.height = "18.8 in"
        self.saw.width = "23.75 in"
        self.saw.weight = "75 lb"
        self.saw.description = "15 Amp 12 in. Sliding Compound Miter Saw"

       

