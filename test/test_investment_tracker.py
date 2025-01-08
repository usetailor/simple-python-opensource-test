import pytest
from datetime import datetime
from investment_tracker import record_transaction


class TestInvestment:
    def test_record_transaction(self):
        print("test_record_transaction")
        record_transaction(100, "food", "Lunch at cafe")
        assert True
