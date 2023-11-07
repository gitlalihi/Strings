#Given a String, perform uppercase of the later part of the string.
string=str(input(" Enter your string:"))
halfindex=len(string)//2
newstring=""
for i in range(len(string)):
    if i>= halfindex:
        newstring= newstring + string[i].upper()
    else:
        newstring= newstring + string[i]
print(" The resultant string is ",newstring)
