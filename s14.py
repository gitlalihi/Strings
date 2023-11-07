#Python | Maximum frequency character in String
string= input("Enter your string:")
print("Your string is:",string)
def max_ferq(string):
    frequncy={}
    for i in string:
        if i in frequncy:
            frequncy[i]=frequncy[i]+1
        else:
            frequncy[i]=1
    newstring = max(frequncy, key = frequncy.get) 
    return newstring
 

print ("The maximum of all characters in your strings is  : ",max_ferq(string) )
        