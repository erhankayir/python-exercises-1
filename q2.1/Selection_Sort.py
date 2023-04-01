#Erhan Kayır
#28.03.2023

import time

def Selection_Sort(my_list):# Selection Sort
    start_time = time.time()
    for i in range(len(my_list)):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    end_time = time.time()
    print("Selection Sort processing time: {:.5f} seconds".format(end_time - start_time))