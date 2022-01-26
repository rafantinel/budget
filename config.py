from datetime import date
import sys

class Budget:
    def __init__(self, cash):
        self.cash = cash

    def deposit(self, value):
        self.cash += value

    def withdraw(self, value):
        if value <= self.cash:
            self.cash -= value
        else:
            return print("Not enough cash.")

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
