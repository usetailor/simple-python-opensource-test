import pytest
from investment_tracker import InvestmentTracker

class TestInvestment:
    """Test class for InvestmentTracker"""

    def test_record_transaction(self):
        """
        Test the record_transaction method of InvestmentTracker.
        Verifies that a transaction can be successfully recorded.
        """
        tracker = InvestmentTracker()
        result = tracker.record_transaction(25.50, "food", "Lunch at cafe")
        assert result == True
        assert len(tracker.expenses) == 1
        assert tracker.expenses[0]["amount"] == 25.50
        assert tracker.expenses[0]["category"] == "food"
        assert tracker.expenses[0]["description"] == "Lunch at cafe"
