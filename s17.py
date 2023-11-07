#Python | Frequency of numbers in String
string= input("Enter your string:")
print("Your string is:",string)
count=0
for i in string:
    if (i.isdigit()):
        count=count+1
print("The frequency of numbers in your string is :",count)        