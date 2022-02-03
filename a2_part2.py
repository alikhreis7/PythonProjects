

import math
############################################################################
#QUESTION 2.1
############################################################################

def min_enclosing_rectangle(radius,x,y):
    '''(number,number,number)->number,number
        Preconditions: N/A
        Returns n none if radius is negative otherwise returns x and y
        coordinates of botton left corner
        of rectangle given radius,x,y/tuple'''
    if radius<=0:
        return None
    return x-radius,y-radius

############################################################################
#QUESTION 2.2
############################################################################

def vote_percentage(result):
    '''(substring)->result
        Preconditions: if answer is yes, count_yes+1, elif
        answer is no, count_no+1
        Returns the percentage of yes or no'''
    
    substrings = [result[i: j] for i in range(len(result))
          for j in range(i + 1, len(result) + 1)]
  
    #print(substrings)
  
    # initializing the variables for taking the count of yes , no and total
    count_yes = 0
    count_no = 0
    total_count = 0
  
    # iterating the list of the substring to count yes and no strings
    for i in substrings:
        if i.lower() == 'yes':
            count_yes = count_yes + 1
        elif i.lower() == 'no':
            count_no = count_no + 1
  
    # summing us to find the total count
    total_count = (count_yes + count_no)
    # if total is not still zero we find the percentage
    if total_count:
        percent_yes = count_yes/total_count
        return percent_yes
    #else return percentage as 0
    else:
        return '0'

result1 = "yes yes yes yes yes abstained abstained yes yes yes"
result2 = "yes, yes, no, yes, no, yes, abstained, yes, yes, no"
result3 = "abstained no abstained yes no yes no yes yes yes no"
result4 = "no yes no no no yes yes yes no"

############################################################################
#QUESTION 2.3
############################################################################
def vote_percentage(yes_count,no_count,abstained_count):
    '''string,string,string->result
        Preconditions: if the total equals the yes count, will print a result
        elif 2/3, result will be different meaning will retirn a different result
        elif 1/2, result will be different, else, the prposal fails
        Returns a different result depending on rhe yes and no count'''

   #total number of votes can be calculated by adding count of yes and no votes
   total = yes_count + no_count

   if total == yes_count:
       result = "proposal passes unanimously"
   elif (yes_count/total) >= (2/3):
       result = "proposal passes with super majority"
   elif (yes_count/total) >= (1/2):
       result = "proposal passes with simple majority"
   else:
       result = "proposal fails"

   return result


def vote():
    '''none->none
    Preconditions: entry has to be yes, no or abstained
    Returns result depending on the users entry ot yes, no or abstained'''
   print('vote()')
   print("enter the yes, no, abstained votes one by one and press enter:")
   votes = input()

   yes_count = votes.count("yes")
   no_count = votes.count("no")
   abstained_count = votes.count("abstained")

   result = vote_percentage(yes_count,no_count,abstained_count)
   print(result)


vote()
