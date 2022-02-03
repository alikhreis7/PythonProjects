

def number_divisible(lst, w):
    num = 0
    for i in lst:
        if(i%w==0):
            num += 1
    return num

if __name__ == '__main__':
    s = input("Please input a list of numbers separated by spaces: ")
    lst = [int(x) for x in s.split(" ")]
    w = int(input("Please input an integer: "))
    print("The number of elements divisible by",w,"is",number_divisible(lst,w))
