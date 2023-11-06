elements = input("Enter elements: ")
elementList = elements.split() 
numberElement = 0

for num in elementList :
    if num.replace(" ", "").isdigit():
        numberElement += 1
        
print("Nember in list: ", numberElement)