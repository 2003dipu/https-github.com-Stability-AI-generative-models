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
"""
# while loop
n = 0
while n <5 :
    print(f" First While loop prints {n}")
    print(f" Second While loop prints {n}")
    n = n + 1
