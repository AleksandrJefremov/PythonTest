ord = input('Skriv din mening här:\n\t').lower()
ord2 = ord.split()
print('\nDin mening har  ', len(ord2), ' ord\n')

print('Sista "a" har indexen ', ord.rindex('a'))

if ord[-1:] == '.':
    print('\nDin mening slutar med punkt')
else:
    print('\nDin mening slutar inte med punkt')

print('\nJag ändrar din mening från "', ord, '" till ')

ord = ord.capitalize().swapcase()

print(ord)