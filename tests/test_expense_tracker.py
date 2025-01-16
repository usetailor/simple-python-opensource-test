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
        This test verifies that:
        1. The expense is correctly added to the list.
        2. The length of the expenses list increases.
        3. The added expense can be retrieved from the list.
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

    def test_add_expense_manually(self):
        """
        Test if an expense can be manually added to the ExpenseTracker's expenses list.
        This test verifies that:
        1. The expense is correctly added to the list.
        2. The length of the expenses list increases.
        3. The added expense can be retrieved from the list.
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