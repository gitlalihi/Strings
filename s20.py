#Find words which are greater than given length k
string= input("Enter your string:")
s1=string.split()
print("Your string is:",s1)
k= int(input("Enter your number you want to find the strings greater than the number you entered:"))
def find_greater_words(s1,k):
    str=[]
    for s in s1:
        if len(s)>k:
            str.append(s)
    return str
print("Your string is :",find_greater_words(s1,k))        
