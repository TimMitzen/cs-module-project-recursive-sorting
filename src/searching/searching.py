# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here


    middle = (start + end) // 2
    if len(arr) == 0:#iff len of arr is equal to 0 return -1
        return - 1
    if start > end:# if the start is bigger than end return -1
        return -1
    if arr[middle] == target:#if the middle of the arr equal target return middle
        return middle
    else:
        if target < arr[middle]:# if the target is smaller end equal the middle - 1
            end = middle - 1
        else:
            start = middle + 1
        return binary_search(arr, target, start, end)




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass

