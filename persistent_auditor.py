num_of_failed = 0

def load_inventory():
    try:
        file = open("inventory.txt", "r")          # open the "inventory.txt" file in read mode
        lines = file.readlines()         # read all lines in the file
        file.close()     # close the file after done reading

        transaction_history = []    # creates an empty list to store old stock values
        inventory = 0
        reading_history = False    # currently not reading stock history
        
        for line in lines:           # for every line in text file
            line = line.strip()       # remove unnecessary spaces and \n

            if line == "Stock history:":   # when python reaches "stock history"
                reading_history = True  # the numbers coming after this belong to transaction history

            elif line == "New stock added:":     
                reading_history = False          

            elif line.startswith("Total stock:"):
                inventory = int(line.replace("Total stock: ", "").strip()) # replace "total stock" with nothing, leave with number, convert num to int

            elif reading_history and line.isdigit(): # if reading_history is true & line contains only digit
                transaction_history.append(int(line))   # convert text into integer & add it to the list

        return inventory, transaction_history

    except FileNotFoundError:         # if inventory.txt cannot be found,
        return 0, []                     

def save_inventory(inventory, transaction_history, new_stock_added):
    file = open("inventory.txt", "w")      # write the txt file

    file. write("Stock history:\n")
    for stock in transaction_history:
        file.write(str(stock) + "\n")     # convert each stock value into text, then go to the new line

    file.write("\nNew stock added:\n")
    for stock in new_stock_added:
        file.write(str(stock) + "\n")

    file.write("\nTotal stock: " + str(inventory) + "\n")
    
    file.close()

inventory, transaction_history = load_inventory()

new_stock_added = []

print("Current stock: ")
for stock in transaction_history:   # print all previously saved stock
    print(stock)

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
        generate_report(inventory, num_of_failed)    # generate report
        save_inventory(inventory, transaction_history, new_stock_added) # save everything into inventory.txt
        break

    inventory = process_delivery(inventory, user_input)

    transaction_history.append(user_input)     # add user input into entire history
    new_stock_added.append(user_input)   # rmb what are the newly added input
    print("New stock added:")
    print(user_input)

    tax = calculate_tax(user_input)

    if inventory > 500:
        print("Stock exceed storage capacity!")
        break