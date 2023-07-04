# After learning this while loop you will be the master of while loop and the deep understanding of while loop will enable you to do impossible possible

def ordinal(n) :
    ordinal_endings = {
        1 : "est",
        2 : "nd",
        3 : "rd",
        4 : "th",
    }
    if 11 <= n <= 13 :
        return f"{n}{ordinal_endings[n % 10]}"
    else :
        return f"{n}th"
n = 0
while n < 100 :
    ordinal_number = ordinal(n)
    print(f"{ordinal_number} line of while loop prints {n}", end = "\n")
    n +=1
# The above codes will print this :
0th line of while loop prints 0
1st line of while loop prints 1
2nd line of while loop prints 2
3rd line of while loop prints 3
4th line of while loop prints 4
5th line of while loop prints 5
6th line of while loop prints 6
7th line of while loop prints 7
8th line of while loop prints 8
9th line of while loop prints 9
10th line of while loop prints 10
11th line of while loop prints 11
12th line of while loop prints 12
13th line of while loop prints 13
14th line of while loop prints 14
15th line of while loop prints 15
16th line of while loop prints 16
17th line of while loop prints 17
18th line of while loop prints 18
19th line of while loop prints 19
20th line of while loop prints 20
21st line of while loop prints 21
22nd line of while loop prints 22
23rd line of while loop prints 23
24th line of while loop prints 24
25th line of while loop prints 25
26th line of while loop prints 26
27th line of while loop prints 27
28th line of while loop prints 28
29th line of while loop prints 29

