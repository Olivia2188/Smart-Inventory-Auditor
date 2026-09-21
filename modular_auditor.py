inventory = 0
num_of_failed = 0

def get_valid_input():
    while True:
        user_input = input("Enter a stock quantity: ")

        if user_input == "quit":
            return "quit"

        elif user_input == "":
            print("Invalid input")
            continue

        elif user_input[0] == ("-") and user_input[1:].isdigit():
            print("Negative numbers are not allowed")
            continue

        elif not user_input.isdigit():
            print("Invalid input. Please enter as numbers (Eg: 1,2,3...)")
            continue

        else:
            user_input = int(user_input)
            return user_input

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total    

while True:
    user_input = get_valid_input()
    if user_input == "quit":
        break

    inventory = process_delivery(inventory, user_input)

    if inventory > 500:
        print("Stock exceed storage capacity!")
        break