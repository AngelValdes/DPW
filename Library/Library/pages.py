'''
name: Angel Valdes
date: 3/16/2016
class: Design Patterns for Web Programming
assignment: Library
instructor: REBECCA CARROLL
'''

class FormPage(object): #class for use input form
    def __init__(self): #initialization method
        self.__title = "Library"
        self.css = "css/styles.css" 
        #head section of the page
        self.__head = """ 
<!DOCTYPE html>
<html>
<head>
    <title>Library</title>
    <meta charset="utf-8" />
    <link href="css/styles.css" rel="stylesheet" />
</head>
<body>
"""
        #form body section of the page
        self.body = """
<h3>Enter car information</h3>
    <div>
        <form method="GET" action="">
            <label for="brandName">Brand Name</label>
            <input type="text" id="brandName" name="brandName" required="required">          
            <label for="year">Year</label>
            <input type="number" id="year" name="year" required="required">
            <label for="price">Price</label>
            <input type="text" id="price" name="price" required="required">
            <input type="submit" value="Add New">
        </form>
    </div>
"""
        #closing the page
        self.__close = """
</body>
</html>
"""
    def print_out(self): #method to compose initial form
        all = self.__head + self.body + self.__close
        return all

class ResultPage(object): #class for page resulting output
    def __init__(self): #initialization method
        self.__title = "Library"
        self.css = "css/styles.css"
        #head section of the page
        self.__head = """
<!DOCTYPE html>
<html>
<head>
    <title>Library</title>
    <meta charset="utf-8" />
    <link href="css/styles.css" rel="stylesheet" />
</head>
<body>
"""
        #Initial part of body
        self.body_start = """
<h3>Your Cars Inventory:</h3>
        <div>          
"""
        #to allow inserting items in list inside body
        self.list_items = ""
        #to create some summaries totals inside body
        self.totals = "<br/>"
        #close body
        self.body_end = """
        </div>
"""
        self.__close = """
</body>
</html>
"""
    def print_out(self): #method to compose initial form
        all = self.__head + self.body_start + self.list_items + self.totals + self.body_end + self.__close
        return all