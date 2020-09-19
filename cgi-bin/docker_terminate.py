#!/usr/bin/python3
import subprocess as sp
import cgi

print("content-type: text/html")
print()

form= cgi.FieldStorage()
cname= form.getvalue("s")
cmd= "sudo docker rm -f {}".format(cname)

x=sp.getoutput(cmd)

print("location:http://192.168.43.80/cgi-bin/docker_status.py")
print()

