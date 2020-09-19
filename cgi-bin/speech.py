#!/usr/bin/python3
import subprocess as sp
import cgi
print("content-type: text/html")
print()
mydata=cgi.FieldStorage()
y=mydata.getvalue('q')


if "docker status" in y:
	print("<meta http-equiv='refresh' content=0;url='http://192.168.43.80/cgi-bin/docker_status.py'/>")
	

elif "docker" in  y:
	print("<meta http-equiv='refresh' content=0;url='http://192.168.43.80/cgi-bin/xxx.py'/>")
