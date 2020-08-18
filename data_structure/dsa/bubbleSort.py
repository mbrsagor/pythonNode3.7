def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [10, 1, 12, 40, 3, 2, 5]
bubbleSort(arr)

for i in range(len(arr)):
    print(arr[i])
