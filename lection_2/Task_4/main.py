userList = input("Enter word: ")
userList = userList.lower()
vowels = "eyuioa"

print("only vowels: ")

for letter in userList:
    if letter in vowels:
        print(letter)
    
