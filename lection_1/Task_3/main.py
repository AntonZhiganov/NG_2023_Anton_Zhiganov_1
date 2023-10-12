print ("Program to convert degrees Celsius to degrees Fahrenheit")
print ("if you want to convert from degrees Celsius to degrees Fahrenheit enter (1)")
print ("if you want to convert from degrees Fahrenheit to degrees Celsius enter (2)")

convert = input("What would you like ")   #The user selects an option

if convert == '1' :                                                     #Converting to degrees Fahrenheit
    celsius1 = float(input("Enter value in degrees Celsius: "))
    fahrenheit1 = float(celsius1 * 9 / 5 + 32)
    print (celsius1, " degrees Celsius on the Fahrenheit scale = ", ("%.2f" % fahrenheit1))  #Output of the result
if convert == '2' :
    fahrenheit2 = float(input("Enter value in degrees Fahrenheit: "))   #Converting to degrees Celsius
    celsius2 = float((fahrenheit2 - 32) / 1.8)
    print (fahrenheit2, " degrees Fahrenheit on the Celsius scale = ", ("%.2f" % celsius2) ) #Output of the result
else :
    print ("You only need to enter 1 or 2, try again")    

