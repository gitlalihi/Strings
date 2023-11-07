#Python | Find all close matches of input string from a list
patterninput1= input("Enter your pattern list of string seperated by a comma:")
str1input=patterninput1.split(',')
print("Your list of pattern strings is :",str1input)   

inputstring=input("Enter your string you want to find the matches from the list of pattern strings:")

    
if inputstring in str1input:
   print("Close matches in the input list of string is:",list(str1input))
else:
   print("No matches found")