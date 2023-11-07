#Remove all duplicates from a given string in Python
string= input("Enter your string:")
print("Your string is:",string)

def remove_duplicate_strs(string):
    unique_char=set()
    newstring =""
    for i in string:
        if i not in unique_char:
           unique_char.add(i)
           newstring=newstring+i 
    return newstring          
        
print("Your modified string is:",remove_duplicate_strs(string))        
