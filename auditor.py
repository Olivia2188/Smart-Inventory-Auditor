inventory = 0
num_of_failed = 0

while True:
    user_input = input("Enter a stock quantity: ")

    if user_input == "quit":
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Failed Entries: {num_of_failed}")
        break

    if user_input == "":
        print("Invalid input")
        num_of_failed += 1
        continue

    if user_input[0] == ("-") and user_input[1:].isdigit():
        print("Negative numbers are not allowed")
        num_of_failed += 1
        continue

    if not user_input.isdigit():
        print("Invalid input. Please enter as numbers (Eg: 1,2,3...)")
        num_of_failed += 1
        continue

    user_input = int(user_input)

    inventory += user_input

    if inventory > 500:
        print("Stock exceed storage capacity!")
        break