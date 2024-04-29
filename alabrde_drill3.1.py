triangle = int(input("Enter integer:"))
count = 1 
while count <= triangle: 
    for j in range (0, count):
        print ("*", end="")
        if (j != count):
            print(" ", end="")
    count = count + 1
    print() 