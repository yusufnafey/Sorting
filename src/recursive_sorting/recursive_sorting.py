# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    c = 0

    while a < len( arrA ) and b < len ( arrB ):

        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            c += 1
            a += 1
        else:
            merged_arr[c] = arrB[b]
            c += 1
            b += 1
            
    while b < len( arrB ):
        merged_arr[c] = arrB[b]
        c += 1
        b += 1
    
    while a < len( arrA ):
        merged_arr[c] = arrA[a]
        c += 1
        a += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
