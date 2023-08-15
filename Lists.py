#LISTS DS
# mutable

list1 = [ 1, 2, 3,'freeze']

#methods --> append, extend, insert

list1.append('leave')
print(list1)

list1.extend((2,0))
print(list1)

list1.insert(2, 'telephone')
print(list1)

del list1[2]
print(list1)

# removes from top of the list -- last added element
a = list1.pop()
print(a)

list1.remove(1)
print(list1)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

b = list2.sort()


print(list2.index(9))
print(list2.count(1))