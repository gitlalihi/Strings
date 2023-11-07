#Python – Specific Characters Frequency in String List
string= input("Enter your string:")
print("Your string is:",string)

stringlistchar=input("Enter your specefic charachters seperated by comma you want to find the frequency:").split(',')
print(" Your list of characters from your string is :",stringlistchar)

d=dict()
for i in stringlistchar:
    d[i]=string[0].count(i)
newstring=d
print("The frequency of specfic charachters in string list are:",newstring)    
