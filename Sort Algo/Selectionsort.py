def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

user_input = input("Enter numbers separated by spaces: ")
input_list = user_input.split()
arr = list(map(int, input_list))
selection_sort(arr)
print("Sorted array:", arr)
