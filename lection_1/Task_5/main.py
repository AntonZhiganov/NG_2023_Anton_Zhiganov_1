print ("quadratic equation calculator")

elementA = float(input ("Enter element a: "))
elementB = float(input ("Enter element b: "))
elementC = float(input ("Enter element c: "))

if elementA == 0 :
    print(" a can`t equal to (0)")
else:
    discriminant = float((elementB * elementB) - (4 * elementA * elementC))
    if discriminant < 0 :
        print ("no roots")
    else:
        root1 = (-elementB + (discriminant ** 0.5)) / (2 * elementA)
        root2 = (-elementB - (discriminant ** 0.5)) / (2 * elementA)
        print("root of the equation: ")
        print(root1, root2)