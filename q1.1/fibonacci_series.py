#Erhan Kayır
#28.03.2023

def fibonacci_series():
    n = int(input("How many terms of fibonacci series would you like to generate?")) #Takes the number of terms from the user
    fnumber0 = 0
    fnumber1 = 1
    for i in range(n):                                  #Performs the operation based on the values given above
        nterm = fnumber0 + fnumber1
        fnumber0 = fnumber1
        fnumber1 = nterm
        print(nterm)