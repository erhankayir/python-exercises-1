import random
import time

# Create a list of 1000 random numbers
my_list = [random.randint(0, 10000) for _ in range(1000)]

# Selection Sort
start_time = time.time()
for i in range(len(my_list)):
    min_idx = i
    for j in range(i+1, len(my_list)):
        if my_list[j] < my_list[min_idx]:
            min_idx = j
    my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
end_time = time.time()
print("Selection Sort processing time: {:.5f} seconds".format(end_time - start_time))

# Bubble Sort
start_time = time.time()
n = len(my_list)
for i in range(n):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
end_time = time.time()
print("Bubble Sort processing time: {:.5f} seconds".format(end_time - start_time))

# Insertion Sort
start_time = time.time()
for i in range(1, len(my_list)):
    key_item = my_list[i]
    j = i - 1
    while j >= 0 and my_list[j] > key_item:
        my_list[j + 1] = my_list[j]
        j -= 1
    my_list[j + 1] = key_item
end_time = time.time()
print("Insertion Sort processing time: {:.5f} seconds".format(end_time - start_time))

# Merge Sort
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    left_list = my_list[:mid]
    right_list = my_list[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))

start_time = time.time()
my_list = merge_sort(my_list)
end_time = time.time()
print("Merge Sort processing time: {:.5f} seconds".format(end_time - start_time))

# Quick Sort
def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    pivot = my_list[len(my_list) // 2]
    left_list = [x for x in my_list if x < pivot]
    middle_list = [x for x in my_list if x == pivot]
    right_list = [x for x in my_list if x > pivot]

    return quick_sort(left_list) + middle_list + quick_sort(right_list)

start_time = time.time()
my_list = quick_sort(my_list)
end_time = time.time()
print("Quick Sort processing time: {:.5f} seconds".format(end_time - start_time))
