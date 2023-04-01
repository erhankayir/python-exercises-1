#Erhan Kayır
#28.03.2023

def geometric_series():
    start = int(input("Starting value:"))               #Takes the starting value from the user
    ratio = int(input("Common ratio:"))                 #Takes the common ratio from the user
    num_elements = int(input("Number of terms:"))       #Takes the number of terms from the user
    for i in range(num_elements):                       #Performs the operation based on the values given above
        print(start * (ratio ** i))
