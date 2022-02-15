###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
#print(digits)
random.shuffle(digits)
#print(digits[:3])
gen_digits = digits[:3]
# print(type(gen_digits))
# print("gen_digit[0] : {} ".format(gen_digits[0]))
# print("gen_digit[1] : {} ".format(gen_digits[1]))
# print("gen_digit[2] : {} ".format(gen_digits[2]))
gen_digits[0] = str(gen_digits[0])
gen_digits[1] = str(gen_digits[1])
gen_digits[2] = str(gen_digits[2])
print("Gen_Digits : {}".format(gen_digits))
# Another hint:

guess = list(input("What is your guess? "))
# print(type(guess))
# print("guess[0] : {} ".format(guess[0]))
# print("guess[1] : {} ".format(guess[1]))
# print("guess[2] : {} ".format(guess[2]))
#
#
# print("Guess : {}".format(guess))

def match_fun():
    if guess[0] != gen_digits[0] and guess[1] != gen_digits[1] and guess[2] != gen_digits[2]:
        print("Nope!")
    elif (guess[0] == gen_digit[0] or guess[1] == gen_digit[1] or guess[2] == gen_digit[2]) and

        print("Match!")
    elif ( (guess[1] == guess[0] or guess[2] == guess[0]) or
    (guess[0] == guess[1] or guess[2] == guess[1]) or
    (guess[0] == guess[2] or guess[1] == guess[2]) ):
        print("Close!")
    elif (guess[0] == gen_digits[0] and guess[1] == gen_digits[1] and guess[2] == gen_digits[2]):
        print("Correct!")
        break



# 297 / 100 = 2 first
# 297 % 100 = 97
# 97 / 10 = 9 second
# 97 % 10 = 7 third

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
