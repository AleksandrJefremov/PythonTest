list2 = [123, 234, 345, 456, 567]
list1 = list2.copy()
print(list1)
counter = 0
#setup

list1.append([2, 3, 43, 342])
print('append: ', list1)
list1 = list2.copy()
list1.extend([2, 3, 43, 342])
print('extend: ', list1)
#append lägger till ett element, extend kan lägga till flera individuella element

list1 = list2.copy()
print('back to the original list')
print(list1)
list1.remove(123)
print('remove: ', list1)
list1 = list2.copy()
list1.pop(0)
print('pop: ', list1)
#pop behöver index, remove behöver exakt värde

list1 = list2.copy()
print('back to the original list\n', list1)
print('len(): ', len(list1))
for i in list1:
    counter = counter + 1

print('using a for loop: ', counter)
