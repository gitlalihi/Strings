#Find length of a string in python
string=str(input(" Enter your string:"))
print("Your length of the given string is ",len(string)) # 1 st way

def len_string(string):   #2nd way
    count=0
    for i in range(len(string)):
       count= count+1
    return count
print("Your length of the string is ",len_string(string))    
    

