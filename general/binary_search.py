def binary_search(target, sorted_list):

    left = 0
    right = len(sorted_list) - 1

    count = 0

    while left <= right:
        count += 1
        mid = (right + left) // 2

        if target == sorted_list[mid]:
            return f"the index of the target is {mid} the number of interations it took to reach this is {count}"
        elif target < sorted_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return "target is not in list"


sorted_list = [i for i in range(128)]
print(binary_search(0, sorted_list))
