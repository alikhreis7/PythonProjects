

import math

###################################
# Question 2.1
###################################
def sum_odd_divisors(n):
    """(int)->sum
        This function tankes an integer n as inputand calculates all the positive
        odd divisor of n."""
    sumodd = 0
    if n == 0:
        return None
    else:
        if n < 0:
            n = -n
        for i in range(1, n+1):
            if n % i == 0 and n % 2 != 0 :
                sumodd = sumodd + i;
                
    return sumodd
###################################
# Question 2.2
###################################

def series_sum(n):
    """(none)->number
    This function calculates the sum of all the terms up to and including n,
    then adds 1000 to it. The equaiton for the sum is from the Basel problem"""
    if(n<0):
        return None
    else:
        sum=1000
        for i in range(1,n+1):
            sum=sum+(1/i**2)
    return sum
n=int(input("please enter a non-negative integer:"))
print(series_sum(n))

###################################
# Question 2.3
###################################
 

def pell(n):
    '''(int)->int
    Precondition: n must be an integer that is greater than 0
    This function returns the nth Pell number
    '''

    if n<0:
        return None
    elif n==0 or n==1:
        return n
    else:
        p_1=1
        p_2=0
        dig=0

        for i in range(1,n):
            dig=p_1
            p_1=2*p_1+p_2
            p_2=dig
        return (p_1)

#####################################
### Question 2.4
#####################################
 

def countMembers(s):
    '''(str)->int
    Preconditon: s must be a string
    This function searches a string for the number of extraordinary characters it contains and returns that integer
    '''
    x=0
    for i in s:
        if i in 'efghijFGHIJKLMNOPQRSTUVWX23456,\!':
            x+=1
    return(x)

#####################################
### Question 2.5
#####################################
 

def casual_number(s):
      a6= ""
      flag = 0

      for i in range((len(s))):
          
           if ( s[i] == ',') :
              a6 = a6
           elif ( s[i].isdigit() ) :
              a6 = a6 + s[i]
              flag = 1
           elif ( s[i] == '-' ) :
              a6 = a6 + s[i]  
           else :
              return None
          
      if flag == 1:
         return a6
      else :
         return None
     
#####################################
### Question 2.6
#####################################
 
        
def alienNumbers(s):
    ''' (str)->int
    Preconditions: the string must only include the characters T,y,!,a,N,U
    This function returns the sum of numerical values of these characaters using string methods
    '''
    a = s.count('T')*1024
    b = s.count('y')*598
    c = s.count('!')*121
    d = s.count('a')*42
    e = s.count('N')*6
    f = s.count('U')*1
    return a+b+c+d+e+f

#####################################
### Question 2.7
#####################################
def alienNumbers(s):
    if s == "T":
        return 1024
    elif s == 'y':
        return 598
    elif s == '!':
        return 121
    elif s == 'a':
        return 42
    elif s == 'N':
        return 6
    elif s == 'U':
        return 1

def alienNumbersAgain(s):
    ''' (str)->int
        Precondition: the string must only include the characters T,y,!,a,N,U
        This function returns the sum of numerical values of these characaters using string methods'''
    num = 0
    i = 0
    counter = 0
  

    for i in s:
        counter += 1
    i=0

    while i < counter :
        num += alienNumbers(s[i])
        i = i+1
    return num

#####################################
### Question 2.8
#####################################
 

def encrypt(s):
    ''' (str)-> str
    Precondition: s must be a string
    This function returns a string which encrypts an inputted string in the form last character, first character, second last character, second character and so on
    '''
    l= []
    for i in range (len(s)):
        l.append (s[len(s)-(i+1)])
        l.append (s[i])
    return ("".join(l[:len(s)]))

#####################################
### Question 2.9
#####################################


def weaveop(s):
    op = []                
    if len(s)<=1:           
        return s            
    s=list(zip(s,s[1:]))    
    op.append(s[0][0])      
    for value in s:          
        if not value[0].isalpha() or not value[1].isalpha(): 
            op.append(value[1])  
            continue;             
        if value[0].isupper() :   
            op.append("O")       
        else:
            op.append("o")       
        if value[1].isupper():    
            op.append("P")
        else:
            op.append("p")      
        op.append(value[1])     
        
    return "".join(op)   
                
   
#####################################
### Question 2.10
#####################################

def squarefree(s):
    """(str) -> bool
    Preconditions: s must be a string that does not contain any spaces.
    This function returns whether a string contains a subword that consecutively appears in the string
    """
    flag = True 
    for i in range(len(s)):
            for j in range(i,len(s)):
                string1 = (s[i:j].strip())
                string2 = s[j:2*j-i].strip()
                if (string1 != "" and string2 != "" and string1==string2):
                    flag = False
    return (flag)
