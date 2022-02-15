#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True
def arrayCheck(nums):
    no_dup = []
    for values in nums:
        if values not in no_dup:
            no_dup.append(values)
    op1 = False
    op2 = False
    op3 = False
    for values in no_dup:
        print(values)
        if values == 1:
            op1 = True
        if values == 2:
            op2 = True
        if values == 3:
            op3 = True
    return op1 and op2 and op3
ret = arrayCheck([1, 1, 2, 1, 2, 3])
print(ret)



#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
    str_even = []
    for k in range(0,len(str),2):
        str_even.append(str[k])
    return ''.join(str_even)

ret1 = stringBits('Heeololeo')
print(ret1)

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# len_a = 5 (0-4) len_b = 3 (0-2) len_a-len_b = 2 (0-1)
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    result = False
    a = a.lower()
    b = b.lower()
    #print(a)
    #print(b)
    len_a = len(a)
    len_b = len(b)
    #print(len_a)
    #print(len_b)
# end_other('Hiabc', 'abc')
# len_a = 5 (0-4) len_b = 3 (0-2) len_a-len_b = 2 (0-1)
    if len_a > len_b: #5 > 3
        match = len_a - len_b #5-3 = 2
        #print("match : {}".format(match))
        a = a[match:] #(2:)
        #print("b : {}".format(b))
        #print("a : {}".format(a))
        if a == b:
            return True
        else:
            return False
    elif len_a < len_b:
        match = len_b - len_a
        b = b[match:]
        if a == b:
            return True
        else:
            return False

ret3 = end_other('AbC', 'HiaBc')
print("Return 3 : {}".format(ret3))


  # CODE GOES HERE

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
    str_dob = []
    j = 0
    for i in range(0, len(str)):
        str_dob.append(str[i])
        str_dob.append(str[i])
    return ''.join(str_dob)

ret2 = doubleChar("LALIT")
print(ret2)

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    a_ret = fix_teen(a)
    b_ret = fix_teen(b)
    c_ret = fix_teen(c)
    return a_ret + b_ret + c_ret


def fix_teen(n):
    if n >= 13 and n <= 19:
        if n == 15 and n == 16:
            return n
        else:
            return 0
    else:
        return n

#ret4 = fix_teen(15)
#print("RETURN FOUR : {}".format(ret4))

# no_teen_sum(1, 2, 3)
ret5 = no_teen_sum(2, 13, 1)
#no_teen_sum(2, 1, 14)
print("RETURN 5 : {} ".format(ret5))


#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for values in nums:
        if values%2 == 0:
            count = count+1
    return count
result = count_evens([2, 1, 2, 3, 4])
print(result)
