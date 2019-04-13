# program for random password generation
import random

characters='abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password=''

for i in range(11):
    password+=random.choice(characters)

print("Here is your password\n")
print(password)
