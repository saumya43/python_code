def mergeSort(arr, l, m, r):
    i, j = 0, 0
    k = l
    arr1 = arr[l:m+1]
    arr2 = arr[m+1:r+1]
    print(arr1)
    print(arr2)
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
        
    
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1

    return arr

if __name__ == "__main__":
    numbers = [1, 3, 2, 4]
    m = int(len(numbers)/2) -1
    print(m)
    l, r = 0, len(numbers)
    print(l, r)
    print(mergeSort(numbers, l, m, r))

