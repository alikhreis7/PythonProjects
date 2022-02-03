

def is_up_monotone(N, d):
    
    """(str) + (str) -> (str)
    This function splits string N in sets of d
    Preconditions: N and d are strings, that are integers."""
    
    s=""
    d = int(d)
    i=0
    for char in range(0, len(N)+1, d):
        if (char==0):
            pass
        elif (char!=0 and char < len(N)+1):
            s+=N[i:char]+','+" "
            i=char
        elif (char == len(N)+1):
            s+=N[i:char]
    if (N[0:d] >N[(len(N))-d:len(N)]):
                print("This sequence is not up-monotone")
    elif (N[0:d] <= N[(len(N))-d:len(N)]):
                print("This sequence is up-monotone")

    return s

print("****************************************")
print("*                                      *")
print("*  __Welcome to up-monotone inquiry__  *")
print("*                                      *")
print("****************************************")
print("")
    
name = (input("What is your name? "))
name = name.replace("  ","")
x = len(name)+51
y = len(name)+20

print((x)*("*"))
print("*" + (" "*(x-2))+("*"))
print("*  __"+((name)+", welcome to up-monotone inquiry.__  "+("*")))
print("*" + (" "*(x-2))+("*"))
print((x)*("*"))

flag=True
while flag:
    question=input(name+", would you like to test if a number admits an up-monotone split of given size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag = False
        print((y)*("*"))
        print("*" + (" "*(y-2))+("*"))
        print("*  " + ("__ Good bye "+(name)+"!__ "+("*")))
        print("*" + (" "*(y-2))+("*"))
        print((y)*("*"))
    elif (question == "yes"):
        flag = True
        print("Good choice!")
        a =''
        N = input("Enter a positive integer: ")
        N = str(N)
        N = N.replace(" ","")
        if  N.isdigit()== False:
            print (" The input can only contain digits. Try again. ")
        elif (round(float(N)) != float(N)):
            print (" The input can only contain digits. Try again. ")
        elif (float(N) <= 0):
            print ("The input has to be a postive integer. Try again.")
        elif (float(N)> 0 and round(float(N)) == float(N)):
            d = input("Input the split. The split has to divide the length of " +(N)+ " i.e. " + str(len(N))+"\n ")
            if ((len(N)) % int(d)==0):
                print((len(N))//int(d))
                print (is_up_monotone(N, d))
            if ((len(N))% int(d)!=0):
                print(""+str(d)+" does not divide "+str(len(N))+". Try again. ")
            
    else:
        flag= True
        print("Please enter yes or no. Try again.")
