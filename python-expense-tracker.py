import csv
from datetime import datetime

class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        self.date = datetime.now().strftime("%m-%d-%Y %H:%M")
    
    def __str__(self):
        return f"{self.date} | {self.category} | ${self.amount:.2f}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        expense = Expense(category, amount)
        self.expenses.append(expense)
        print("Expense added")

    def show_expense(self):
        if not self.expenses:
            print("No expneses saved")
            return
        print("\n--- All Expenses ---")
        for e in self.expenses: 
            print(e)

    def save_to_csv(self, filename="expenses.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])
            for e in self.expenses:
                writer.writerow([e.date, e.category, e.amount])
        print(f"File saved to {filename}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense\n2. Show Expenses\n3. Save & Exit\n")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter a category: ").lower()
            amount = float(input("Please enter an amount: "))
            tracker.add_expense(category, amount)

        if choice == "2":
            tracker.show_expense()

        if choice == "3":
            tracker.save_to_csv()
            break

if __name__ == "__main__":
    main()