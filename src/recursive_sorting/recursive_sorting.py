# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # Initiazing innitial array
    iA = 0
    iB = 0

    for i in range(elements):
        if len(arrA) <= iA:
            merged_arr[i] = arrB[iB]
            iB += 1
        elif len(arrB) <= iB:
            merged_arr[i] = arrA[iA]
            iA += 1
        elif arrB[iB] < arrA[iA]:
            merged_arr[i] = arrB[iB]
            iB += 1
        else:
            merged_arr[i] = arrA[iA]
            iA += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        arr_left = arr[:middle]
        arr_right = arr[middle:]
        return merge(merge_sort(arr_left), merge_sort(arr_right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
