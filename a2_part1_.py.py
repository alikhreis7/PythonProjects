

import math
import random

def primary_school_quiz(flag, n):
    '''(number,number)->number
        Preconditions: flag is a positive integer
        Returns number of correct answers given flag and n'''
    if flag==1:
        num1=0
        num2=0
        correct=0
        for i in range(n):
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            ans=pow(num1,num2)
            question=int(input('Question '+str(i+1)+':'+'\nWhat is the result of: '+str(num1)+'^'+str(num2)+' '))
            if ans==question:
                correct=correct+1
        return(correct)
    elif flag==0: 
        num1=0
        num2=0
        correct=0
        for i in range(n):
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            ans=num1-num2
            question=int(input('Question '+str(i+1)+':'+'\nWhat is the result of: '+str(num1)+'-'+str(num2)+' '))
            if ans==question:
                correct=correct+1
        return(correct)

def high_school_eqsolver(a,b,c):
    '''(number,number,number)->string
        Preconditions: a b c are real numbers
        Returns equation first and then prints solutions given a b c'''
    discriminant=b**2-4*a*c
    if a==0 and b==0 and c==0:
        print('The quadratic equation '+str(a)+'·x + '+str(c)+' = 0 is satisfied for all numbers x')
    elif a==0 and b==0:
        print('The quadratic equation '+str(a)+'·x + '+str(c)+' = 0 is satisfied for no numbers x')
    elif a==0:
        sol=-c/b
        print('The linear equation '+str(b)+'x + '+str(c)+' = 0 has the following root/solution: '+str(sol))
    elif discriminant>0:
        root1=(-b+math.sqrt(discriminant))/(2*a)
        root2=(-b-math.sqrt(discriminant))/(2*a)
        print('The quadratic equation '+str(a)+'·x^2 + '+str(b)+'x + '+str(c)+' = 0 has the following real roots:\n'+str(root1)+' and '+str(root2))
    elif discriminant<0:
        root1=-b/(2*a)
        root2='i '+str(math.sqrt(abs(b**2-4*a*c))/(2*a))
        print('The quadratic equation '+str(a)+'·x^2 + '+str(b)+'x + '+str(c)+' = 0 has the following two complex roots:\n'+str(root1)+' + '+root2+' and '+str(root1)+' - '+root2)
        
    elif discriminant==0:
        root1=(-b+math.sqrt(discriminant))/(2*a)
        print('The quadratic equation '+str(a)+'·x^2 + '+str(b)+'x + '+str(c)+' = 0 has only one soluttion, a real root '+str(root1))
print(high_school_eqsolver(3,2,15))


# main
print('*********************************************************')
print('*\t\t\t\t\t\t\t*')
print('*__Welcome to my math quiz-generator / equation-solver__*')
print('*\t\t\t\t\t\t\t*')
print('*********************************************************')

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    x = len(name)+70
    print("*"+("*")*x+"*")
    print("*"+(" ")*x+"*")
    print("* __"+name+", welcome to my math quiz-generator for primary school students.__ *")
    print("*"+(" ")*x+"*")
    print("*"+("*")*x+"*") 
    question=int(input(name+' what would you like to practice? Enter\n0 for subtraction\n1 for exponentiation\n')) 
    if question==0:
        numOfQues=int(input('How many practice questions would you like to do? '))
        correct=primary_school_quiz(0,numOfQues)
    else:
        numOfQues=int(input('How many practice questions would you like to do? '))
        correct=primary_school_quiz(1,numOfQues)
    score=(correct/numOfQues)*100
    if score>=90:
        print('Congratulations '+name+"! You'll probably get an A tomorrow. Now go eat dinner and go to sleep.")
    elif score>=70:
        print('You did well '+name+', but I know you can do better.')
    else:
        print('I think you need some more practice '+name+'.')
        
elif status=='2':
    x = len(name)+57
    print("*"+("*")*x+"*")
    print("*"+(" ")*x+"*")
    print("* __quadratic equation, a·x^2 + b·x + c= 0, solver for "+name+'__ *')
    print("*"+(" ")*x+"*")
    print("*"+("*")*x+"*") 

    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        question=question.lower()
        question=question.strip()
        
        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a=float(input('Enter a number the coefficient a: '))
            b=float(input('Enter a number the coefficient b: '))
            c=float(input('Enter a number the coefficient c: '))
            high_school_eqsolver(a,b,c)
 
else:
    print(name+' you are not a target audience for this software. ')

print("Good bye "+name+"!")

