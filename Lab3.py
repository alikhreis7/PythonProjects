######################################
#EXERCISE 1
######################################

##Logical errors:
##
##Counter variable is not initialized
##There should be loop construct to print values from 10 to 1
##The value of counter variable should be decremented to print 10 to 1


##Correct Code :

counter = 10
while counter > 0:
    print(counter)
    counter = counter -1

########################################
###EXERCISE 2
########################################

#Using While Loop

# Function implementation of the algorithm
def printNumbers(n):
    i = 1
    # Looping from 1 to n
    while(i<=n):
        # Printing value of i
        print(i)
        i += 1

# Reading number
n = int(input("Enter value for N: "))
printNumbers(n)

#Using For Loop

# Function implementation of the algorithm
def printNumbers(n):
    # Looping from 1 to n
    for i in range(1,n+1):
        # Printing value of i
        print(i)

# Reading number
n = int(input("Enter value for N: "))
printNumbers(n)

######################################
#EXERCISE 3
######################################

import random

def guess(randNum):

    numberOfGuess = 0

    while True:

        userGuess = int(input("Enter a number between 1 and 10: "))

        if userGuess == randNum:

            print("Congratualtions, you have guessed correctly in", numberOfGuess, "attempts")

            break

        elif userGuess < randNum:

            print("Your guess is too low, try again...")

        else:

            print("Your guess is too high, try again...")

randNum = random.randint(1, 10)

guess(randNum)

######################################
#EXERCISE 4
######################################
import sys
#method to compute factorial
def computeFact(n):
  
    #assigning fact as 1
    fact=1
  
    # if n is zero return 1, exception condition
    if n==0:
        return 1;
    if n<0:
        print('The integer should not be negative, it is always positive')
        print('GOODBYE')
        sys.exit()
  
    # iterate i from 1 to n, multiply fact with i and store result in fact
    for i in range(1,n+1):
        fact = fact*i
  
    #return the factorial
    return fact
  
#input of non-negative integer
n = int(input("Enter a non-negative integer: "))

#calling computeFact() and printing result
print("Factorial of ",n," is ",computeFact(n))
