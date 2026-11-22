import json
import os
from typing import Dict, List, Optional
try:
    from models import Book, DigitalMedia, Item, Magazine
except ImportError:
    from task5_inventory_system.models import Book, DigitalMedia, Item, Magazine


class InventoryManager:
    """Enterprise Inventory Management and Tracking System."""

    def __init__(self):
        self.items: Dict[str, Item] = {}

    def add_item(self, item: Item) -> None:
        if item.asset_id in self.items:
            raise ValueError(f"Asset ID '{item.asset_id}' already exists in inventory.")
        self.items[item.asset_id] = item

    def remove_item(self, asset_id: str) -> bool:
        asset_id = asset_id.upper().strip()
        if asset_id in self.items:
            del self.items[asset_id]
            return True
        return False

    def get_item(self, asset_id: str) -> Optional[Item]:
        return self.items.get(asset_id.upper().strip())

    def checkout_asset(self, asset_id: str) -> str:
        item = self.get_item(asset_id)
        if not item:
            return f"Asset ID '{asset_id}' not found in registry."
        try:
            item.check_out()
            return f"Successfully checked out [{item.asset_id}] '{item.title}'."
        except ValueError as e:
            return f"Checkout failed: {e}"

    def return_asset(self, asset_id: str, days_overdue: int = 0) -> str:
        item = self.get_item(asset_id)
        if not item:
            return f"Asset ID '{asset_id}' not found in registry."
        try:
            item.return_asset()
            fee = item.calculate_late_fee(days_overdue)
            fee_msg = f" Late fee assessed: ${fee:.2f}" if fee > 0 else " No late fees."
            return f"Successfully returned [{item.asset_id}] '{item.title}'.{fee_msg}"
        except ValueError as e:
            return f"Return failed: {e}"

    def total_asset_value(self) -> float:
        return sum(item.price for item in self.items.values())

    def search_by_title(self, query: str) -> List[Item]:
        q = query.lower()
        return [item for item in self.items.values() if q in item.title.lower()]

    def generate_tabular_report(self) -> str:
        header = f"{'Asset ID':<10} {'Type':<14} {'Title':<28} {'Price':>10} {'Status':<14}"
        lines = [
            "=" * len(header),
            "              ENTERPRISE SMART INVENTORY AUDIT REPORT",
            "=" * len(header),
            header,
            "-" * len(header)
        ]

        for item in sorted(self.items.values(), key=lambda x: x.asset_id):
            meta = item.display_metadata()
            lines.append(
                f"{item.asset_id:<10} {meta['Type']:<14} {item.title[:26]:<28} ${item.price:>9.2f} {meta['Status']:<14}"
            )

        lines.append("-" * len(header))
        lines.append(f"Total Asset Count: {len(self.items)} | Total Inventory Value: ${self.total_asset_value():,.2f}")
        lines.append("=" * len(header))
        return "\n".join(lines)


def run_demo():
    mgr = InventoryManager()

    # Prepopulate items
    b1 = Book("BK-101", "Clean Code in Python", 45.99, "Mariano Anaya", 420, "978-1800560215")
    b2 = Book("BK-102", "Python Design Patterns", 39.50, "Chetan Giridhar", 280, "978-1785888038")
    m1 = Magazine("MG-201", "Python Developers Weekly", 12.00, 48, "TechPress Media")
    d1 = DigitalMedia("DM-301", "Microservices with FastAPI", 79.00, "MP4/H.264", 3200.0)

    for item in [b1, b2, m1, d1]:
        mgr.add_item(item)

    print(mgr.generate_tabular_report())

    print("\n--- Simulating Asset Transactions ---")
    print("1. Check out Book BK-101:")
    print("   ->", mgr.checkout_asset("BK-101"))

    print("\n2. Attempt duplicate check out of BK-101 (Encapsulation test):")
    print("   ->", mgr.checkout_asset("BK-101"))

    print("\n3. Return Book BK-101 with 5 days overdue (Polymorphic fee calc):")
    print("   ->", mgr.return_asset("BK-101", days_overdue=5))

    print("\n4. Check out & return Digital Media DM-301 with 4 days overdue:")
    print("   ->", mgr.checkout_asset("DM-301"))
    print("   ->", mgr.return_asset("DM-301", days_overdue=4))

    print("\n--- Updated Audit Report ---")
    print(mgr.generate_tabular_report())


if __name__ == "__main__":
    run_demo()
