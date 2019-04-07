# @author: coderistan
#
#  Insertion sort with Python
#  Time Complexity
#
# +---------+-----------+---------+
# |   Best  |  Average  |  Worst  |
# +---------+-----------+---------+
# |   Ω(n)  |  Θ(n^2)   |  O(n^2) |
# +---------+-----------+---------+

def insertion_sort(array):
    for i in range(1,len(array)):
        temp = array[i]
        j = i-1
        
        while(j >= 0 and temp < array[j]):
            array[j],array[j+1] = array[j+1],array[j]
            j = j-1
            
        array[j+1] = temp
        
    return array



array = [12,4,25,35,10,8,1,21]

print("Before: {}".format(" ".join([str(i) for i in array])))
print("After: {}".format(" ".join([str(i) for i in insertion_sort(array)])))
