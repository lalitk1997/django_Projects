'hello'
"hello"
"I've a dog."
mystring = 'abcdefg'
print(mystring)
print(mystring[0])
#slicing
print(mystring[:]) #print complete strings
print(mystring[2:]) #including index 2 till end of strings
print(mystring[:3]) #from index 0 upto index 3 (not including 3)
print(mystring[::2]) #step-size = 2

#strings are immutable : cannot update a character in a string
#mystring[2] = 'x' #error

up_mystr = mystring.upper()
print(up_mystr)

lo_mystr = mystring.lower()
print(lo_mystr)

first_mystr = mystring.capitalize()
print(first_mystr)

my_str_split = "Hello World"
print(my_str_split.split(" "))

#print formatting
x = "Item One : {} Item Two : {}".format("dog", "cat")
print(x)

y = "Item One : {y} Item Two : {x}".format(x="Dog", y="Cat")
print(y)
