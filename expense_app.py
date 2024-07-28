# expense_app.py
from models import User

class ExpenseSharingApp:
    def __init__(self):
        self.users = {}
        self.expenses = []

    def add_user(self, name, email, mobile):
        if name.lower() not in self.users:
            self.users[name.lower()] = User(name, email, mobile)
            return "User added successfully"
        else:
            return "User already exists"

    def get_user_details(self, name):
        user = self.users.get(name.lower())
        if user:
            return vars(user)
        return "User not found"

    def add_expense(self, description, amount, paid_by, splits):
        if paid_by.lower() not in self.users:
            return "User who paid the amount does not exist."
        for user in splits.keys():
            if user.lower() not in self.users:
                return f"User {user} does not exist."
        self.expenses.append({
            'description': description,
            'amount': amount,
            'paid_by': paid_by.lower(),
            'splits': splits
        })
        return "Expense added successfully"

    def calculate_balances(self):
        balances = {user: 0 for user in self.users}
        for expense in self.expenses:
            total_amount = expense['amount']
            paid_by = expense['paid_by']
            splits = expense['splits']
            for user, amount in splits.items():
                balances[user] -= amount
            balances[paid_by] += total_amount
        return balances

    def generate_balance_sheet(self):
        balances = self.calculate_balances()
        return balances

    def split_equally(self, total_amount, participants):
        amount_per_person = total_amount / len(participants)
        return {user: amount_per_person for user in participants}

    def split_exact(self, exact_amounts):
        total_amount = sum(exact_amounts.values())
        return exact_amounts, total_amount

    def split_percentage(self, percentages, total_amount):
        if sum(percentages.values()) != 100:
            return "Percentages do not add up to 100"
        return {user: (percent / 100) * total_amount for user, percent in percentages.items()}
