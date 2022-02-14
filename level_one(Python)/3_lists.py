# lists
mylist1 = [1, 2, 3, 4]
mylist2 = ["string", 1, 2, 3.2, ["asf", 1, 2]]
print(mylist2)

#splice works in similar fashion
mylist3 = ['a', 'b', 'c', 'd', 'e']
print(mylist3)
mylist3[0] = 'New Item' #Lists are mutable
print(mylist3)

#function-append
print('function - append')
mylist4 = ['d', 'e', 'f']
mylist4.append('new item')
print(mylist4)
#function-extend
mylist4.extend(mylist3)
print(mylist4)
#function pop
item = mylist4.pop() #can also specify index position in pop()
print(item)
print(mylist4)
#function reverse
mylist4.reverse()
print(mylist4) #inplace reverse
#function sort
mylist4.sort()
print(mylist4)

# nested list index
mylist5 = [1, 2, ['x', 'y', 'z']]
print(mylist5[2][1])

# List comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0])
first_col = [row[0] for row in matrix]
print(first_col)
