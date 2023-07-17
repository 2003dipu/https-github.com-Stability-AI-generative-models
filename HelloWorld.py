"""
red_bucket = input("What do you want to put in the red bucket ? :")
print(red_bucket)

print(5==4)
print(5!=4)
print(5>=4)
print(5>=5)
print(5> and = 5)

Samyo_age = 13
kingergarten_age = 5
if Samyo_age < kingergarten_age:
    print("Samyo should be in pre-school.")
elif Samyo_age == kingergarten_age :
    print("Enjoy kingergarten.")
else :
    print("Samyo should be in another class.")



def print_kevin (text):
   
    print(text)
    print(text)
    print(text)
print_kevin ("He earns a lot from his YouTube channel.")

def school_age_calculator(age, name):
    if age < 5:
        print(f"Enjoy your time! {name} is only {age}.")
    elif age == 5:
        print(f"Enjoy kindergarten, {name}")
    else:
        print("they grow up so fast.")
school_age_calculator(6, "Samyo")
    
def add_ten_to_age(age): #function
    new_age = age + 10
    return new_age
how_old_will_i_be = add_ten_to_age(3)
print(f"Your age will be {how_old_will_i_be}")

# while loop
n = 0
while n <5 :
    print(f" First While loop prints {n}")
    print(f" Second While loop prints {n}")
    n = n + 1

x = 0
while x <5:
    print(x)
    x =x+1
    
#For
for x in range(4,10):
    if x == 6: break
    print(x)


    
# Machine learning codes are not supported here
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url,tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))
housing = load_housing_data()

import math
print(f"pi is {math.pi}")

#Basic Calculator in Python
num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number : "))
result = num1 + num2
print(result)

#Now build an advanced calculator using Python
import math
import tkinter as tk

def add():
  num1 = float(entry1.get())
  num2 = float(entry2.get())
  result = num1 + num2
  label3.config(text=str(result))

def subtract():
  num1 = float(entry1.get())
  num2 = float(entry2.get())
  result = num1 - num2
  label3.config(text=str(result))

def multiply():
  num1 = float(entry1.get())
  num2 = float(entry2.get())
  result = num1 * num2
  label3.config(text=str(result))

def divide():
  num1 = float(entry1.get())
  num2 = float(entry2.get())
  result = num1 / num2
  label3.config(text=str(result))

root = tk.Tk()
root.title("Advanced Calculator")

label1 = tk.Label(root, text="First number:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Second number:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root)
label3.grid(row=2, column=0)

button1 = tk.Button(root, text="Add", command=add)
button1.grid(row=3, column=0)

button2 = tk.Button(root, text="Subtract", command=subtract)
button2.grid(row=3, column=1)

button3 = tk.Button(root, text="Multiply", command=multiply)
button3.grid(row=4, column=0)

button4 = tk.Button(root, text="Divide", command=divide)
button4.grid(row=4, column=1)

root.mainloop() 
#Mad Libs Game
color = input("Enter a color : ")
plural_noun = input("Enter a Plural Noun :")
celebrity = input("Enter a celebrity : ")
print(f"Roses are {color} ")
print(f"{plural_noun} are blue")
print(f"I love {celebrity}")


#Lists in Python
friends = ["Pronoy", "Amit",[12],[23],[34], "Shrabanto", "Shimul","Bipul"]
friends[2] = "Dipu"
print(friends)
print(friends[3])
print(friends[2::])

#Lists in Python
lucky_numbers = [4,6,8,12,14,18,20]
friends = ["Amit Singha","Dipu Singha" , "Shrabanto Singha",2,"Pronoy Singha","Dipu Singha", "Shimul Singha","Tusar Singha","Dipu Singha"]
print(friends)
friends[3]= "two"
friends.sort()
friends2 = "Steve Jobs",friends.copy()
print(friends2)
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

# Tuples 
# Tuples are immutable
coordinate = [(4,5),(-1,7),(-13,12)]

coordinates1 = [2,3,-45]

coordinates2 =(3,-3,10)
print(type(coordinates1))
if type(coordinates2) == tuple:
    print("You wrote tuple")
else:
    print("You wanted to write tuple. Is that correct sir?")

def sayhi(user_name, user_age,personality):
    print(f"Hello {user_name}. You are {user_age}!. You are also super-{personality}")
    print("I'm inside of this function.")
    print("In order to print me out, call me outside of this function or just invoke it.")
sayhi("Mike",28,"intelligent")
sayhi("Dipu Singha",21,"creative")

#Return statement are usually used with a function
def cube(num):
    num_tobe_fourth = num*num*num*num
    print("This is a function of exponent or power 4")
    return num_tobe_fourth
print(cube(2))
print("The above function is an example of return statement.")

def power(num):
    print("This is a function of exponent three.")
    return num*num*num
result = power(6)

print(f"The cubed of the number you inserted is {result}")
#If statement in Python
I wake up
If I'm hungry
   I eat breakfast
I leave my house
 If it's cloudy
   I take an umbrella
otherwise 
    I bring sungglasses
I'm at a restaurant
If I want meat
   I order a steak
otherwise if I want vegetables
        I order brocoli & lentil soup
otherwise 
    I order salad.  
#Basic if statement in Python
# I show you how to use three different 'and' statement in Python unlike anything ever before
is_male = True
is_tall = False
age = 12
country = "India"
if is_male and is_tall and age <0:
    print("The person must be a tall male.The person has not been born yet")
elif is_male and not is_tall and age >0 and country == "India":
    print("The person must be a short male. The person have been born in India.")
elif not is_male and is_tall:
    print("The person must be a tall female")
elif not is_male and not is_tall:
    print("The person must be a short female.")
else:
    print("The person must be a short female.")

#Want more if statement? Here's more:
#Python Weight converter this is an exercise that will follow-up lessons on if statements.
print("Welcome credit card user! If you want to sign up for your credit card you must meet the following terms and conditions.")
age = int(input("Enter your age: "))
if age >100:
    print("You are too old to sign up!")
elif age>= 18:
    print("You are signed up!")
elif age < 0:
    print("You haven't been born yet.")
else :
    print("You must be 18+ to sign up.")

#Here is another if statement in daily life use case.
response = input("Would you like food? (y/n): ")
if response == "y":
    print("Have some food!")
else:
    print("No food for you.If you want food you can press y.")
#I got another if statement for you

name = input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

#Math in Python
# Steve Jobs famously said "Good artists copy. Best artists steal!"
friends = 10
# friends+=1
# friends = friends -2
# friends -= 2
# friends = friends* 3
#friends *= 3
# friends = friends/2
# friends /= 2
#friends = friends ** 2
# friends **= 2 # the augmented assignment operator version of this equation
# Modulous operator is the percent sign %. It returns the remainder of any devision.
remainder = friends % 3


print(remainder)

x = 3.1413
y = -7
z = 5
# result = round(x)
# result = abs(y)
# result = pow(z,3)
#result = max(x,y,z)
result = min(x,y,z)
print(result)
import math
# print(math.pi)
# print(math.e)
x = 9.1
# result = math.sqrt(x)
# result = math.ceil(x) # ceiling function always rounds a number up
result = math.floor(x) # a floor function always rounds a number down.
print(result) 
import math
radius = float(input("Enter the radius of the circle : "))
circumference = 2 * math.pi * radius
print(f"The circumference is : {circumference}") 
import math
radius = float(input("Enter the radius of a circle (in meter) :"))
area = math.pi * pow(radius,2)
print(f"The area is : {round(area,2)} squared m") 
# Finding the hypotenus of a right angle triangle
import math
def right_angle_triangle():
    print("This is a right angle triangle.")
    print("     /|")
    print("    / |")
    print("   /  |")
    print("  c   b")
    print(" /    | ")
    print("/__a__|")
right_angle_triangle()

a = float(input("Enter side a (in cm): "))
b = float(input("Enter side b(in cm) :"))
c = math.sqrt((pow(a,2))+ pow(b,2))
print(f"Side c =  {round(c,2)} cm.") 
import numpy
import math
import matplotlib
import numpy as np

from pathlib import Path
import pandas as pd
def load_housing_data():

for_sale = False
if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")

online = False
if online:
    print("This user is online.")
else:
    print("This user is offline.")
# Python Calculator program
operator = input("Enter an operator (+ - * /) :")
num1 = float(input("Enter the 1st number : "))
num2 = float(input("Enter the 2nd number : "))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
else:
    print(f"{operator} is not a valid operator.")

# Python weight converter program
print("Hello user. You can convert your weight here.")
weight = float(input("Enter your weight : "))
unit = input("Enter the unit (K or L):")

if unit == "K":
   weight = weight * 2.205
   unit = "Lbs"
   print(f"Your weight is : {round(weight,1)} {unit}")
elif unit == "L":
   weight = weight/2.205
   unit = "Kgs"
   print(f"Your weight is : {round(weight,1)} {unit}")
else:
   print(f"{unit} is not a valid unit.")

# Temperature conversion in Python
# Copy and paste  ° degree symbol from here because it's not found in your lenovo laptop.
unit = input(" Is the temperature in Farenhight or Celsius (F/C):")
temperature = float(input("Enter the temperature : "))

if unit == "F":
    temperature = round((temperature - 32) *5 / 9,1)
    print(f"The temperature is {temperature}° Celsious")
elif unit == "C":
    temperature = round((9 * temperature) / 5 + 32, 1)
    print(f"The temperature is {temperature} ° Farenhight") 
# Logical operators = used on conditional statements.
#                     and = checks two or more conditions if True
#                     or  = checks if at least one condition is True
#                     not = True if condition is False, and vice versa
temperature = 25
if temperature >0 and temperature <30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")

temperature = float(input("Enter the temperature in Celsius : "))

if 0 < temperature < 30 :
    print(f"The current temperature is {temperature}° Celsius and it is good.")
else:
    print(f"The current temperature is {temperature}° Celsius and it is bad.")

temperature = -12

if temperature <= 0 or temperature >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")

sunny = False

if not sunny:
    print("It is sunny outside.")
else:
    print("It's cloudy outside.")

rich = "A person claimed to be the richest!"

if not rich:
    print("The person is rich")
else:
    print("The person is poor.")

# Strings method in Python
# name = input("Enter your full name : ")
# result = len(name)
# result = name.find("S")
# result = name.rfind("d")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
#result = name.isalpha()
phone_number = input("Enter your phone number :  ")
# result = phone_number.count("-")
result = phone_number.replace("-", "  ")
print(result)

print(help(str)) 

# Validate user input exercises.
# 1. Username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits
username = input("Enter a username :")

if len(username) > 12:
    print("Username can't be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces.") 
else:
    print(f"Welcome {username.upper()}") 

username = input("Enter a username :")

if len(username) > 12:
    print("Username can't be more than 12 characters.")
elif username.find(" "):
    print("Your username can't contain spaces.") 
else:
    print(f"Welcome {username.upper()}")

username = input("Enter a username :")

if len(username) > 12:
    print("Username can't be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces.") 
elif not username.isalpha():
    print("Your username can't contain digits.")
else:
    print(f"Welcome {username.upper()}")
"
# String indexing in Python.
# indexing = accessing elements of a sequence using [] (indexing operator)
#              [start : end : step]

credit_number = "3240-1232-9054-5498"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2])
# print(credit_number[3::2])
# last_digit = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digit}")
#reversing an string
credit_number = credit_number[::-1]
print(credit_number)

# Python Email slicer exercise
email = input("Enter you email :")
index = email.index("@")
user_name = email[:index] # This is an built-in index method keyword. 
domain = email[index +1 :]
print(f"Your username is {user_name} and domain is {domain}")

# alternative to the above code . It takes less lines of code
email = input("Enter you email :")
user_name = email[: email.index("@")]
domain = email[email.index("@") + 1:]
print(f"Your username is {user_name} and domain is {domain}")
# Format specifiers = {value : flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align(carrot symbol)
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space between positive numbers
# :, = comma separator

price1 = 387687.547655
price2 = -46565.675
price3 = 7098434534536547.2345

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

# While loops = execute some codes WHILE some condition remains true
name = input("Enter your name : ")
if name == "":
    print("You did not enter your name.")
else:
    print(f"Welcome {name}")

name = input("Enter your name : ")
while name == "":
    print("You did not enter your name.")
    name = input("Enter your name : ")

print(f"Welcome {name}")

age = int(input("Enter your age : "))

while age < 0:
    print("Are you okay? Age can't be negative!")
    age = int(input("Enter your age : "))
print(f"You are {age} years old.")

# Not logical operator inside of while loop
food = input("Enter a food you like(q to quit): ")

while not food == "q":
    print(f"You will be given {food}. Please wait a minute. ")
    food = input("Enter another food you like(q to quit): ")
print("You can order online anytime.")
print("To order online go to our website : www.freefood.com")

num = int(input("Enter a number between 1-10 :"))

while num <0 or num > 10:
    
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1-10 :"))
print(f"Your number is {num} ")

# ***Compound interest calculator in Python***
# For those who doesn't know well about interest- WHAT IS INTEREST?
## Interest is the monetary charge for the privilege of borrowing money. Interest expense of revenue
# ... is often expressed as a dollar amount while the interest rate is used to calculate interest...
#... is typically expressed as an anual percentage rate (APR). Interest is the amount of money 
#... a lender or financial institution receives for lending out money. Interest can also refer to the amount 
#... of ownership a stockholder has in a company, usually expressed as a percentage.
# A =P(1+r/100)^t
# A = final amount, P = initial principal balance,
#  r = interest rate, n = number of time periods elapsed
principle  = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount : "))
    if principle < 0:
        print("Priciple can't be less than zero.")
    else:
        break
while True:
    rate = float(input("Enter the interest rate : "))
    if rate < 0:
        print("Interest rate can't be less than zero.")
    else:
        break
while True:
    time = int(input("Enter the time in years : "))
    if time < 0:
        print("Time can't be less than zero.")
    else:
        break
total_balance = principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s : ${total_balance:,}")

# For Loops = execute a block of code a fixed number of times.
# You can iterate over a range, sequence, strings etc. 
for x in reversed(range(1,10)):
    print(x)
print("Happy new Year!")

for x in range(1,10,2):
    print(x)
print("Happy new Year!")

credit_card = "1234-5678-9101"

for x in credit_card:
    print(x)

for x in range(1,21):
    
    if x == 13:
        continue
    else:
        print(x)

# Nested Loop = a loop inside of another loop(outer or inner)
#               outer loop:
#                   inner loop:

for x in range(3):
    for y in range(1,10):
        print(y,end="")
    print()

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns : "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()

import time
my_time = int(input("Enter the time in seconds: "))
for x in reversed(range(0,my_time)):
    print(x)
    time.sleep(2)

print("Time's up!")

import time
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")

# PYTHON CREDIT CARD VALIDATOR PROGRAM IN PYTHON

# 1. Remove any "-" or " "
# 2.Add all digits in the odd places from right to left
# 3. Double every second digits from right to left
#                  (if result is a two digit number,
#                   add two digits number together to get a single digit.)
# 4. Sums the total of steps 2 & 3
# if sum is divisible by 10, then the credit card # is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1

card_number = input("Enter a credit card # : ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]
print(card_number)

# Step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)


# Step 3
for x in card_number[1::2]:
    x = int(x)*2
    if x >= 10:
        sum_even_digits += (1+(x % 10))
    else:
        sum_even_digits += x
# Step 4
total = sum_even_digits + sum_odd_digits

# Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")

# COLLECTION = single "variable" used to store multiple values
# LIST = ordered and changeable. Duplicates
# set = {} ordered and immutable, but add/remove. No duplicates
# Tuple = () ordered and immuatable. Dupliates. Faster

fruits = ("banana","coconut","jackfruit","mango","blackberry","coconut")
# print(fruits[::4])
#fruits[1] = "pineapple"
#for fruit in fruits:
#fruits.append("pineapple")
#fruits.remove("banana")
# fruits.insert(0,"pineapple")
# print(fruits)
 
# print(dir(fruits))
# print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
# fruits.sort()
# fruits.reverse()
# fruits.clear()
#print(fruits.index("coconut"))
# print(fruits.count("apple"))
# fruits.add("pineapple")
# fruits.remove("jackfruit")
# fruits.pop()
#fruits.clear()
# print(fruits.count("coconut"))
#print(fruits)
for fruit in fruits:
    print(fruit)

# Shopping cart program in Python
foods = []
prices = []
total = 0
while True:
    food = input("Enter a food to buy(q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food} : $"))
        foods.append(food)
        prices.append(price)
print("-----YOUR CART-----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"Your total is : ${total}")

# Python 2D collection are easy
# 1 D collections
foods=       ["apple"  , "orange" , "banana","jackfruit"]
vegetables = ["celery" , "carrots" ,"potatoes"          ]
meats =      ["chicken", "fish"    ,"turkey"            ]

# 2D list
groceries = ({"apple"  , "orange" , "banana","jackfruit"},
             {"celery" , "carrots" ,"potatoes"},
             {"chicken", "fish"    ,"turkey"})
# taking the elements found within our 2D list i am going to line this up kinds like this
# put some spaces before the arrays to line them all left-aligned
# It kind of represents a grid or Matrix with rows and columns
# Each individual list resembles a row. Each elements resembles a column
# print(groceries[0])
# print([grocerries[1]])
# print(groceries[1][2])
# print(groceries)
# print(groceries[0][0])
for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()

num_pad =((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*",0,"#"))
# This is an exmple of mumber pad in python
for row in num_pad:
    for num in row:
        print(num, end =" ")
    print()

# Python quiz game
questions = ("How many elements are there in the periodic table? :",
             "Who is the richest person in the world? :",
             "What is the secret to success in life? :",
             "What is the most abundant gas in the earth's atmosphere? :",
             "How many bones are there in the human body? :")
options = (("A. 116", "B. 117", "C. 118", "D. 119"),#1st element corresponds to my 1st question
           ("A. Elon Musk", "B. Vladimir Putin", "C. Bill Gates", "D. Jeff Bezos"),# vice versa
           ("A. Just Do it and never give up", "B. Quit", "C. Hardwork", "D. Wishing"),
           ("A. Hydrogen", "B. Oxygem", "C. Hellium", "D. Nitrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"))
answers = ("C", "A", "A", "D","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+= 1
        print("CORRECT!")
    else:
        print("INCORRECT! ")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1
print("---------------------")
print("     RESULT          ")
print("---------------------")

print("answers:", end= " ")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses :", end="")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score/ len(questions)* 100)
print(f"Your score is : {score}%") # The end of quiz game

# Dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates
capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))
# if capitals.get("Russia"):
#    print("That capital exists.")
# else:
#    print("That capital doesn't exist")
#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})
#capitals.pop("China")
#capitals.popitem()
#keys = capitals.keys()
#for key in capitals.keys():
#    print(key)
#values = capitals.values()
#for value in capitals.values():
#    print(value)
#items = capitals.items()
for key,value in capitals.items():
    print(f"{key} : {value}")

# Concession Stand program

menu = {"pizza":4.00,
        "thaipong":9.65,
        "coconut":8.76,
        "jambura":5.54,
        "usoy":11.54,
        "nonchak":15.45,
        "chambhut":12.65,
        "sayngkum":10.00}

cart = []
total =0
print("-----------MENU-----------")
# To make the customer aware of the total cost all together
sum_of_all_items = sum(menu.values())
print(f" The sum of all items is ${sum_of_all_items}")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select a food item (q to quit): ").lower()
    if food =="q":
        break
    elif food == "all":
        print(f"You ordered all food items. Your total is ${sum_of_all_items}")
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"{food} is not avaiable! Select a food item from the list.")
print("---------YOUR ORDER-----")
for food in cart:
    total+= menu.get(food)
    print(food, end= " ")
print()
print(f"Total is : ${total:.2f}")


# This is the code with fix. ALTERNATIVE-1
menu = {"pizza": 4.00,
        "thaipong": 9.65,
        "coconut": 8.76,
        "jambura": 5.54,
        "usoy": 11.54,
        "nonchak": 15.45,
        "chambhut": 12.65,
        "sayngkum": 10.00}

cart = []
total = 0

print("-----------MENU-----------")
# To make the customer aware of the total cost all together
sum_of_all_items = sum(menu.values())
print(f" The sum of all items is ${sum_of_all_items}")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select a food item (q to quit): ").lower()
    if food == "q":
        break
    elif food == "all":
        print(f"You ordered all food items. Your total is ${sum_of_all_items}")
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"{food} is not available! Select a food item from the list.")

if cart:
    print("---------YOUR ORDER-----")
    for food in cart:
        total += menu.get(food)
        print(food, end=" ")
    print()
    print(f"Total is : ${total:.2f}")
else:
    print("No items in cart")

# ALTERNATIVE-2
menu = {"pizza": 4.00,
        "thaipong": 9.65,
        "coconut": 8.76,
        "jambura": 5.54,
        "usoy": 11.54,
        "nonchak": 15.45,
        "chambhut": 12.65,
        "sayngkum": 10.00}

cart = []
total = 0

print(f"The sum of all items is {sum(value for value in menu.values())}")
print(*menu.items(), sep="\n")

while True:
    food = input("Select a food item (q to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print(f"{food} is not available!")

if cart:
    for food in cart:
        total += menu[food]
    print(*cart, sep=" ")
    print(f"Total is : {total}")
else:
    print("No items in cart")

# GENERATE RANDOM NUMBERS IN PYTHON
import random
#print(help(random)) 

low = 1
high = 100
# dice_number = random.randint(low, high)
#number = random.random()
options = ("rock","paper","scissors")
option = random.choice(options)
cards = ["2","3","4","5","6","7","8","9","10","J","Q","k","A"]
random.shuffle(cards)
print(cards)

# Number Guessing Game In Python
import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low}-{high}) : "))
    guesses += 1

    if guess > number:
        print(f"{guess} is too high.")
    elif guess < number:
        print(f"{guess} is too low.")
    else:
        print(f"{guess} is correct!")
        break
print(f"This round took you {guesses} guessess.")
    
# Rock Paper Scissors Game in Python
#                                           < Solution 1 >
import random

options = ("rock","paper","scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock,paper,scissors):  ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win! Congratulations! ")
    elif player == "paper" and computer == "rock":
        print("You win! Congratulations!")
    elif player == "scissors" and computer == "paper":
        print("You win. Congratulations!")
    else:
        print("You lose!")

    if not input("Play again?(y/n):").lower() == "y":
        running = False
    else:
        continue
print("Thanks for playing.")
"""
#                                     <  Solution 2  >
import random

options = ("rock", "paper", "scissors")

while True:
    player = input("Enter a choice (rock, paper, scissors): ")
    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win! Congratulations!")
    else:
        print("You lose!")

    if input("Play again? (y/n): ").lower() != "y":
        break

print("Thanks for playing.")



    
