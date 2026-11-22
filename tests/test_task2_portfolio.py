import unittest
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task2_stock_tracker.portfolio import Holding, PortfolioTracker


class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.tracker = PortfolioTracker()

    def test_holding_calculations(self):
        h = Holding("AAPL", 10, 150.0, current_price=180.0)
        self.assertEqual(h.total_invested, 1500.0)
        self.assertEqual(h.current_market_value, 1800.0)
        self.assertEqual(h.profit_loss, 300.0)
        self.assertAlmostEqual(h.profit_loss_percentage, 20.0, places=2)

    def test_add_holding(self):
        self.tracker.add_holding("TSLA", 5, 200.0, current_price=220.0)
        self.assertIn("TSLA", self.tracker.holdings)
        self.assertEqual(self.tracker.holdings["TSLA"].shares, 5)

    def test_remove_holding(self):
        self.tracker.add_holding("GOOGL", 10, 100.0)
        self.assertTrue(self.tracker.remove_holding("GOOGL"))
        self.assertNotIn("GOOGL", self.tracker.holdings)
        self.assertFalse(self.tracker.remove_holding("UNKNOWN"))

    def test_summary_metrics(self):
        self.tracker.add_holding("STOCK1", 10, 100.0, current_price=120.0)
        self.tracker.add_holding("STOCK2", 10, 50.0, current_price=40.0)
        # Invested: 1000 + 500 = 1500
        # Market Val: 1200 + 400 = 1600
        # PL: +100
        m = self.tracker.get_summary_metrics()
        self.assertEqual(m["total_invested"], 1500.0)
        self.assertEqual(m["total_market_value"], 1600.0)
        self.assertEqual(m["total_profit_loss"], 100.0)

    def test_export_csv(self):
        self.tracker.add_holding("AAPL", 5, 200.0, current_price=210.0)
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
            tmp_path = tmp.name

        try:
            exported = self.tracker.export_summary_csv(tmp_path)
            self.assertTrue(os.path.exists(exported))
            with open(exported, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn("AAPL", content)
                self.assertIn("PORTFOLIO_TOTAL", content)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
