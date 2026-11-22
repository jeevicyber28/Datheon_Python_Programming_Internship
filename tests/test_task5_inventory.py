import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task5_inventory_system.models import Item, Book, Magazine, DigitalMedia
from task5_inventory_system.inventory import InventoryManager


class TestInventorySystem(unittest.TestCase):

    def test_abc_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Item("ID-1", "Base Item", 10.0)

    def test_encapsulation_validation(self):
        b = Book("B-1", "Test Book", 20.0, "Author", 100, "ISBN-123")
        with self.assertRaises(ValueError):
            b.price = -5.0

        with self.assertRaises(ValueError):
            b.title = ""

    def test_polymorphism_late_fees(self):
        book = Book("B-1", "Python Guide", 30.0, "Author", 200, "123")
        mag = Magazine("M-1", "Tech Journal", 10.0, 5, "Press")
        media = DigitalMedia("D-1", "Video Course", 50.0, "MP4", 1500)

        # 3 days overdue
        self.assertEqual(book.calculate_late_fee(3), 1.50)  # 3 * 0.50
        self.assertEqual(mag.calculate_late_fee(3), 3.00)   # 3 * 1.00
        self.assertEqual(media.calculate_late_fee(3), 2.75) # 2.00 + 3*0.25

    def test_dunder_methods(self):
        b1 = Book("B-1", "Book 1", 20.0, "Author", 350, "111")
        b2 = Book("B-1", "Book 1 Copy", 25.0, "Author", 350, "111")
        b3 = Book("B-2", "Book 2", 20.0, "Author", 150, "222")

        self.assertEqual(b1, b2)  # __eq__ on asset_id
        self.assertNotEqual(b1, b3)
        self.assertEqual(len(b1), 350)  # __len__ returns pages
        self.assertIn("Book", repr(b1))  # __repr__

    def test_inventory_manager_operations(self):
        mgr = InventoryManager()
        b = Book("B-1", "Data Structures", 40.0, "Author", 300, "123")
        mgr.add_item(b)

        # Checkout
        res = mgr.checkout_asset("B-1")
        self.assertIn("Successfully checked out", res)
        self.assertTrue(b.is_checked_out)

        # Duplicate checkout prevention
        res_fail = mgr.checkout_asset("B-1")
        self.assertIn("failed", res_fail)

        # Return asset
        res_ret = mgr.return_asset("B-1", days_overdue=2)
        self.assertIn("Successfully returned", res_ret)
        self.assertFalse(b.is_checked_out)


if __name__ == "__main__":
    unittest.main()
