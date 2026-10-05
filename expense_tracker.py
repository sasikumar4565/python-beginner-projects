print("===== EXPENSE TRACKER =====")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        expenses.append([name, amount])
        print("Expense added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")

            for expense in expenses:
                print(expense[0], "- ₹", expense[1])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense[1]

        print("Total Expenses: ₹", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
