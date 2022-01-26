import sys
from config import *

categories = []
budget = []
MAX_LENGTH = 100

def main():
    
    # Get budget year
    year = get_year()

    # Add budget category and available cash
    add_category()

    q1 = input("Would you like to update your budget? ").lower()
    if q1 == "exit":
        exit_program()

    # Update budget
    while q1 != "0":

        total = 0
        # Print current budget
        print(f"Budget for {year}")
        for d in budget:
            for key in d:
                print(f"{key} = {d[key].cash} ")
                total += d[key].cash
        print(f"total = {total}")

        # Print update options
        with open("options.txt", "r") as f:
            get_options = f.read()
            print(get_options)
        q2 = input("Select one of the options above: ").lower()
        if q2 == "0" or q2 == "exit":
            exit_program()
        # Deposit
        elif q2 == "1":
            index = find_category("Deposit into: ")
            value = get_cash_value("Value: ")
            budget[index[0]][index[1]].deposit(value)
        # Withdraw
        elif q2 == "2":
            index = find_category("Withdraw from: ")
            value = get_cash_value("Value: ")
            budget[index[0]][index[1]].withdraw(value)
        # Transfer
        elif q2 == "3":
            origin = find_category("Origin: ")
            value = get_cash_value("Value: ")
            destination = find_category("Destination: ")
            budget[origin[0]][origin[1]].withdraw(value)
            budget[destination[0]][destination[1]].deposit(value)
        # Add category
        elif q2 == "4":
            add_category()
        # Remove category
        elif q2 == "5":
            remove_category()
        # Exit program
        elif q2 == "exit":
            exit_program()
        q1 = input("Would you like to update your budget? ").lower()


    total = 0
    # Write output file
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write(f"Budget for {year} \n")
        for d in budget:
            for key in d:
                f.write(f"{key} = {d[key].cash} \n")
                total += d[key].cash
        f.write(f"total = {total} \n")

    print("Budget completed!")

def add_category():

    count = len(categories)
    while count < MAX_LENGTH:
        usr_input = input("Add category (type 0 to stop): ").lower()
        if usr_input == "0" and count == 0:
            sys.exit("No categories were added.")
        elif usr_input == "0":
            break
        elif usr_input == "exit":
            exit_program()
        else:
            if count != 0:
                for category in categories:
                    if usr_input == category:
                        print("Category already exists.")
                        break
                    if categories.index(category) == count - 1:
                        categories.append(usr_input)
                        count += 1
                        break
            else:
                categories.append(usr_input)
                count += 1
        if count == MAX_LENGTH:
            print("Limit reached.")
    
    for category in categories:
        cash = get_cash_value(f"Available cash for {category}: ")
        budget.append({category : Budget(cash)})

def remove_category():
    usr_input = input("Remove category: ").lower()
    if usr_input == "exit":
        exit_program()
    for category in categories:
        if usr_input == category:
            index = categories.index(usr_input)
            categories.remove(usr_input)
            budget[index].pop(usr_input)
            if len(categories) == 0:
                sys.exit("All categories removed.")

def find_category(m):
    while True:
        usr_input = input(m)
        if usr_input == "exit":
            exit_program()
        for category in categories:
            if usr_input == category:
                return [categories.index(category), usr_input]
            if categories.index(category) == len(categories) - 1:
                print("Category not found.")
                break

if __name__ == "__main__":
    main()