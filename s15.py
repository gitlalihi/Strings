#Python – Odd Frequency Characters
string= input("Enter your string:")
print("Your string is:",string)
newstring=set(string)
list=[]
for i in newstring:
    if(string.count(i) % 2 != 0):
        list.append(i)
print ("The odd frequency of  characters in your strings is  : ",list )
        