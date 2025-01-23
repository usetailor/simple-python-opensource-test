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

    def test_add_expense_manually(self):
        """
        Test if an expense can be manually added to the ExpenseTracker's expenses list.
        This test verifies that expenses can be added and retrieved correctly,
        and checks all attributes of the added expense.
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

        # Additional assertions to increase coverage
        self.assertEqual(tracker.expenses[0]["description"], "Groceries")
        self.assertEqual(tracker.expenses[0]["amount"], 50.00)
        self.assertEqual(tracker.expenses[0]["category"], "food")
        self.assertEqual(tracker.expenses[0]["date"], "2023-04-15")

        # Test adding an expense with a different category
        expense2 = {
            "description": "Bus ticket",
            "amount": 2.50,
            "category": "transport",
            "date": "2023-04-16"
        }
        tracker.expenses.append(expense2)

        self.assertEqual(len(tracker.expenses), 2)
        self.assertIn(expense2, tracker.expenses)
        self.assertEqual(tracker.expenses[1], expense2)

    def test_add_multiple_expenses(self):
        """
        Test if multiple expenses can be added to the ExpenseTracker's expenses list.
        This test verifies that expenses can be added and retrieved correctly,
        and checks all attributes of the added expenses.
        """
        tracker = ExpenseTracker()
        expense1 = {
            "description": "Groceries",
            "amount": 50.00,
            "category": "food",
            "date": "2023-04-15"
        }
        expense2 = {
            "description": "Movie tickets",
            "amount": 30.00,
            "category": "entertainment",
            "date": "2023-04-16"
        }

        # Add expenses to the tracker
        tracker.expenses.append(expense1)
        tracker.expenses.append(expense2)

        # Check if both expenses were added
        self.assertEqual(len(tracker.expenses), 2)
        self.assertIn(expense1, tracker.expenses)
        self.assertIn(expense2, tracker.expenses)

        # Check details of the first expense
        self.assertEqual(tracker.expenses[0]["description"], "Groceries")
        self.assertEqual(tracker.expenses[0]["amount"], 50.00)
        self.assertEqual(tracker.expenses[0]["category"], "food")
        self.assertEqual(tracker.expenses[0]["date"], "2023-04-15")

        # Check details of the second expense
        self.assertEqual(tracker.expenses[1]["description"], "Movie tickets")
        self.assertEqual(tracker.expenses[1]["amount"], 30.00)
        self.assertEqual(tracker.expenses[1]["category"], "entertainment")
        self.assertEqual(tracker.expenses[1]["date"], "2023-04-16")

        # Verify that the expenses are in the correct order
        self.assertEqual(tracker.expenses[0], expense1)
        self.assertEqual(tracker.expenses[1], expense2)

    def test_add_expense_manually(self):
        """
        Test if an expense can be manually added to the ExpenseTracker's expenses list.
        This test verifies that expenses can be added and retrieved correctly,
        and checks all attributes of the added expense.
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

        # Additional assertions to increase coverage
        self.assertEqual(tracker.expenses[0]["description"], "Groceries")
        self.assertEqual(tracker.expenses[0]["amount"], 50.00)
        self.assertEqual(tracker.expenses[0]["category"], "food")
        self.assertEqual(tracker.expenses[0]["date"], "2023-04-15")

        # Test adding an expense with a different category
        expense2 = {
            "description": "Bus ticket",
            "amount": 2.50,
            "category": "transport",
            "date": "2023-04-16"
        }
        tracker.expenses.append(expense2)

        self.assertEqual(len(tracker.expenses), 2)
        self.assertIn(expense2, tracker.expenses)
        self.assertEqual(tracker.expenses[1], expense2)

    def test_add_expense_manually(self):
        """
        Test if an expense can be manually added to the ExpenseTracker's expenses list.
        This test verifies that expenses can be added and retrieved correctly,
        and checks all attributes of the added expense.
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

        # Additional assertions to increase coverage
        self.assertEqual(tracker.expenses[0]["description"], "Groceries")
        self.assertEqual(tracker.expenses[0]["amount"], 50.00)
        self.assertEqual(tracker.expenses[0]["category"], "food")
        self.assertEqual(tracker.expenses[0]["date"], "2023-04-15")

        # Test adding an expense with a different category
        expense2 = {
            "description": "Bus ticket",
            "amount": 2.50,
            "category": "transport",
            "date": "2023-04-16"
        }
        tracker.expenses.append(expense2)

        self.assertEqual(len(tracker.expenses), 2)
        self.assertIn(expense2, tracker.expenses)
        self.assertEqual(tracker.expenses[1], expense2)