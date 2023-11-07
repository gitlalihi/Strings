#Remove Letters From a String in Python
string=str(input(" Enter your string:"))
char=int(input(" Enter position of a charachter/letter to be removed"))
newstring=""
for i in range(len(string)):
    if i!=char:
        newstring=newstring +string[i]
print(" Your string after removing a charachter is",newstring)        