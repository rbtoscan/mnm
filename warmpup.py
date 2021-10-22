

#a. Given the string x, write a function that will return a two-element list 
# where the first element will be the string x with letters in even places changed to uppercase.
#The second item in the list will be uppercase in odd places.
#Example:
#fun ("abcdef") -> ['aBcDeF', 'AbCdEf']
#Assume that the input to the function contains only letters.
#Commit and push!

# this task is written in python 2.7

def warmup_a(string):
    c=0
    out1=""
    out2=""
    for i in string:
        c=c+1
        if c%2 == 0 :
            out1=out1+i.lower()
        else:
            out1=out1+i.upper()

    c=1
    for i in string:
        c=c+1
        if c%2 == 0 :
            out2=out2+i.lower()
        else:
            out2=out2+i.upper()

    return [out1,out2]

input="abcdef"
output = warmup_a(input)

print output


#b. Write a function that takes a string as an argument. As output, it will return the number of letters in the string more than once. The code should not be case-
#sensitive.

def warmup_b(string):
    c=0
    char_dic= {}
    for i in string:
        if i.lower() not in char_dic:
            char_dic[i.lower()]=1
        else:
            char_dic[i.lower()]=char_dic[i.lower()]+1


    repeated=[]
    for k,v in char_dic.iteritems():
        #print k,v
        if v > 1:repeated.append(k)

    print "Number of repeated letters:",len(repeated),
    #print 'The following letters occur more than once:',
    print "(",
    for i in repeated: print i,
    print ")"
    
      

warmup_b("ABBA")
warmup_b("aBcbA")
warmup_b("RhabarbArka")