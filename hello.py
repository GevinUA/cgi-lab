#!/usr/bin/env python3

import os, json
print("Content-type:text/html\r\n\r\n")
print()
print("<title>test CGI script</title>")
print("<h1>CGI header</h1>")
print("<p>Hello CMPUT404</p>") 

#Q1:
# print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
print(json_object)

