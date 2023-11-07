#Generating random strings until a given string is generated
import random
target_string= input("Enter your target string:")
print ("Your  target string is :",target_string)

def generate_random_string(length):
       return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')for i in range (length))

count=0
while True:
       count=count+1
       random_string=generate_random_string(len(target_string))
       print(f"Attempts {count}:{random_string}")
       if random_string==target_string:
              print(f"Your target string {target_string} is generated in{count}attempts")
              break              
             



