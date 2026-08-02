for i in range(0, 11):
    print(str(i) + " cubed is " + str(i**3))
    total = sum(j**3 for j in range(0, i+1))
    print("Total: " + str(total))