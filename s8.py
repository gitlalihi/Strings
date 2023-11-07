#Python program to check if a string has at least one letter and one number
string=str(input(" Enter your string:"))

flag_l = False
flag_n = False
 
for i in string:
    if i.isalpha():
        flag_l = True
    if i.isdigit():
        flag_n = True
print(flag_l and flag_n)
 
 
