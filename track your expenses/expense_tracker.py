# Class for individual expenses
class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        # Corrected typo: decription -> description
        self.description = description
        self.amount = amount

    # Optional: Add a string representation for easier viewing
    def __str__(self):
        return f"Date: {self.date}, Description: {self.description}, Amount: {self.amount:.2f}"

# Class to manage a collection of expenses
class ExpenseTracker:
    def __init__(self):
        # Consistent naming: expense -> expenses (plural for a list)
        self.expenses = []

    def add_expense(self, expense):
        # Corrected variable name: expenses -> expense (the parameter)
        # Corrected list name: self.expense -> self.expenses
        self.expenses.append(expense)
        # It's often better to have the confirmation print in the main loop
        # after the call, as you did, or return True/False from the method.

    def remove_expense(self, index):
        # Use 1-based index for user input, convert to 0-based for list access
        actual_index = index - 1
        if 0 <= actual_index < len(self.expenses):
            del self.expenses[actual_index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")

    # --- Added Missing Methods ---
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\n--- All Expenses ---")
        # Enumerate provides both index (starting from 0) and item
        for i, expense in enumerate(self.expenses):
            # Print with a 1-based index for user convenience
            print(f"{i+1}. {expense}") # Uses the __str__ method of Expense
        print("--------------------")

    def total_expenses(self):
        # Calculate total using a generator expression and sum()
        total = sum(expense.amount for expense in self.expenses)
        print(f"\nTotal amount of all expenses: {total:.2f}")

# --- Main function to run the tracker interface ---
# !!! Corrected Indentation: Moved main() outside the class !!!
def main():
    tracker = ExpenseTracker()

    # !!! Corrected Indentation: Moved while loop inside main() !!!
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            try: # Add error handling for amount input
                amount = float(input("Enter the amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue # Skip the rest of this loop iteration
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            # Corrected typo: sucessfully -> successfully
            print("Expense added successfully.")
        elif choice == "2":
            if not tracker.expenses:
                print("No expenses to remove.")
                continue
            tracker.view_expenses() # Show expenses with indices first
            try: # Add error handling for index input
                index = int(input("Enter the expense number to remove: "))
                tracker.remove_expense(index)
            except ValueError:
                print("Invalid index. Please enter a number.")
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# --- Script execution entry point ---
# !!! Added this block to actually call main() !!!
if __name__ == "__main__":
    main()