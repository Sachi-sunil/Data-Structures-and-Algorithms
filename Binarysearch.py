def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = []
ans = "y"
while ans == 'y':
    user_input = int(input("Enter integer element"))
    arr.append(user_input)
    ans = input("Do you want to add another element? : y/n ?")

target = int(input("Enter the element to search for: "))

result = binary_search(arr, target)

if result != -1:
    print("Target ", target, " found at index ", result)
else:
    print(target, " not found in the list.")