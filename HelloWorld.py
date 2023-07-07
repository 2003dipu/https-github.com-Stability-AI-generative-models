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
    I order salad.  """
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
    print("No food for you.")
#I got another if statement for you

name = input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")
