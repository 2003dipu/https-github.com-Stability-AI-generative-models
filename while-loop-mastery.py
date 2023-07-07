# After learning this while loop you will be the master of while loop and the deep understanding of while loop will enable you to do impossible possible

def ordinal(n) :
    ordinal_endings = {
        1: "st",
        2: "nd",
        3: "rd",
        4: "th",
    }
    if 11 <= n <= 13:
        return f"{n}{ordinal_endings[n % 10]}"
    else:
        return f"{n}{ordinal_endings.get(n % 10, 'th')}"

n = 0
while n < 100:
    ordinal_number = ordinal(n)
    print(f"{ordinal_number} line of while loop prints {n}", end = "\n")
    n +=1