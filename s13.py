#Python – Least Frequent Character in String
string= input("Enter your string:")
print("Your string is:",string)
def least_ferq(string):
    frequncy={}
    for i in string:
        if i in frequncy:
            frequncy[i]=frequncy[i]+1
        else:
            frequncy[i]=1
    newstring = min(frequncy, key = frequncy.get) 
    return newstring
 

print ("The minimum of all characters in your strings is  : ",least_ferq(string) )
        