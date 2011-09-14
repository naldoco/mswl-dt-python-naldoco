#!/usr/bin/python
#Keep an eye on: http://docs.python.org/library/string.html
pswd = file( '/etc/passwd', 'r' )
for line in pswd:
    line = line.strip()
    fields = line.split(':')
    print fields[0],'->' ,fields[6]
pswd.close()
