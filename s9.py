# Python Program to Accept the Strings Which Contains all Vowels
string = input("Enter a string: ")
def contains_all_vowels(input_str):
    input_str = input_str.lower()
    all_vowels = {'a', 'e', 'i', 'o', 'u'}
    for v in all_vowels:
        if v not in input_str:
            return False
    return True
if contains_all_vowels(string):
    print("Accepted")
else:
    print("Not accepted")


