#Python – Avoid Spaces in string length
string=str(input(" Enter your string with spaces:"))
count = 0
for i in range(len(string)):
    if i =='':
        continue
    count = count +1
print("The charachters frequency avoiding the spaces is:",string)        
