userList = input("Enter word: ")
vowels = "eyuioaEYUIOA"

print("only vowels: ")

for letter in userList:
    if letter in vowels:
        print(letter)
    
