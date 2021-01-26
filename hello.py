#!/usr/bin/env python3


#Resources used for this script:
'''

retrieving cookies: 
Rajendra Dharmkar
https://www.tutorialspoint.com/How-to-retrieve-cookies-in-Python-CGI-Programming

setting cookies:
Rajendra Dharmkar
https://www.tutorialspoint.com/How-to-setup-cookies-in-Python-CGI-Programming

'''


import os
import json
import templates
import secret
import cgi
form = cgi.FieldStorage()

def login():
    print('Content-Type: text/html')
    print()
    #question 1
    #print(json.dumps(dict(os.environ),indent=2))
    #print()
    #question 2
    #The Query_String parameter when obtaining hello.py 
    #print("parameters: ")
    #print(os.environ["Query_String"])
    # print('''
    # <!doctype html> 
    # <html>
    # <body>
    # <ul>
    # ''')
    # for item in os.environ["QUERY_STRING"].split('%'):
    #     print(f"<li>"+str(item)+"</li>")
    # #print("<li>hello</li>")

    # print('''
    # </ul>
    # </body>
    # </html>
    # ''')

    #question 3
    # "HTTP_USER_AGENT" displays the OS and browser information
    #question3.1
    print(templates.login_page())
def find_cookeis():
    if(len(os.environ["HTTP_COOKIE"]) >0 ):
        cookies =[]
        # print('Content-Type: text/plain')
        # print()
        # print("values: "+str(os.environ["HTTP_COOKIE"]))

        for item in os.environ["HTTP_COOKIE"].split(";"):

            values = item.split("=")
            print(values)  
            if(values[0] == "username"):
                cookies.append(values[1])
                
            if(values[0] == " password"):
                cookies.append(values[1])
        cookies.sort()
        return cookies
    return []

def main():
    cookies = find_cookeis()
    # print()
    if(len(cookies) >1):

        #print("username: "+cookies[0])
        #print("password: "+cookies[1])
        print('Content-Type: text/html')
        print()
        print(templates.secret_page(cookies[0],cookies[1]))
    else:     
        if(len(form) ==0):
            login()
        if(len(form) > 0):
            if(form.getvalue("username") == secret.username and form.getvalue("password") == secret.password):
                print("Set-Cookie:username = "+form.getvalue("username") + ";")
                print("Set-Cookie:password = "+form.getvalue("password") + ";")
                print('Content-Type: text/html')
                print()
                print(templates.secret_page(secret.username,secret.password))
                # print('''<!doctype html> 
                # <html>
                # <body>''')
                # print("<b>"+"Logged in as: " + form.getvalue("username")+"</b>")
                # print('''<ul> ''')
                # print("<li> <b>"+"username : "+str(form.getvalue("username")) + "</b> </li>")
                # print("<li> <b>"+"password: "+str(form.getvalue("password")) + "</b> </li>")

                # print('''</ul> ''')
                # print("<b>refresh page to see if the cookies work. i sent them to the template page!</b>")
                # print('''
                # </body>
                # </html>''')
            else:
                print('Content-Type: text/html')
                print()
                print(templates.after_login_incorrect())
main()