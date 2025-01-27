import pytest

from investment_tracker import InvestmentTracker

class TestInvestment:
    """Test class for InvestmentTracker functionality."""

    def test_record_transaction(self):
        """
        Test the record_transaction method of InvestmentTracker.

        This test creates an InvestmentTracker instance, records a transaction,
        and checks if the transaction was added successfully.
        """
        tracker = InvestmentTracker()
        result = tracker.record_transaction(25.50, "food", "Lunch at cafe")
        assert result == True
        assert len(tracker.expenses) == 1
        assert tracker.expenses[0]["amount"] == 25.50
        assert tracker.expenses[0]["category"] == "food"
        assert tracker.expenses[0]["description"] == "Lunch at cafe"

    def test_calculate_overall_spending(self):
        """
        Test the calculate_overall_spending method of InvestmentTracker.

        This test creates an InvestmentTracker instance, records multiple transactions,
        and checks if the total spending is calculated correctly.
        """
        tracker = InvestmentTracker()
        tracker.record_transaction(25.50, "food", "Lunch at cafe")
        tracker.record_transaction(35.00, "transport", "Uber ride")
        tracker.record_transaction(150.00, "utilities", "Electricity bill")

        total_spending = tracker.calculate_overall_spending()
        expected_total = 25.50 + 35.00 + 150.00

        assert total_spending == pytest.approx(expected_total)

    def test_filter_by_category(self):
        """
        Test the filter_by_category method of InvestmentTracker.

        This test creates an InvestmentTracker instance, records transactions
        in different categories, and checks if filtering by a specific category
        returns only the expenses for that category.
        """
        tracker = InvestmentTracker()
        tracker.record_transaction(25.50, "food", "Lunch at cafe")
        tracker.record_transaction(35.00, "transport", "Uber ride")
        tracker.record_transaction(15.00, "food", "Snacks")
        tracker.record_transaction(150.00, "utilities", "Electricity bill")

        food_expenses = tracker.filter_by_category("food")

        assert len(food_expenses) == 2
        assert all(expense["category"] == "food" for expense in food_expenses)
        assert sum(expense["amount"] for expense in food_expenses) == pytest.approx(40.50)

    def test_register_new_category(self):
        """
        Test the register_new_category method of InvestmentTracker.

        This test creates an InvestmentTracker instance, registers a new category,
        and checks if the category was added successfully. It also tests that
        adding an existing category returns False and that invalid inputs raise
        appropriate exceptions.
        """
        tracker = InvestmentTracker()

        # Test adding a new category
        result = tracker.register_new_category("savings")
        assert result == True
        assert "savings" in tracker.categories

        # Test adding an existing category
        result = tracker.register_new_category("food")
        assert result == False

        # Test adding an invalid category (empty string)
        with pytest.raises(ValueError):
            tracker.register_new_category("")

        # Test adding an invalid category (non-string)
        with pytest.raises(ValueError):
            tracker.register_new_category(123)

    def test_compute_category_sum(self):
        """
        Test the compute_category_sum method of InvestmentTracker.

        This test creates an InvestmentTracker instance, records transactions
        in different categories (including multiple transactions in the same category),
        and checks if the sum for a specific category is calculated correctly.
        It also verifies that an invalid category raises a ValueError.
        """
        tracker = InvestmentTracker()
        tracker.record_transaction(25.50, "food", "Lunch at cafe")
        tracker.record_transaction(35.00, "transport", "Uber ride")
        tracker.record_transaction(15.00, "food", "Snacks")
        tracker.record_transaction(150.00, "utilities", "Electricity bill")

        # Test sum for food category
        food_sum = tracker.compute_category_sum("food")
        assert food_sum == pytest.approx(40.50)

        # Test sum for transport category
        transport_sum = tracker.compute_category_sum("transport")
        assert transport_sum == pytest.approx(35.00)

        # Test invalid category
        with pytest.raises(ValueError):
            tracker.compute_category_sum("invalid_category")

    def test_add_bread_and_milk(self):
        """
        Test the add_bread and add_milk methods of InvestmentTracker.

        This test creates an InvestmentTracker instance, calls the add_bread
        and add_milk methods, and checks if the transactions were added
        correctly to the expenses list with the proper amount, category,
        and description.
        """
        tracker = InvestmentTracker()

        # Test add_bread method
        tracker.add_bread()
        assert len(tracker.expenses) == 1
        assert tracker.expenses[0]["amount"] == 100
        assert tracker.expenses[0]["category"] == "food"
        assert tracker.expenses[0]["description"] == "Bread"

        # Test add_milk method
        tracker.add_milk()
        assert len(tracker.expenses) == 2
        assert tracker.expenses[1]["amount"] == 100
        assert tracker.expenses[1]["category"] == "food"
        assert tracker.expenses[1]["description"] == "Milk"

        # Verify total spending
        total_spending = tracker.calculate_overall_spending()
        assert total_spending == 200

    def test_record_transaction_invalid_category(self):
        """
        Test that attempting to record a transaction with an invalid category
        raises a ValueError.

        This test creates an InvestmentTracker instance and tries to record
        a transaction with a category that doesn't exist in the predefined
        categories. It checks if a ValueError is raised with the appropriate
        error message.
        """
        tracker = InvestmentTracker()

        with pytest.raises(ValueError) as excinfo:
            tracker.record_transaction(50.00, "invalid_category", "Test transaction")

        assert "Category must be one of:" in str(excinfo.value)
        assert all(category in str(excinfo.value) for category in tracker.categories)

    def test_record_transaction_invalid_amount(self):
        """
        Test that attempting to record a transaction with an invalid amount
        (non-positive number) raises a ValueError.

        This test creates an InvestmentTracker instance and tries to record
        transactions with zero and negative amounts. It checks if a ValueError
        is raised in both cases with the appropriate error message.
        """
        tracker = InvestmentTracker()

        # Test with zero amount
        with pytest.raises(ValueError) as excinfo:
            tracker.record_transaction(0, "food", "Invalid transaction")
        assert "Amount must be a positive number" in str(excinfo.value)

        # Test with negative amount
        with pytest.raises(ValueError) as excinfo:
            tracker.record_transaction(-50.00, "food", "Invalid transaction")
        assert "Amount must be a positive number" in str(excinfo.value)

        # Verify that no transactions were added
        assert len(tracker.expenses) == 0