#Erhan Kayır
#28.03.2023

import time

def Merge_Sort(my_list):# Merge Sort
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