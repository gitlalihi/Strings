#Python | Swap commas and dots in a String
string= input("Enter your string having dots and commas:")
print("Your string is:",string)
string=string.replace(',' , '_')
string=string.replace('.',',')
string=string.replace('_','.')

print(" Your modified string is :",string)
