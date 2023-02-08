list1 =['Adam', 'Elis', 'Jonas', 'Mark', 'William']
print('list1 = ', list1)
list2 = list1.copy()
list2.reverse()
print('list2 = ', list2)
element1 = list2[0]
list1.insert(2, element1)
print('list1 = ', list1)
print('list1 har', list1.count(element1), element1)