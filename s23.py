#Python | Check if a given string is binary string or not
string=input("Enter your string:")
s1=set(string)
print(" Your string is:",s1)
set={'0','1'}
if set==s1 or set=={'0'} and set=={'1'}:
    print("Your string is binary")
else:
    print("Your string is not binary")
