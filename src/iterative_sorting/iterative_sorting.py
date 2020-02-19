# TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
        # smallest_index = cur_index
        # smallest = min(arr[i:])
        # sml_index = arr.index(smallest)
        
        # arr[sml_index], arr[i], arr[sml_index]
        # print("selection", selection_sort(the_array))
        
        # for j in range(cur_index, len(arr)):
        #     if arr[j] < arr[smallest_index]:
        #         smallest_index = j
           
           
           
            # for j in range(i):
            #     if arr[j] < arr[j-1]:
            #         temp = arr[j]
            #         arr[j] = arr[j+1]
            #         arr[j] = temp   
            
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
            # current = arr[cur_index]
            # smallest = arr[smallest_index]
            # arr[cur_index] = smallest
            # arr[smallest_index] = current     



        # TO-DO: swap

    # return arr


def selection_sort2(arr):
    for i in range(0, len(arr)-1):
        current_i = i
        smlest = current_i
        for nA in range(i+1, len(arr)):
            if arr[nA] < arr[smlest]:  # as passes comparing the new loop to the set previously smallest
                smlest = nA
        # the swap below needs to be assigned under the inner loop so it actually does shit
                arr[current_i], arr[smlest] = arr[smlest], arr[current_i]
                print(arr)
    return arr


the_array = [3, 2, 4, 5, 1, 6, 8, 7, 9, 0]

print("selection", selection_sort2(the_array))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) -1):
        for j in range(i + 1, len(arr)):
            if arr[i]>arr[j]:
              arr[i], arr[j] = arr[j], arr[i]
    return arr
print("buble", bubble_sort(the_array))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
