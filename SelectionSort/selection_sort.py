# @author: coderistan
# Selection sort with Python
#  Time Complexity
#
# +---------+-----------+---------+
# |   Best  |  Average  |  Worst  |
# +---------+-----------+---------+
# |  Ω(n^2) |  Θ(n^2)   |  O(n^2) |
# +---------+-----------+---------+


def selection_sort(array):
    for i in range(0,len(array)):
        min_ = i

        for k in range(i,len(array)):
            if(array[k] < array[min_]):
                min_ = k

        temp = array[min_]
        array[min_] = array[i]
        array[i] = temp

    return array

array = [12,4,25,35,10,8,1,21]

print("Before: {}".format(" ".join([str(i) for i in array])))
print("After: {}".format(" ".join([str(i) for i in selection_sort(array)])))
