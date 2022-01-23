# Bucket Sort in Python
from hashlib import new
import os
import re
import shutil

path = os.path.abspath(os.getcwd())+'/Data/'
path2 = os.path.abspath(os.getcwd())+'/sorted/'
print(path)
mylist = os.listdir(path)
newlist = []

for index, list in enumerate(mylist):
    list = list.replace('.txt', '')
    hold = re.sub('[^0-9]', '', list)
    os.rename(path+list+'.txt', path2 + hold + '.txt')
    newlist.append(int(hold))
print(mylist)
# Bucket sort for numbers
# having integer part


def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)

    # range(for buckets)
    rnge = (max_ele - min_ele) / noOfBuckets

    temp = []

    # create empty buckets
    for i in range(noOfBuckets):
        temp.append([])

    # scatter the array elements
    # into the correct bucket
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)

        # append the boundary elements to the lower array
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])

        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])

    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()

    # Gather sorted elements
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1


# Driver Code

noOfBuckets = 5
bucketSort(newlist, noOfBuckets)


print("Sorted Array is")


print(newlist)
