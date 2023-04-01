#Erhan Kayır
#28.03.2023

import time

def Bubble_Sort(my_list):# Bubble Sort
    start_time = time.time()
    n = len(my_list)
    for i in range(n):
        for j in range(n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    end_time = time.time()
    print("Bubble Sort processing time: {:.5f} seconds".format(end_time - start_time))