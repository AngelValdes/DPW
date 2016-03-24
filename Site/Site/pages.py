'''
name: Angel Valdes
date: 3/24/2016
class: Design Patterns for Web Programming
assignment: Dynamic Site
instructor: REBECCA CARROLL
'''

class Page(object): #class with common functionality by all pages to be inherited
    def __init__(self): #initialization method
        #head section of the page
        self.__title = ""
        self._head = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">
    <title>My Tools Site</title>
    <link href="css/bootstrap.min.css" rel="stylesheet" />
    <link href="css/bootstrap-theme.min.css" rel="stylesheet" />
    <link href="css/styles.css" rel="stylesheet" />
</head>

<body>

    <div class="container">
        <div class="masthead">
            <h2>My Tools Site</h2>
            <nav>
                <ul class="nav nav-justified">
                    <li><a href="/">Home</a></li>
                    <li><a href="/?toolType=saw">Saw</a></li>
                    <li><a href="/?toolType=drill">Drill</a></li>
                    <li><a href="/?toolType=aircompressor">Air Compressor</a></li>
                    <li><a href="/?toolType=nailgun">Nail Gun</a></li>
                    <li><a href="/?toolType=sander">Sander</a></li>
                </ul>
            </nav>
        </div>
        <p>Today: {date}</p>
"""
       