'''
Created on May 10, 2016

@author: amolsaurabh
'''



def generateNbitStrings(n):
    '''Generate all n bit binary strings for given n'''
    if n == 0:
        return []
    if n == 1:
        return ["0","1"]
    return ["0" + x for x in generateNbitStrings(n-1)] + ["1" + x for x in generateNbitStrings(n-1)]


def permuteString(s,start,end):
    " Print all possible permutation of a string"
    result = "" 
    if(start == end):
        for i in s:
            result = result + i
        print result
    else:
        for i in range(start,end):
            s[start], s[i] = s[i], s[start]
            permuteString(s, start+1, end)
            s[start], s[i] = s[i], s[start]
         

print generateNbitStrings(4)
permuteString(list("abcd"), 0, len("abcd"))



