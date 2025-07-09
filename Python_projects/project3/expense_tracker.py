import json
import os
import argparse
from datetime import datetime

EXPENSES_FILE = "expenses.json"

def load_expenses():
    """Load expenses from JSON file or return empty list."""
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    """Save expenses to JSON file."""
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

def add_expense(description, amount):
    """Add a new expense."""
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    expense = {
        "id": expense_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")

def update_expense(expense_id, description, amount):
    """Update an expense."""
    expenses = load_expenses()
    for expense in expenses:
        if expense['id'] == expense_id:
            expense['description'] = description
            expense['amount'] = amount
            expense['date'] = datetime.now().strftime("%Y-%m-%d")
            save_expenses(expenses)
            print(f"Expense {expense_id} updated")
            return
    print(f"Expense {expense_id} not found")

def delete_expense(expense_id):
    """Delete an expense."""
    expenses = load_expenses()
    expenses = [expense for expense in expenses if expense['id'] != expense_id]
    save_expenses(expenses)
    print("Expense deleted successfully")

def list_expenses():
    """List all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses found")
        return
    print("ID  Date       Description  Amount")
    for expense in expenses:
        print(f"{expense['id']:<4}{expense['date']:<11}{expense['description']:<13}${expense['amount']}")

def summary_expenses(month=None):
    """Show summary of expenses, optionally for a month."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses found")
        return
    if month:
        total = sum(expense['amount'] for expense in expenses
                    if expense['date'].startswith(f"2025-{month:02d}"))
        print(f"Total expenses for month {month}: ${total}")
    else:
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total expenses: ${total}")

def main():
    """Handle CLI commands."""
    parser = argparse.ArgumentParser(description="Simple Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add expense")
    parser_add.add_argument("--description", required=True)
    parser_add.add_argument("--amount", type=float, required=True)

    parser_update = subparsers.add_parser("update", help="Update expense")
    parser_update.add_argument("--id", type=int, required=True)
    parser_update.add_argument("--description", required=True)
    parser_update.add_argument("--amount", type=float, required=True)

    parser_delete = subparsers.add_parser("delete", help="Delete expense")
    parser_delete.add_argument("--id", type=int, required=True)

    subparsers.add_parser("list", help="List expenses")

    parser_summary = subparsers.add_parser("summary", help="Show summary")
    parser_summary.add_argument("--month", type=int, help="Month (1-12)")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        summary_expenses(args.month)

if __name__ == "__main__":
    main()
