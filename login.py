#!/usr/bin/env python3

import cgi
import cgitb
import os
import templates
import get_data_from_form
import secret
from http.cookies import SimpleCookie

#create instance of field storage
form = cgi.FieldStorage()
#get data from field

username = form.getvalue("username")
password = form.getvalue("password")
cookie = SimpleCookie(os.environ.get("HTTP_COOKIE"))

#first determine if I can use cookie to log in
if(cookie.get("username") and cookie.get("password") and cookie.get("username").value == secret.username and cookie.get("password").value == secret.password):
	print("Content-type:text/html\r\n\r\n"+templates.secret_page(cookie.get("username").value, cookie.get("password").value))
#if I can't, and I havn't input my username and password, then show login page
elif(username ==None and password == None):
    print(templates.login_page())
# if I input those value, judge if it is correct
else:

	if(username==None and password == None):
		print(get_data_from_form.login_page())
	#if correct, save the cookie, and log in.
	elif(username == secret.username and password == secret.password):
		print("Set-Cookie: username=" + secret.username)
		print("Set-Cookie: password=" + secret.password)
		print("Content-type:text/html\r\n\r\n")
		print("<html>")
		print("<head>")
		print("<title>Hello - Second CGI Program</title>")
		print("</head>")
		print("<body>")
		print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))
		print("</body>")
		print("</html>")
	#if not, then try again
	else:
		print(templates.after_login_incorrect())
