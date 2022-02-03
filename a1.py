




#########################################################
# Question 1
##########################################################

def poem_generator():
    '''This has two inputs to be put in and it will generate at poem, the inputs have to be name and the city of birth'''
    print('poem_generator()')
    name = input('Please enter your name:')
    cob = input('Enter your city of Birth:')
    print('There once was a person from ' + cob, '\nTheir name was ' + name,
          '\nThey desperately wanted to fly.\nBut whenever they flapped,\n' + name + ' got so chapped, \nthat poor '
                                                                                     'person from ' + cob)
poem_generator()

#####################################################
## Question 2
#####################################################

def impl2loz(w):
    '''imp2loz is taking a non-negative number which is w as input and is returning (l,o)'''
    l = int(w)
    decimalPart = w-l
    o = 16*decimalPart
    return(l,o)

###############################################
## Question 3
############################################

def pale(n):
    '''pale is taking a positive integer n as input but n has only four digits, the function demonstrates if n is a pale number'''
    m1 = (n // 10) % 100
    m2 = n % 100
    m3 = n // 100
    ld = n % 10
    c1 = (m1 == 33, m2 == 33, m3 == 33)
    c2 = (ld % 4 == 0)
    final_result = (c1 == False) or (c2 == False)
    return final_result
    

#############################################
## Question 4
############################################

def bibformat(author='George R. R. Martin', title='A Game of Thrones', city='New York city', publisher='Bantam Spectra', year='1996'):
    '''bibformat has parameters of 5 different things and are set to something, then it will print them in an orderly fashion'''
    print(' bibformat("George R. R. Martin","A Game of Thrones","New York city", "Bantam Spectra", "1996" ')
    print(" '{0}({1}). {2}. {3}: {4}' ".format(author, year, title, city, publisher))
bibformat()

#############################################
## Question 5
############################################

def bibformat_display():
    '''this function will take five inputs, four of them need to be strings and one is a number and will print them in an orderly fashion'''
    print('bibformat_display()')
    title = input("Enter the title of book: ")
    author = input("Enter the name of the author: ")
    year = input("What year was the book published? ")
    publisher = input("Enter the name of the publisher: ")
    city = input("In what city are the headquaters of the publisher? ")
    print("{0}({1}). {2}. {3}: {4}".format(author, year, title, city, publisher))

bibformat_display()

#############################################
## Question 6
############################################

def compound(x,y,z):
    '''this function takes an input three integers and returns true if x is the only even number or all gretater than 100 then it is false'''
    return (x % 2 == 0 and y % 2 != 0 and z % 2 != 0) and (x+y > 100 or x+z> 100 or y+z> 100)


#############################################
## Question 7
############################################

import math
def funct(p):
    '''we rearrange the given equation and we get r= sqrt(log5(p-10)), the following function will determine r using math'''
    print(f"The solution is {math.sqrt(math.log(p - 10, 5))}")

#############################################
## Question 8
############################################
import math
def gol(n):
    '''The main logic in this function is that we need to find a power of 2 such that its more than n i,e
    2k>=n, which can be done by taking ceil i,e nearest integer value of log2n'''
    return math.ceil(math.log(n,2))


#############################################
## Question 9
############################################

def cad_cashier(price, payment):
    '''this function is taking two  non-negative numbers iwth two decimal in  payment 0 or 5. this function has to return a real number
    with 2 decimal places representing the change the customer should get''' 
    price = round(price / 5, 2) * 5
    val = round(payment - price, 2)
    return val

#############################################
## Question 10
############################################

def cad_cashier(price, payment):
    '''this function is taking two  non-negative numbers iwth two decimal in  payment 0 or 5. this function has to return a real number
    with 2 decimal places representing the change the customer should get'''
    price = round(price / 5, 2) * 5
    val = round((payment - price), 2)
    return val


def min_CAD_coins(price,payment):
    '''In this function, we have to find the minimum number of toonies,
    loonies, quarters, dimes and nickels for the change. To find the minimum number of coins,
    we have to give out the coins with highest values first.
    Find the number of toonies that can fit in the change, and subract this amount from change. then,
    find the number of loonies that can fit in the new change and deduct that amount from change which we did below.'''
    change = cad_cashier(price,payment)
    t = change//2
    change = round(change - 2*t,2)
    l = change//1
    change = round(change - l,2)
    q = change//0.25
    change = round(change - 0.25*q,2)
    d = change//0.10
    change = round(change - 0.10*d,2)
    n = change//0.05

    return (t,l,q,d,n)

