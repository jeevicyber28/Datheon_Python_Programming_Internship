from abc import ABC, abstractmethod
from typing import Any, Dict


class Item(ABC):
    """
    Abstract Base Class representing an enterprise library or organization asset.
    Demonstrates Abstraction, Encapsulation, and Dunder Methods.
    """

    def __init__(self, asset_id: str, title: str, price: float):
        self.__asset_id: str = asset_id.strip().upper()
        self.__title: str = title.strip()
        self.__price: float = 0.0
        self.price = price  # Uses setter for validation
        self.__is_checked_out: bool = False

    # Property Getters & Setters (Encapsulation)
    @property
    def asset_id(self) -> str:
        return self.__asset_id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str):
        if not value or not value.strip():
            raise ValueError("Title cannot be empty.")
        self.__title = value.strip()

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = float(value)

    @property
    def is_checked_out(self) -> bool:
        return self.__is_checked_out

    def check_out(self) -> None:
        if self.__is_checked_out:
            raise ValueError(f"Asset '{self.__asset_id}' is already checked out.")
        self.__is_checked_out = True

    def return_asset(self) -> None:
        if not self.__is_checked_out:
            raise ValueError(f"Asset '{self.__asset_id}' was not checked out.")
        self.__is_checked_out = False

    # Abstract Methods to enforce Polymorphism in subclasses
    @abstractmethod
    def calculate_late_fee(self, days_overdue: int) -> float:
        """Calculate fine based on item category and days overdue."""
        pass

    @abstractmethod
    def display_metadata(self) -> Dict[str, Any]:
        """Return a dictionary of item metadata."""
        pass

    # Magic / Dunder Methods
    def __str__(self) -> str:
        status = "Checked Out" if self.__is_checked_out else "Available"
        return f"[{self.__asset_id}] {self.__title} (${self.__price:.2f}) - {status}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.__asset_id!r}, title={self.__title!r}, price={self.__price!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Item):
            return self.__asset_id == other.asset_id
        return False


class Book(Item):
    """Derived class representing a physical or digital book."""

    def __init__(self, asset_id: str, title: str, price: float, author: str, pages: int, isbn: str):
        super().__init__(asset_id, title, price)
        self.author = author
        self.pages = max(1, int(pages))
        self.isbn = isbn

    def calculate_late_fee(self, days_overdue: int) -> float:
        # Standard book late fee: $0.50 per day
        return max(0.0, days_overdue * 0.50)

    def display_metadata(self) -> Dict[str, Any]:
        return {
            "Type": "Book",
            "AssetID": self.asset_id,
            "Title": self.title,
            "Author": self.author,
            "Pages": self.pages,
            "ISBN": self.isbn,
            "Price": f"${self.price:.2f}",
            "Status": "Checked Out" if self.is_checked_out else "Available"
        }

    def __len__(self) -> int:
        return self.pages


class Magazine(Item):
    """Derived class representing a periodic publication."""

    def __init__(self, asset_id: str, title: str, price: float, issue_number: int, publisher: str):
        super().__init__(asset_id, title, price)
        self.issue_number = int(issue_number)
        self.publisher = publisher

    def calculate_late_fee(self, days_overdue: int) -> float:
        # Magazines have higher late fee due to timeliness: $1.00 per day
        return max(0.0, days_overdue * 1.00)

    def display_metadata(self) -> Dict[str, Any]:
        return {
            "Type": "Magazine",
            "AssetID": self.asset_id,
            "Title": self.title,
            "Issue": self.issue_number,
            "Publisher": self.publisher,
            "Price": f"${self.price:.2f}",
            "Status": "Checked Out" if self.is_checked_out else "Available"
        }

    def __len__(self) -> int:
        return self.issue_number


class DigitalMedia(Item):
    """Derived class representing digital assets like software, courses, audiobooks."""

    def __init__(self, asset_id: str, title: str, price: float, format_type: str, file_size_mb: float):
        super().__init__(asset_id, title, price)
        self.format_type = format_type
        self.file_size_mb = float(file_size_mb)

    def calculate_late_fee(self, days_overdue: int) -> float:
        # Digital media auto-revokes license after 3 days: $2.00 flat + $0.25/day
        if days_overdue <= 0:
            return 0.0
        return 2.00 + (days_overdue * 0.25)

    def display_metadata(self) -> Dict[str, Any]:
        return {
            "Type": "DigitalMedia",
            "AssetID": self.asset_id,
            "Title": self.title,
            "Format": self.format_type,
            "SizeMB": f"{self.file_size_mb:.1f} MB",
            "Price": f"${self.price:.2f}",
            "Status": "Checked Out" if self.is_checked_out else "Available"
        }

    def __len__(self) -> int:
        return int(self.file_size_mb)
