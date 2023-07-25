# walrus operator := 
# assignment operator aka walrus operator
# assigns values to variables as part of a larger expression
# new to Python 3.8
# Here's an example of why walrus operator would be useful
#happy = True
#print(happy)
#print(happy := True)
foods = list()
while food := input("What food do you like? :") != "quit":
    foods.append(food)
