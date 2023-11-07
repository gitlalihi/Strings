#Reverse Words in a Given String in Python
string=str(input("Enter a string"))
x=0
def reversal(x):
    sReverse= x[::-1]  
    return sReverse    

string= reversal(string) 
print("Reversed string is\n", string)