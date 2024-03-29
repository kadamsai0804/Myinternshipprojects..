class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def show_summary(self):
        print("Expense Summary:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. Show Summary")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully!")
        elif choice == '2':
            tracker.show_summary()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
