#Python | Check for URL in a String
string= input("Enter your string :").split()
print("Your string is:",string)
newstring=[]
for i in string:
    if i.find("https:")==0 or i.find("http:")==0:
        newstring.append(i)
print(" Your  checked string  is:",newstring)        
