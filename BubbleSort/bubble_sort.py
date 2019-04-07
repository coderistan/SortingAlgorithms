# @author: coderistan
#
# Bubble sort with Python
#  Time Complexity
#
# +---------+-----------+---------+
# |   Best  |  Average  |  Worst  |
# +---------+-----------+---------+
# |   Ω(n)  |  Θ(n^2)   |  O(n^2) |
# +---------+-----------+---------+

def bubble_sort(array):
    for i in range(0,len(array)):
        for k in range(0,len(array)-i-1):
            if(array[k] > array[k+1]):
                temp = array[k+1]
                array[k+1] = array[k]
                array[k] = temp

    return array

array = [12,4,25,35,10,8,1,21]

print("Before: {}".format(" ".join([str(i) for i in array])))
print("After: {}".format(" ".join([str(i) for i in bubble_sort(array)])))
