def searchSmaller(arr, start_index): 
    smaller = arr[start_index]
    smaller_index = start_index

    for i in range(start_index + 1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_index = i

    return smaller_index

def sortBySelection(arr): 
    for i in range(len(arr)):
        smaller_index = searchSmaller(arr, i) 
        arr[i], arr[smaller_index] = arr[smaller_index], arr[i]

    return arr

def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = (low  + high )
        kick = list[middle]
        if kick == item:
            return middle
        if kick > item:
            high = middle - 1
        else:
            low = middle + 1
    return None
    
my_list = [1, 2, 3, 5, 4, 10, 9, 8, 7, 6]
ordenared_list = sortBySelection(my_list)

print (binarySearch(ordenared_list, 3))