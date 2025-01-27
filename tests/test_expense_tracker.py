import pytest

from datetime import datetime
from expense_tracker import ExpenseTracker

class TestExpenseTracker:
    def test_expense_tracker_initialization(self):
        """
        Test if the ExpenseTracker is initialized with the correct default categories.
        """
        tracker = ExpenseTracker()
        expected_categories = {"food", "transport", "utilities", "entertainment", "other"}

        assert tracker.expenses == [], "Expenses should be an empty list upon initialization"
        assert tracker.categories == expected_categories, "Categories should match the default set"

    def test_add_new_category(self):
        """
        Test if a new category can be added to the ExpenseTracker.
        """
        tracker = ExpenseTracker()
        new_category = "healthcare"

        # Add the new category
        tracker.categories.add(new_category)

        assert new_category in tracker.categories, f"The new category '{new_category}' should be in the categories set"
        assert len(tracker.categories) == 6, "The categories set should now have 6 items"

    def test_remove_category(self):
        """
        Test if an existing category can be removed from the ExpenseTracker.
        """
        tracker = ExpenseTracker()
        category_to_remove = "entertainment"

        # Remove the category
        tracker.categories.remove(category_to_remove)

        assert category_to_remove not in tracker.categories, f"The category '{category_to_remove}' should not be in the categories set"
        assert len(tracker.categories) == 4, "The categories set should now have 4 items"
        assert tracker.categories == {"food", "transport", "utilities", "other"}, "The remaining categories should match the expected set"

    def test_add_expense(self):
        """
        Test if an expense can be added to the ExpenseTracker.
        This test checks if the expenses list is updated correctly when an expense is added.
        """
        tracker = ExpenseTracker()
        expense = {
            "amount": 50.0,
            "category": "food",
            "description": "Grocery shopping",
            "date": datetime.now().date()
        }

        # Add the expense
        tracker.expenses.append(expense)

        assert len(tracker.expenses) == 1, "The expenses list should have one item"
        assert tracker.expenses[0] == expense, "The added expense should match the original expense"
        assert tracker.expenses[0]["category"] in tracker.categories, "The expense category should be in the tracker's categories"