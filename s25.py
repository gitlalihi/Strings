#Python program to find uncommon words from two Strings
string=input("Enter your sentence:").split()
print("Your sentence is  :",string)

string2=input("Enter your second sentence:").split()
print("Your second sentence is  :",string2)

newliststr=[]
for i in string:
    if i not in string2:
        newliststr.append(i)
for j in string2:
    if j not in string:
        newliststr.append(j)
newliststr=list(set(newliststr)) 

print(" Your uncommon words in both of your sentences is:",newliststr)
