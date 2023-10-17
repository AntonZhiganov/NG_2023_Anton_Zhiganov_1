print ("Calculator")
chous = input ("What you want to do?(1 - (+)), (2 - (-)), (3 - (*)), (4 - (/)), (5 - Square root), (6 - degree)? : ") #Action selection
print ("If you enter (5) The second number has no effect :) ")
firstNumber = float(input ("Enter first number: ")) #1 number
secondNumber = float(input ("Enter second number: ")) #2 number
match chous :
    case "1": print ("Addition result: " + str(firstNumber + secondNumber))           #add
    case "2": print ("Minus result: " + str(firstNumber - secondNumber))              #minus
    case "3": print ("Multiplication result: " + str(firstNumber * secondNumber))     #multiplication
    case "4": print ("Result of division: " + str(firstNumber / secondNumber))        #division
    case "5": print ("Result of square root calculation: " + str(firstNumber ** 0.5)) #square root
    case "6": print ("Degree result: " + str(firstNumber ** secondNumber))            #degree
    case _ : print ("Please enter corect number (1-6) ")
