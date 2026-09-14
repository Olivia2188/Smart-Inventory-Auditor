inventory = 0

while True:
    user_input = input("Enter a stock quantity:")

    if user_input == "quit":
        break

    if user_input[0] == ("-") and user_input[1:].isdigit():
        print("Negative numbers are not allowed")
        continue

    if not user_input.isdigit():
        print("Invalid input. Please enter as numbers (Eg: 1,2,3...)")
        continue

    inventory += user_input

    if inventory>500:
        print("Stock exceed storage capacity!")
        break



    user_input = int(user_input)
