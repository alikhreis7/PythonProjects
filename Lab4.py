##############################################################
#Exercise 1: The average
##############################################################

def Average(lst):
    return sum(lst) / len(lst)
  
lst = [ ]
n = int(input("Enter number of elements : "))
print('Enter the elements')

for i in range(0,n):
    lst.append(int(input()))

average = Average(lst)
  
print("Average of the list =", round(average, 2))

##############################################################
#Exercise 2: Statistics calculations
##############################################################

def min_max_average(marks):
    min_value, max_value, average = marks[0], marks[0], 0
    for num in marks:
        average += num
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    average /= len(marks)
    return min_value, max_value, average


def main():
    n = int(input("How many marks do you want to enter? "))
    marks = []
    for i in range(n):
        marks.append(float(input("Enter a score: ")))
    min_value, max_value, average = min_max_average(marks)
    print("Min value is", min_value)
    print("Max value is", max_value)
    print("Average marks is", average)


main()

##############################################################
#Exercise 3: Ball Toss
##############################################################

import math


def function(v):
  
    dist = [0]*10
    g = 9.8
  
    
    for i in range(0,10):
  
        thetaR = math.pi*i*10/180
        distance = 2*v*v*math.cos(thetaR)*math.sin(thetaR)/g
        dist[i] = "{:.2f}".format(distance)
  
    
    return dist


v = float(input("Enter velocity: "))


print("Distance in meter per second :",function(v))

##############################################################
#Exercise 4: Standard Deviation
##############################################################

def standard_deviation(lst):
    m = sum(lst) / len(lst)
    total = 0
    for num in lst:
        total += (num - m) ** 2
    return (total / (len(lst) - 1)) ** 0.5


def main():
    n = int(input("How many numbers do you want to enter? "))
    lst = []
    for i in range(n):
        lst.append(float(input("Enter a number: ")))
    print("Standard deviation is", standard_deviation(lst))


main()                                                                             

