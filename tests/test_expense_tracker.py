import unittest

from expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def test_default_categories(self):
        """
        Test if the ExpenseTracker initializes with the correct default categories.
        """
        tracker = ExpenseTracker()
        expected_categories = {"food", "transport", "utilities", "entertainment", "other"}
        self.assertEqual(tracker.categories, expected_categories)

    def test_initial_expenses_empty(self):
        """
        Test if the ExpenseTracker initializes with an empty expenses list.
        """
        tracker = ExpenseTracker()
        self.assertEqual(len(tracker.expenses), 0)
        self.assertListEqual(tracker.expenses, [])

    def test_add_new_category(self):
        """
        Test if a new category can be added to the ExpenseTracker.
        """
        tracker = ExpenseTracker()
        new_category = "healthcare"
        tracker.categories.add(new_category)
        self.assertIn(new_category, tracker.categories)
        self.assertEqual(len(tracker.categories), 6)  # 5 default + 1 new

    def test_expenses_attribute(self):
        """
        Test if the ExpenseTracker initializes with an empty expenses list
        and if we can add an expense manually.
        """
        tracker = ExpenseTracker()

        # Check initial state
        self.assertEqual(len(tracker.expenses), 0)
        self.assertIsInstance(tracker.expenses, list)

        # Manually add an expense
        expense = {
            "description": "Groceries",
            "amount": 50.00,
            "category": "food",
            "date": "2023-04-15"
        }
        tracker.expenses.append(expense)

        # Check if the expense was added
        self.assertEqual(len(tracker.expenses), 1)
        self.assertIn(expense, tracker.expenses)
        self.assertEqual(tracker.expenses[0], expense)

    def test_add_expense_manually(self):
        """
        Test if an expense can be manually added to the ExpenseTracker's expenses list.
        This test works with the current implementation of ExpenseTracker and verifies
        that we can add an expense to the list and retrieve it correctly.
        """
        tracker = ExpenseTracker()
        expense = {
            "description": "Groceries",
            "amount": 50.00,
            "category": "food",
            "date": "2023-04-15"
        }

        # Manually add the expense to the expenses list
        tracker.expenses.append(expense)

        self.assertEqual(len(tracker.expenses), 1)
        self.assertIn(expense, tracker.expenses)
        self.assertEqual(tracker.expenses[0], expense)

        # Additional checks to increase coverage
        self.assertEqual(tracker.expenses[0]["description"], "Groceries")
        self.assertEqual(tracker.expenses[0]["amount"], 50.00)
        self.assertEqual(tracker.expenses[0]["category"], "food")
        self.assertEqual(tracker.expenses[0]["date"], "2023-04-15")

    def test_add_multiple_expenses(self):
        """
        Test if multiple expenses can be added to the ExpenseTracker's expenses list.
        This test verifies that we can add multiple expenses to the list and retrieve them correctly.
        It also checks if the expenses are stored in the order they were added.
        """
        tracker = ExpenseTracker()
        expenses = [
            {
                "description": "Groceries",
                "amount": 50.00,
                "category": "food",
                "date": "2023-04-15"
            },
            {
                "description": "Bus ticket",
                "amount": 2.50,
                "category": "transport",
                "date": "2023-04-16"
            },
            {
                "description": "Movie",
                "amount": 15.00,
                "category": "entertainment",
                "date": "2023-04-17"
            }
        ]

        # Add multiple expenses to the expenses list
        for expense in expenses:
            tracker.expenses.append(expense)

        # Check if all expenses were added
        self.assertEqual(len(tracker.expenses), 3)

        # Check if expenses were added in the correct order
        for i, expense in enumerate(expenses):
            self.assertEqual(tracker.expenses[i], expense)
            self.assertEqual(tracker.expenses[i]["description"], expense["description"])
            self.assertEqual(tracker.expenses[i]["amount"], expense["amount"])
            self.assertEqual(tracker.expenses[i]["category"], expense["category"])
            self.assertEqual(tracker.expenses[i]["date"], expense["date"])

        # Check if categories are still intact
        self.assertSetEqual(tracker.categories, {"food", "transport", "utilities", "entertainment", "other"})

    def test_add_expense_manually(self):
        """
        Test if an expense can be manually added to the ExpenseTracker's expenses list.
        This test works with the current implementation of ExpenseTracker and verifies
        that we can add an expense to the list and retrieve it correctly.
        """
        tracker = ExpenseTracker()
        expense = {
            "description": "Groceries",
            "amount": 50.00,
            "category": "food",
            "date": "2023-04-15"
        }

        # Manually add the expense to the expenses list
        tracker.expenses.append(expense)

        self.assertEqual(len(tracker.expenses), 1)
        self.assertIn(expense, tracker.expenses)
        self.assertEqual(tracker.expenses[0], expense)

        # Additional checks to increase coverage
        self.assertEqual(tracker.expenses[0]["description"], "Groceries")
        self.assertEqual(tracker.expenses[0]["amount"], 50.00)
        self.assertEqual(tracker.expenses[0]["category"], "food")
        self.assertEqual(tracker.expenses[0]["date"], "2023-04-15")