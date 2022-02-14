print(1=='1') #False
print(1==1) #True

# Logical operator : and, or
print(1<2 and 2<3)
print(2>1 or 2<1)

# if
if 1<2:
    print("Yes!")

# nested if
if 2<3:
    if 3<4:
        print("True!")

# if-else
if 2<3:
    print("2<3")
else:
    print("2!<3")

# if-elif-else

# for loop
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in seq:
    # code here
    print(item)

d = {'Sam':1, 'Frank':2, 'Dan':3}
for names in d:
    print(names) # print keys only not value

for keys in d:
    print(keys)
    print(d[keys])

# tuple iterations
mypairs = [(1, 2), (3, 4), (5, 6)]
for tup in mypairs:
    print(tup)

# tuple unpacking
for (tup1, tup2) in mypairs:
    print(tup1)
    print(tup2)

# while loops
i = 1
while i<5:
    print("value of i is : {}".format(i))
    i = i + 1

# in-built function in python
# range functions
print(range(5))
print(list(range(0,5)))
print(list(range(0, 20, 2))) #(including-min, upto-max, step-size)

#list comprehension
x = [1, 2, 3, 4]
out = []

for val in x:
    out.append(val**2)

print(x)
print(out)

# another-method
out = [num ** 2 for num in x]
print(out)
