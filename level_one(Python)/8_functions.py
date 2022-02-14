# function with default value
def my_func(param1="default"):
    print("hello : {}".format(param1))

my_func()

# function with doc string
def my_func1(param2="default1"):
    """
    FUNCTION EXPLANATION : DOCS-STRING
    """
    print("hello : {}".format(param2))

my_func1();

# function with return value
def my_func2():
    return "Hello!!"

ret_val = my_func2()
print(ret_val)

# addition functions
# make sure to check type of input to function
def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1+num2
    else:
        return "NULL"

ret_val2 = addNum(10, 20)
print(ret_val2)

ret_val3 = addNum('10', 20)
print(ret_val3)

# lambda experssion
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_bool(num):
    return num%2 == 0

lambda num: num%2 == 0

# filter function(function, list)
even = filter(even_bool, mylist)
print(list(even))

even1 = filter(lambda num: num%2 == 0, mylist)
print(list(even1))

# other useful functions
str = 'hello #morning'
#.lower()
#.upper()
#.split()
result = str.split('#')[1]
print(result)

# IN functions
print('x' in [1, 2, 3, 'x'])
