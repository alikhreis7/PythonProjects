

import string

def open_file():
    while (True):
       '''None->file object
       See the assignment text for what this function should do'''
       try:
           fileopen = input("Enter the name of the file: ")
           ods = open(fileopen, 'r')
           return ods
       except FileNotFoundError:
          print('There is no file with that name. Try again.')
   

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    word = {}
    ln = fp.read().splitlines()
    i=1
    for l in ln:
        edit = l
        glist =[]
        for p in string.punctuation:
            edit = edit.lower().replace(p,"")
        l_edit = edit.split(" ")
        for s in l_edit:
            if len(s) >= 2:
                glist.append(s)
        for w in glist:
            mykey = word.get(w)
            if mykey is None:
                word.update({w:{i}})
            else:
                mykey.add(i)
                word.update({w:mykey})
        i+=1
    return word


def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    slinenum = []
    for i in query:
        if i in D:
            x = D.get(i)
            slinenum.append(x)
        else:
            print('The word', i, "is not in the file!")
            return
    if len(slinenum) > 0:
        res = slinenum[0]
    for x in slinenum:
        res = x.intersection(res)
    if len(res) > 0:
        for r in res:
            print(r, end=" ")
    print()

    

##############################
# main
##############################
file=open_file()
D=read_file(file)
while True:
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    if query == "q":
        quit()
    for p in string.punctuation:
        query = query.lower().replace(p, "")
    query = query.split(" ")
    main = find_coexistance(D, query)
    print(query)

