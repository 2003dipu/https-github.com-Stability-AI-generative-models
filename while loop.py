print("Master the basics of while loop")

def generate_ordinal_number(number):
    if number % 100 in range (11,20):
        return f"{number}th"
    else :
        suffixes = {1: "st", 2: "nd", 3:"rd"}
        return f"{number}{suffixes.get(number % 10,'th')}"
    n = 0
    while n < 30:
        ordinal_number = generate_ordinal_number(n+1)
        print(f"{ordinal_number} line of while loop prints {n}")
        n += 1
print("If you understand this while loop, then you are a master of while loop")