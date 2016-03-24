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
       pass

