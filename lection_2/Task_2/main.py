elements = input("Enter elements: ")
elementList = elements.split() 
numberElement = sum(1 for item in elementList if item.replace(".", "", 1).replace(",", "", 1).replace(" ", "", 1).isdigit())
print("Number in list: ", numberElement)