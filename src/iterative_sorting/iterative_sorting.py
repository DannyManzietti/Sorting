# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
   
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for k in range(cur_index, len(arr)):
            if arr[k] < arr[smallest_index]:
                smallest_index = k

       
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        swaps = 0
        for i in range(len(arr)):
            if i > 0 and arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1
        if swaps == 0:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr