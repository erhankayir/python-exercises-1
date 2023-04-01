#Erhan Kayır
#28.03.2023

import time

def Insertion_Sort(my_list):# Insertion Sort
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