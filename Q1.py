def arithmetic_series():
    start = int(input("Starting value:"))               #Takes the starting value from the user
    end = int(input("End value:"))                      #Takes the end value from the user
    step = int(input("Common difference:"))             #Takes the common difference from the user

    for i in range(start, end, step):                   #Performs the operation based on the values given above
        print(i)

def geometric_series():
    start = int(input("Starting value:"))               #Takes the starting value from the user
    ratio = int(input("Common ratio:"))                 #Takes the common ratio from the user
    num_elements = int(input("Number of terms:"))       #Takes the number of terms from the user
    for i in range(num_elements):                       #Performs the operation based on the values given above
        print(start * (ratio ** i))

def fibonacci_series():
    n = int(input("How many terms of fibonacci series would you like to generate?")) #Takes the number of terms from the user
    a = 0
    b = 1
    for i in range(n): #Performs the operation based on the values given above
        c = a + b
        a = b
        b = c
        print(c)
    

def choice(): #Performs the respective function based on the user's input
    series = int(input("Choose the series you would like to run:\n0:Exit the program\n1:Arithmetic series\n2:Geometric series\n3:Fibonacci series\n"))
    if series == 1 :
        arithmetic_series()
    elif series == 2:
        geometric_series()
    elif series == 3:
        fibonacci_series()
    elif series == 0:
        print("Program terminated")

choice()
series_cont = input("Would you like to generate another series? (Y/N)")

while series_cont == "Y":
    choice()
