#!/usr/bin/python3

first = input()
last = input()

# named formatting variables, best way to put something in string
print("Hello {firstname} {lastname}! You just delved into python.".format(firstname=first, lastname=last))

# if not named, index matters
print("Hello {} {}! You just delved into python.".format(first, last))

# similar to printf, but for %s to work, must pass a tuple after %
print("Hello %s %s! You just delved into python." % (first, last))

# Use template and substitute args
from string import Template
tmpl = Template("Hello $firstname $lastname! You just delved into python.")
print(tmpl.substitute(firstname=first, lastname=last))
