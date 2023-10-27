userList = input("Enter numer: ")

try:
    
    num = int(userList)

    print("Number| Divider")
    print("----------------")
    for numb in range(1, num + 1):
        divisors = [d for d in range(1, numb + 1) if numb % d == 0]
        print(f"{numb:^6} | {', '.join(map(str, divisors))}")

    prime_numbers = [num for num in range(2, num + 1) if len([d for d in range(1, num + 1) if num % d == 0]) == 2]
    print("\nprime numbers", num, ":", prime_numbers)
except ValueError:
    print("You enter dont numbers")