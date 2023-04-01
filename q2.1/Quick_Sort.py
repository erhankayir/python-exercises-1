#Erhan Kayır
#28.03.2023

import time 

def Quick_Sort(my_list):# Quick Sort
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