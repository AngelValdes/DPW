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

        self.drill = Tool()#instantiate drill object with values
        self.drill.price = "$129.00"
        self.drill.make = "DeWALT"
        self.drill.model = "DCD771C2"
        self.drill.image = "images/drill.jpg"
        self.drill.height = "4.25 in"
        self.drill.width = "9.875 in"
        self.drill.weight = "6.75 lb"
        self.drill.description = "20-Volt Max Lithium-Ion 1/2 in. Cordless Drill/Driver Kit"

        self.air_compressor = Tool()#instantiate compressor object with values
        self.air_compressor.price = "$199.00"
        self.air_compressor.make = "DeWALT"
        self.air_compressor.model = "DW1KIT18PP"
        self.air_compressor.image = "images/aircompressor.jpg"
        self.air_compressor.height = "19.875 in"
        self.air_compressor.width = "16.875 in"
        self.air_compressor.weight = "40.75 lb"
        self.air_compressor.description = "6 Gal. Heavy Duty Air Compressor Combo Kit"

        

