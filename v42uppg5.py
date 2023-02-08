#uppg 5
n = int(input('skriv en int: '))
m = int(input('skriv en till int: '))

def adder(n, m):
    h = max(n, m)
    l = min(n, m)
    sum = 0
    for i in range(h - l):
        sum += i + l
    return sum

print(adder(n, m))