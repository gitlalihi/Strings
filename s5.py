#Python program to print even length words in a string
string=str(input(" Enter your string:"))
str_split = string.split(',')

for i in str_split:
    if len(i.strip()) % 2 == 0:  
        print(i)
even_length_words = [w for w in str_split if len(w.strip()) % 2 == 0]
print("Your even length words are:", even_length_words)
print("Total even length words:", len(even_length_words))