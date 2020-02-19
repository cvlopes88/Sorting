# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # creating placeholders for where we are in each arr
    a_index = 0
    b_index = 0

    # Loop through the length of  the combined elements
    for k in range(elements):
        # if one arrA or arr B is empty merge the other list
        if a_index >= len(arrA):
            merged_arr[k] = arrB[b_index]
            b_index += 1
        elif b_index >= len(arrB):
            merged_arr[k] = arrA[a_index]
            a_index += 1
        # if A[1] is smaller than B[1]
        elif arrA[a_index] < arrB[b_index]:
            # append A[1] to the merged array
            merged_arr[k] = arrA[a_index]
            a_index += 1
        # else
        else:
            # append B[1] to the end of the merged array
            merged_arr[k] = arrB[b_index]
            b_index += 1

    print(merged_arr)
    
    return merged_arr


    # merge(arr1, arr2)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
     # split the list into sublists until they are all length one or less
       # CEHCK IF LENGTH IS ONE OR LESS IF SO RETURN THE LIST
       if len(arr) > 1:
        
        # divide in half
        # call split function on left
        left = arr[:len(arr) // 2]
        # call split function on right
        right = arr[:len(arr) // 2:]
        # Sort the left
        left = merge_sort(left)
        # sort the right
        right = merge_sort(right)
        arr = merge(left, right)
       return arr
       print(merge_sort([3, 4, 1, 5, 3]))

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

