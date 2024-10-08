def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr=[]
ans="y"
while ans=='y':
    user_input = int(input("Enter integer element"))
    arr.append(user_input)
    ans=input("Do you want to add another element? : y/n ?")


target = int(input("Enter the element to search for: "))


result = linear_search(arr,target)


if result != -1:
    print("Target ",target," found at index ",result)
else:
    print(target," not found in the list.")