#Python | Count the Number of matching characters in a pair of string
string= input("Enter your string:")
print("Your string is:",string)

string1=input("Enter your 2nd string:")
#str2=string1.split(',')
print("Your 2nd string is :",string1)

def matching_charpair_counting(string,string1):

    count = 0
    for char in string:
        if char in string1:
            count =count + 1
    return count

matchstr = matching_charpair_counting(string,string1)
print(f"Your matching pairs are: {matchstr}")