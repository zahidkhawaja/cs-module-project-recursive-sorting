# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    x = 0
    y = 0
    z = 0
    
    while x < len(arrA) and y < len(arrB):
        if arrA[x] < arrB[y]:
            merged_arr[z] = arrA[x]
            x += 1
        else:
            merged_arr[z] = arrB[y]
            y += 1
        z += 1
    while x < len(arrA):
        merged_arr[z] = arrA[x]
        z += 1
        x += 1
    while y < len(arrB):
        merged_arr[z] = arrB[y]
        z += 1
        y += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = arr[:middle]
    right = arr[middle:]

    return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
"""
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
"""

