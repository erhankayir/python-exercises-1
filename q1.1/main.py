#Erhan Kayır
#28.03.2023

import fibonacci_series
import arithmetic_series
import geometric_series

def selection():
    decision = input("Would you like to generate another series? (Y/N)")
    if decision == "Y" or decision == "y":
        choice()
    elif decision == "N" or decision == "n":
        print("Program terminated")
    else :
        print("Review your selection")
        selection()    

def choice():                                           #Performs the respective function based on the user's input
    series = int(input("Choose the series you would like to run:\n0: Exit the program\n1: Arithmetic series\n2: Geometric series\n3: Fibonacci series\n"))
    if series == 1 :
        arithmetic_series.arithmetic_series()
        selection()
    elif series == 2:
        geometric_series.geometric_series()
        selection()
    elif series == 3:
        fibonacci_series.fibonacci_series()
        selection()
    elif series == 0:
        print("Program terminated")
    else :
        print("Review your selection")
        choice()
        
choice()