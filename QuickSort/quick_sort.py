# @author: coderistan
#
#  Quick sort with Python
#  Time Complexity
#
# +---------+-----------+---------+
# |   Best  |  Average  |  Worst  |
# +---------+-----------+---------+
# | Ω(nlogn)|  Θ(nlogn) |  O(n^2) |
# +---------+-----------+---------+

def partition(array,low,high):
    i = low-1
    pivot = array[high]
    for k in range(low,high):
        if(array[k] <= pivot):
            i = i+1
            array[i],array[k] = array[k],array[i]

    array[i+1],array[high] = array[high],array[i+1]
    
    return i+1

def quick_sort(array,low,high):
    if(low < high):
        pivot = partition(array,low,high)
        
        quick_sort(array,low,pivot-1)
        quick_sort(array,pivot+1,high)


array = [12,4,25,35,10,8,1,21]

print("Before: {}".format(" ".join([str(i) for i in array])))
quick_sort(array,0,len(array)-1)
print("After: {}".format(" ".join([str(i) for i in array])))


