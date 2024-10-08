def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


user_input = input("Enter numbers separated by spaces: ")
input_list = user_input.split()
arr = list(map(int, input_list))
bubble_sort(arr)
print("Sorted array:", arr)
