def ordinal(n):
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = suffixes.get(n % 10, 'th')
    return str(n) + suffix

n = 0
while n < 51:
    ordinal_number = ordinal(n)
    print(f"{ordinal_number} line of while loop prints {n}")
    n += 1
