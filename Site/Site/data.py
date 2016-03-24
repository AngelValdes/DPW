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

        self.nail_gun = Tool()#instantiate nail gun object with values
        self.nail_gun.price = "$119.00"
        self.nail_gun.make = "DeWALT"
        self.nail_gun.model = "DWFP12233"
        self.nail_gun.image = "images/nailgun.jpg"
        self.nail_gun.height = "13.09 in"
        self.nail_gun.width = "3.74 in"
        self.nail_gun.weight = "2 lb"
        self.nail_gun.description = "18-Gauge Pneumatic Brad Nailer"

        self.sander = Tool()#instantiate sander object with values
        self.sander.price = "$79.00"
        self.sander.make = "DeWALT"
        self.sander.model = "DWE6423K"
        self.sander.image = "images/sander.jpg"
        self.sander.height = "6.2 in"
        self.sander.width = "7.25 in"
        self.sander.weight = "4 lb"
        self.sander.description = "3 Amp 5 in. Corded Variable Speed Random Orbit Sander"

