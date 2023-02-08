#uppg 3
n = int(input())
print(' ' + n * '___')
for i in range(n):
    print('|' + n * '   ' + '|')
print(' ' + n * '___')
# | är längre än _ så man måste ta flera _ för att det ska bli en kvadrat och inte en rektangel