from random import shuffle


def selection_sort(some_list):
    for i, num in enumerate(some_list):
        curr_min_idx = i
        for j in range(i + 1, len(some_list)):
            if some_list[j] < some_list[curr_min_idx]:
                curr_min_idx = j
        some_list[i], some_list[curr_min_idx] = some_list[curr_min_idx], some_list[i]
    return some_list


some_list = [i for i in range(10)]
shuffle(some_list)
print(some_list)
selection_sort(some_list)
print(some_list)
