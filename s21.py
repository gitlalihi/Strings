#Python program for removing i-th character from a string
string= input("Enter your string:")
print("Your string is:",string)
i=int(input("Enter the index you want to remove from the string"))
newstring= string[:i] + string[i+1:]
print(" Your string after removing the i th index is:",newstring)

