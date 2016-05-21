'''
Created on May 10, 2016

@author: amolsaurabh
'''

from sorting_algos import sorting

def isPostTraversalOfBST(ll):
    "Determine if given an array is post order of BST "
    i = 0;
    length = len(ll)
    if length <= 1:
        return True
    while(ll[i] < ll[length-1]):
        i += 1
    for j in range(i,length-2):
        if ll[j] < ll[length-1]:
            return False
    return isPostTraversalOfBST(ll[:(i-1)]) and isPostTraversalOfBST(ll[(i+1):(length-2)])

def sortedSquareArray(ll):
    "Given a sorted array of intergers find a sorted array of square of all integers from that array"
    if not sorting.isArraySorted(ll):
        return []
    length = len(ll)
    result = []
    i = 0
    j = length -1
    while(i<j):
        if ll[i]*ll[i] < ll[j]*ll[j]:
            result.insert(0,ll[j]*ll[j])
            j -= 1
        else:
            result.insert(0,ll[i]*ll[i])
            i +=1
    return result
        
if __name__ == '__main__':
    ll = [0, 2, 4, 6, 5, 3, 1, 8, 10, 9, 7 ]
    ll1 = [0, 2, 4, 6, 5, 14, 1, 8, 10, 9, 7 ]
    print isPostTraversalOfBST(ll)
    print isPostTraversalOfBST(ll1)
    
    temp = [-5,-86,69,73,-11,17,1,-74,34,3]
    temp = sorting.bubble_sort(temp)
    print  "Sorted array" + str(temp)
    print " Case 1: sq sorted array : " + str(sortedSquareArray(temp))
    temp = [5,-86,69,73,11,17,1,74,34,3]
    print " Case 2: sq un sorted array  : " + str(sortedSquareArray(temp))
    