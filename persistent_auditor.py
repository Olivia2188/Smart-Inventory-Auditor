num_of_failed = 0

def load_inventory():
    try:
        file = open("inventory.txt", "r")          # open the "inventory.txt" file in read mode
        inventory = int(file.readline())         # read one line from the file as text, convert the text into int & store inside variable called inventory
        file.close()     # basically just mean close the file after done reading
        return inventory

    except FileNotFoundError:         # if inventory.txt cannot be found,
        return 0                     # inventory just start from 0

inventory = load_inventory()

def get_valid_input():
    failed_attempts = 0
    while True:
        user_input = input("Enter a stock quantity: ")

        if user_input == "quit":
            return "quit", failed_attempts

        elif user_input == "":
            print("Invalid input")
            failed_attempts += 1
            continue

        elif user_input[0] == ("-") and user_input[1:].isdigit():
            print("Negative numbers are not allowed")
            failed_attempts += 1
            continue

        elif not user_input.isdigit():
            print("Invalid input. Please enter as numbers (Eg: 1,2,3...)")
            failed_attempts += 1
            continue

        else:
            user_input = int(user_input)
            return user_input, failed_attempts

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total    

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Number of failed entries: {failed_attempts}")

while True:
    user_input, failed_attempts = get_valid_input()
    num_of_failed += failed_attempts
    if user_input == "quit":
        generate_report(inventory, num_of_failed)
        break

    inventory = process_delivery(inventory, user_input)

    tax = calculate_tax(user_input)

    if inventory > 500:
        print("Stock exceed storage capacity!")
        break