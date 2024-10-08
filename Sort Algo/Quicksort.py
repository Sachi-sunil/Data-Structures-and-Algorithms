def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

user_input = input("Enter numbers separated by spaces: ")
input_list = user_input.split()
arr = list(map(int, input_list))
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
