#############################################################
#Excersice 1
#############################################################


def check(age):
   if age>=18 and age<=55:
       return True
   else:
       return False

age=int(input("Enter your age: "))
if(check(age)):
   print("Transaction accepted")
else:
   print("Transaction refused")


#############################################################
#Excersice 2
#############################################################


temp = int(input("Enter temperature: "))
activityNumber = 0
if(temp >= 80.0):
    activityNumber = 1
elif(temp>=60.0):
    activityNumber = 2
elif(temp>=40.0):
    activityNumber = 3
else:
    activityNumber = 4
if(activityNumber == 1):
    print("Swimming")
elif(activityNumber==2):
    print("Soccer")
elif(activityNumber==3):
    print("Volleyball")
else:
    print("Skying")


#############################################################
#Excersice 3
#############################################################


def isDivisible(check):
    if check % 2 == 0 and check % 3 == 0:  # checking if the number is divisible by both 2 and 3, example 6 or 12.
        return 1
    elif check % 2 == 0 or check % 3 == 0:  # checking if the number is divisible by 2 or 3, example 4 or 9
        return 2
    else:  # if the number is not divisible by either 2 and 3, example 7,5,11 etc.
        return 0


number = int(input("Enter an integer: "))  # asking the user to enter an integer number converting it to integer.
print(isDivisible(number))  # calling the isDivisible method and printing the result returned.



#############################################################    
#Excersice 4
#############################################################


import math
#Functio to return determinant value
def findDeterminant(a,b,c):
    return math.pow(b,2)-(4*a*c)
#Function to find root
def findRoot(a,b,c,determinant):
    #Determinant<0 condition
    if(determinant<0):
        print('The quadratic equation ',a,'x^2+',b,'x+',c,' has no real roots')
    #Determinant=0 condition
    elif(determinant==0):
        print('The quadratic equation ',a,'x^2+',b,'x+',c,' has 1 real roots')
        root=(-b+math.sqrt(determinant))/(2*a)
        print('Root1 = Root2 = ',root)
    #Determinant>0 condition
    else:
        root1=(-b + math.sqrt(determinant)) / (2*a);
        root2 =(-b -math.sqrt(determinant)) / (2*a);
        print('The quadratic equation ',a,'x^2+',b,'x+',c,' has 2 distinct real roots')
        print('Root1 = ',root1,' and Root2 = ',root2)
#Main function for input
def main():
    a=float(input('Enter the value of coefficient a : '))
    b=float(input('Enter the value of coefficient b : '))
    c=float(input('Enter the value of coefficient c : '))
    findRoot(a,b,c,(findDeterminant(a,b,c)))
main()
