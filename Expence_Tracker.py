print("----------Expense Tracker----------")

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add(self, amount, category):
        self.expenses.append((amount, category))

    def show(self):
        print("Item No    |  Price(in Rs)  |  Category")
        i = 1
        for exp in self.expenses:
            amt, cat = exp
            print(i, "           ", amt, "          ", cat)
            i += 1

    def total(self):
        s = 0
        for amt, _ in self.expenses:
            s += amt
        return s

tracker = ExpenseTracker()

while True:
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total")
    print("4. Exit")

    ch = input("Choose: ")

    if ch == "1":
        amt = float(input("Amount: "))
        cat = input("Category: ")
        tracker.add(amt, cat)

    elif ch == "2":
        tracker.show()

    elif ch == "3":
        print("Total =", tracker.total())

    elif ch == "4":
        break