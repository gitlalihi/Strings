#Python program to count number of vowels using sets in given string
string= input("Enter your string:")
print("Your string is:",string)
vowels={'a','e','i','o','u','A','E','I','O','U'}
count=0
for v in vowels:
    if v  in string:
        count= count+1
print(f"Your number of vowels in your string is: {count}")        
