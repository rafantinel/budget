from datetime import date
import sys

class Budget:
    def __init__(self, category, cash):
        self.cash = cash
        self.category = category

    def deposit(self, value):
            self.cash += value

    def withdraw(self, value):
        if value <= self.cash:
            self.cash -= value
        else:
            return print("Not enough cash.")

# Create budget object and add to list
def add_categories(budget=[], n=100):

    c = []
    if budget:
        for item in budget:
            c.append(item.category)
        
    count = len(c)
    index = 0    
    while count < n:
        q = input("Add category (type 0 to stop): ").lower()
        if q == "0" and count == 0:
            sys.exit("No categories were added.")
        elif q == "0":
            break
        elif q == "exit":
            exit_program()
        else:
            if q in c:
                print("Category already added.")
                continue
            else:
                c.append(q)
                count += 1
                index += 1

        if count == n:
            print("Limit reached.")

    for i in range(count - index, count):
        cash = get_cash_value(f"Available cash for {c[i]}: ")
        budget.append(Budget(c[i], cash))

    return budget

# Remove objects from budget list
def remove_category(budget):
    
    count = len(budget)
    while True:
        r = find(budget, "Remove category (type 0 to stop): ")
        if r != None:
            budget.remove(budget[r])
            count -= 1
            if count == 0:
                sys.exit("All categories removed.")
       

# Find categories
def find(list, m):
    while True:
        q = input(m)
        if q == "0":
            return None
        elif q == "exit":
            exit_program()

        for i in range(0, len(list)):
            if list[i].category == q:
                return i
            if i == len(list) - 1:
                print("Category not found.")

# Get positive float
def get_cash_value(m):
    while True:
        cash = input(m)
        try:
            cash = float(cash)
            if cash > 0:
                break
            else:
                print("Must provide a positive number.")
                continue
        except:
            if cash == "exit":
                exit_program()
            else:
                print("Must provide a positive number.")
                continue
    return cash

# Get valid year
def get_year():
    while True:
        year = input("Budget year: ")
        try:
            year = int(year)
            if year >= date.today().year:
                break
            else:
                print("Year must be at least the current year.")
                continue
        except:
            if year == "exit":
                exit_program()
            else:
                print("Year must be at least the current year.")
                continue
    return year

def exit_program():
    return sys.exit("Program stopped.")
