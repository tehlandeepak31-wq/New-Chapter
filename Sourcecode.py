# Display Welcome message
print("Welcome to the Daily Expense Tracker!")
#  Show menu option to the user
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
#  List to store all expenses values
expenses = []
#  Infinite loop to keep the program running until user exits
while True:
    # Take user choice as input
    choice = input()
    # Option 1: Add a new expense
    if choice == "1":
        amount = float(input())
        expenses.append(amount)
        print("Expense added successfully!")
     # Option 2: View all expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")
    # Option 3: Calculate total and average
    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = 0
            for expense in expenses:
                total += expense
            average = (total / len(expenses))
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")
    # Option 4: Clear all expenses
    elif choice == "4":
        expenses = []
        print("All expenses cleared.")
        
    # Option 5: Exit program
    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    # Handle invalid input
    else:
        print("Invalid choice. Please try again.")
