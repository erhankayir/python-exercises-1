#Erhan Kayır
#28.03.2023

import Selection_Sort
import Bubble_Sort
import Insertion_Sort
import Merge_Sort
import Quick_Sort
import random

def q2():
    def create_list():
        list_input = input("Would you like to enter your own list? If you don't have a list, a list of random numbers will be generated.\nThe generated list will be generated from 1000 random numbers between 1 and 10000. (Y/N)\n")
        if list_input == "Y" or list_input == "y":
            my_list_str = input("Sayilari aralarinda bosluk birakarak girin: ")
            my_list = list(float(my_list_str.split()))
        elif list_input == "N" or list_input == "n":
            my_list = [random.randint(0, 10000) for _ in range(1000)]
        else:
            print("Please use the specified expressions")
            my_list = create_list()
        return my_list

    my_list = create_list()
    Selection_Sort.Selection_Sort(my_list.copy())
    Bubble_Sort.Bubble_Sort(my_list.copy())
    Insertion_Sort.Insertion_Sort(my_list.copy())
    Merge_Sort.Merge_Sort(my_list.copy())
    Quick_Sort.Quick_Sort(my_list.copy())

def selection():
    sec=input("Would you like to run it again?(Y/N)")
    if sec== "Y" or sec=="y":
        q2()
    elif sec== "N" or sec=="n":
        print("Program terminated")
    else :
            print("Review your selection")
            selection()

q2()
selection()