# Python higher order function = a function that either
#             1. accepts a function as an argument or
#             2. returns a function
#           ( in python functions are also treated as objects)
# example -1
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
# example -2

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))
