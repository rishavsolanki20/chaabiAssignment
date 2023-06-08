def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                index = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


arr = [5,416,54,21,6135,15,741]
sorted_arr = selectionSort(arr)
print(sorted_arr)