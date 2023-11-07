#Program to check if a string contains any special character
import re
string= input("Enter your string:")
print ("Your string is :",string)

if ( bool (re.match ("^[a-zA-Z0-9] *$",string)) == True):
        print(" string does not have a special  charchter")
else:
        print("string has  a special chrachter")

       