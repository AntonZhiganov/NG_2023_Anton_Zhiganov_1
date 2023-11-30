userList = input("Enter word: ")
userList = userList.lower() #convert to lowercase
vowels = "eyuioa"

print("only vowels: ")

for letter in userList:
    if letter in vowels:
        print(letter)
    
