inventory = 0

while True:
    user_input = input("Enter a stock quantity:")

    if user_input == "quit":
        break
    
    if not user_input.isdigit():
        print("Error. Please enter as numbers (Eg: 1,2,3...)")
        continue

    user_input = int(user_input)
