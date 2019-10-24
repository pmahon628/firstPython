print ("What is up homie.")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Variables
character_name = "Pat"
character_age = 29
character_age_wish = "20"
is_Male = True

print("There once was a man named "  + character_name + ",")
print("He is " + character_age + " years old")

# reassign
character_name = "Tim"

print("There once was a man named "  + character_name + ",")
print("He likes that his name is " + character_name + ",")
print("He wishes he was " + character_age_wish + ".")

# Strings

phrase = "Umphreys Mcgee"
print(phrase + "is cool")

# functions for  strings
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("parmeter"))
print(phrase.index("enter in param that is not in string throws  error "))
print(phrase.replace("original", "replace"))

# numbers
print(2.0987)
# cant print math functions
print(3  * 4)
# can also do order of operations
print(5 * 5 + 4)
print(3 * (4  + 5))
# modulous - gives remainder - below  gives one
print(10 % 3 )

my_num = 5
print(my_num)

# convert # to string
print(str(my_num) +  "  my  favorite number")

# number functions
# absolute value
my_num =  -5
print(abs)(my_num)
# power to
print(pow(3, 2))
# max  - gives  bigger # / min - does opposite
print(max(4 ,6))

# importing - gives access to alot of math in python
from math import *

# getting input from user:
name = input("Enter your name:  ")
print("hello " + name + "!")

age =  input("enter your age: ")
print("Hello " + name + " You are " + age)

# calculator
num1 = input("enter a number: ")
num2 = input("enter another number: ")
result = int(num1) + int(num2) 
# change int to float to get  decimals
print(result)

# mad libs game
color = input("Enter a color:")
plural_noun = input("Enter a plural noun:")
celebrity = input("Enter a celebrity:")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# Lists
freinds = ["Jake", "Joel", "Andy", "Kris", 4,]

print(freinds)
# refer to elements by index




