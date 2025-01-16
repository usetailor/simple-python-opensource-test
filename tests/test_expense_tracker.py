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