#Python program to capitalize the first and last character of each word in a string
string=str(input(" Enter your string:"))
s1=string.split()
newstring=[]
for i in s1:
    s2=i[0].upper()+ i[1:-1] + i[-1].upper()
    newstring.append(s2)
newstring =" ".join(newstring)    
print("Your modified string is :",newstring)    