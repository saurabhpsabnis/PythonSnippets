
#Sorting Algorithms to sort a given list in ascending order
#Auther : Saurabh P Sabnis 

def bubble_sort(ll):
    "Bubble sort"
    for x in range(len(ll)-1,0,-1):
        for y in range(0,len(ll[:x])):
            if ll[y] > ll[y+1]: 
                ll[y], ll[y+1] = ll[y+1],ll[y]
    return ll

def selection_sort(ll):
    "Selection Sort"
    for x in range(len(ll)-1):
        smallest = x
        for y in range(x,len(ll)):
            if ll[y] < ll[smallest]:
                smallest = y
        if smallest != x:
            ll[x],ll[smallest] = ll[smallest],ll[x]
    return ll
            
def insertion_sort(ll):
    for x in range(len(ll)-1):
        y = x
        while y >= 0 and ll[y] > ll[y+1]:
            ll[y], ll[y+1] = ll[y+1], ll[y]
            y = y-1
    return ll

def quick_sort(ll):
    if len(ll) == 0:
        return []
    pivote = ll[0]
    less = []
    greater = []
    equal = []
    for x in ll:
        if x > pivote:
            greater.append(x)
        elif x < pivote:
            less.append(x)
        else:
            equal.append(x)
    return quick_sort(less) + equal + quick_sort(greater)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i != len(left) and j != len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    for x in range(i,len(left)):
        result.append(left[x])
    for x in range(j,len(right)):
        result.append(right[x])
    return result
 
def mearge_sort(ll):
    middle = len(ll) // 2
    if middle == 0:
        return ll
    else:
        left = ll[:middle]
        right = ll[middle:]
        left = mearge_sort(left)
        right = mearge_sort(right)
        return merge(left, right)

def max_heapify(ll,i):
    flag = False
    largest = i
    if 2*i + 1 < len(ll) and ll[2*i+1] > ll[largest]:
        flag = True
        largest = 2*i +1 
    if 2*i + 2 < len(ll) and ll[2*i+2] > ll[largest]:
        flag = True
        largest = 2*i +2
    if flag:
        ll[i], ll[largest] = ll[largest], ll[i]
        max_heapify(ll, largest)
        
def min_heapify(ll,i):
    flag = False
    smallest = i
    if 2*i + 1 < len(ll) and ll[2*i+1] < ll[smallest]:
        flag = True
        smallest = 2*i +1 
    if 2*i + 2 < len(ll) and ll[2*i+2] < ll[smallest]:
        flag = True
        smallest = 2*i +2
    if flag:
        ll[i], ll[smallest] = ll[smallest], ll[i]
        min_heapify(ll, smallest)

def heap_sort(ll):
    sortedList = []
    for i in range(len(ll)//2,-1,-1):
        min_heapify(ll,i)
    for i in range(len(ll)):
        sortedList.append(ll[0])
        ll = ll[1:]
        min_heapify(ll,0)
    return sortedList

if __name__ == '__main__':
    temp = [5,86,69,73,11,17,1,74,34,3]
    print "bubble sort " + str(bubble_sort(temp))
    temp = [5,86,69,73,11,17,1,74,34,3]
    print "Selection sort" + str(selection_sort(temp))
    temp = [5,86,69,73,11,17,1,74,34,3]
    print "insertion sort" + str(insertion_sort(temp))
    temp = [5,86,69,73,11,17,1,74,34,3]
    print "Quick sort" + str(quick_sort(temp))
    temp = [5,86,69,73,11,17,1,74,34,3]
    print "Merge Sort" + str(mearge_sort(temp))
    temp = [5,86,69,73,11,17,1,74,34,3]
    print "Heap sort" + str(heap_sort(temp))

