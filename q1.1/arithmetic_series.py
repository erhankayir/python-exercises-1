#Erhan Kayır
#28.03.2023

def arithmetic_series():
    start = int(input("Starting value:"))               #Takes the starting value from the user
    end = int(input("End value:"))                      #Takes the end value from the user
    step = int(input("Common difference:"))             #Takes the common difference from the user
    for i in range(start, end, step):                   #Performs the operation based on the values given above
        print(i)
