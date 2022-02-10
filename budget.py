from config import *

def main():
    
    # Get budget year
    year = get_year()

    # Add budget category and available cash
    budget = add_categories()

    q = input("Would you like to update your budget? ").lower()
    # Update budget
    while q != "0":

        if q == "exit":
            exit_program()

        total = 0
        # Print current budget
        print(f"Budget for {year}")
        for item in budget:
            print(f"{item.category} = {item.cash}")
            total += item.cash
        print(f"Total = {total}")

        # Print update options
        with open("options.txt", "r") as f:
            get_options = f.read()
            print(get_options)

        q = input("Select one of the options above: ").lower()
        if q == "exit":
            continue
        
        match q:
            case "0":
                break
            case "1":
                # Deposit
                c = find(budget, "Deposit into: ")
                v =  get_cash_value("Value: ")
                budget[c].deposit(v)
            case "2":
                # Withdraw
                c = find(budget, "Withdraw from: ")
                v =  get_cash_value("Value: ")
                budget[c].withdraw(v)
            case "3":
                # Transfer
                c = find(budget, "Origin: ")
                t = c
                v = get_cash_value("Value: ")
                c = find(budget, "Destination: ")
                budget[t].withdraw(v)
                budget[c].deposit(v)
            case "4":
                # Add category
                add_categories(budget)
            case "5":
                remove_category(budget)

        q = input("Would you like to update your budget? ").lower()
  
    total = 0
    # Write output file
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write(f"Budget for {year}\n")
        for item in budget:
            f.write(f"{item.category} = {item.cash}\n")
            total += item.cash
        f.write(f"Total = {total}\n")
    
    return print("Budget completed!")


if __name__ == "__main__":
    main()
