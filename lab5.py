


################################
#Exercise 1
################################

s1 = 'good'
s2 = 'bad'
s3 = 'crazy'
print('azy' in s3)
print(' ' not in s1)
print(s1 + s2 + s3)
print(s1 + ' ' +s2 + ' ' + s3)
print(s3 * 10)
print(len(s1 + s2 + s3))


################################
#Exercise 2
################################

# declare the variable aha
aha = 'abcdefgh'


a = aha[:4]
b = aha[3:6]
c = aha[-1]
d = aha[-3:-1]
e = aha[-5:]
f = aha[-3:]
g = aha[0:7:3]
h = aha[1:4:2]

# printing the results
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

################################
#Exercise 3
################################

s=''' In ,M. Charles-Francois-Bienvenu Myriel was a bishop in Digne. He Was
a seventy five years old man; he held that position in Digne since 1806. ...'''
nS=''
for i in s:
    if i=='.' or i==',' or i==';' or i=='\n':
        nS+=' '
    else:
        nS+=i
print(nS)

nS=nS.strip()
print(nS)
nS=nS.lower()
print(nS)
count=nS.count('in')

print('\"in\" occurs',count,' number of times' )
nS=nS.replace('was','is')

################################
#Exercise 4
################################

def count1(s,a):
    return s.count(a)

def count2(s,a):
    count=0
    for i in range(len(s)):
        if s[i]==a: count+=1
    return count
#main part
s=input('Enter the string: \n')
print(count1(s,'a'))
print(count2(s,'a'))

################################
#Exercise 5
################################

def spaces(str):
    return(" ".join(str))

print(spaces('important'))

################################
#Exercise 6
################################

def code(s):
    result = ''
    for i in range(1, len(s), 2):
        result += s[i] + s[i - 1]
    if len(s) % 2 == 1:
        result += s[-1]
    return result
print(code('message secret'))
print(code('Message'))

    

