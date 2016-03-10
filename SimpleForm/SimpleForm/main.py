'''
name: Angel Valdes
date: 3/9/2016
class: Design Patterns for Web Programming
assignment: Simple Form
instructor: REBECCA CARROLL
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): 
    def get(self):# main function
        p = Page() #instantiate an object of Page type
        if self.request.GET: #determine if there is any query string variables
            self.full_name = self.request.GET['fullName'] #get query string variables values
            self.phone = self.request.GET['phone']
            self.email = self.request.GET['email']
            self.gender = self.request.GET['gender']
            self.subject = self.request.GET['subject']
            self.additional_comments = self.request.GET['additionalComments']
            all = p.print_submission() #call submission method
            all = all.format(**locals())   #replace placeholders for local values
            self.response.write(all) #write out the final result to the browser
        else:
            self.response.write(p.print_form()) #write out to the user the result of calling print_form method from p instance

class Page(object): #class for page properties and behaviours
    def __init__(self): #initialization method
        #define head variable to contain common initial html elements
        self.head = ''' 
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    <meta charset="utf-8" />
    <link href="css/styles.css" rel="stylesheet" />
</head>
<body>
    <h2>Contact Us!</h2>
'''
#define form variable to contain form html elements for initial form
        self.form = '''
    <h3>By sending your questions and comments below</h3>
    <div>
        <form method="GET" action="">
            <label for="fullName">Full Name</label>
            <input type="text" id="fullName" name="fullName" required="required">
            <label for="phone">Phone</label>
            <input type="text" id="phone" name="phone" required="required">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required="required">
            <fieldset>
                <legend>Details</legend>
                <input type="radio" name="gender" value="male" checked="checked"> Male
                <input type="radio" name="gender" value="female"> Female<br><br>
                <label for="subject">Subject</label>
                <select id="subject" name="subject">
                    <option value="sales">sales</option>
                    <option value="marketing">marketing</option>
                    <option value="other">other</option>
                </select>
                <label for="additionalComments">Additional comments</label>
                <textarea rows="8" style="width:100%" id="additionalComments" name="additionalComments"></textarea>
            </fieldset>            
            <input type="submit" value="Submit">
        </form>
    </div>
'''
 
#define submission variable to contain form html elements for printing submited values on screen
        self.submission = '''
        <h3>Thank you for sending your comments</h3>
        <div>
            <form>
                <label>Full Name: </label>{self.full_name}<br/>
                <label>Phone: </label>{self.phone}<br/>
                <label>Email: </label>{self.email}<br/>
                <label>Gender: </label>{self.gender}<br/>
                <label>Subject: </label>{self.subject}<br/>
                <label>Additional comments: </label>{self.additional_comments}<br/>
            </form>
        </div>
'''
#define close variable to contain common closing html elements
        self.close = '''
</body>
</html>
'''
        def print_form(self): #method to compose initial form
            all = self.head + self.form + self.close
            return all 

        def print_submission(self): #method to compose final submited values displayed in screen
            all = self.head + self.submission + self.close
            return all

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
