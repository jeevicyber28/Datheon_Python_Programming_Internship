import csv
import os
from datetime import datetime
from typing import Dict, List, Optional


class Holding:
    def __init__(self, symbol: str, shares: float, buy_price: float, current_price: Optional[float] = None):
        self.symbol = symbol.upper().strip()
        self.shares = float(shares)
        self.buy_price = float(buy_price)
        self.current_price = float(current_price) if current_price is not None else self.buy_price

    @property
    def total_invested(self) -> float:
        return self.shares * self.buy_price

    @property
    def current_market_value(self) -> float:
        return self.shares * self.current_price

    @property
    def profit_loss(self) -> float:
        return self.current_market_value - self.total_invested

    @property
    def profit_loss_percentage(self) -> float:
        if self.total_invested == 0:
            return 0.0
        return (self.profit_loss / self.total_invested) * 100.0


class PortfolioTracker:
    def __init__(self, market_data_path: Optional[str] = None):
        self.holdings: Dict[str, Holding] = {}
        self.market_prices: Dict[str, float] = {}
        if market_data_path and os.path.exists(market_data_path):
            self.load_market_prices(market_data_path)

    def load_market_prices(self, csv_filepath: str) -> None:
        """Loads benchmark market prices from a CSV file."""
        try:
            with open(csv_filepath, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    symbol = row.get("Symbol", "").strip().upper()
                    price_str = row.get("Price", "") or row.get("CurrentPrice", "")
                    if symbol and price_str:
                        try:
                            self.market_prices[symbol] = float(price_str)
                        except ValueError:
                            pass
        except Exception as e:
            print(f"Warning: Could not read market data from {csv_filepath}: {e}")

    def add_holding(self, symbol: str, shares: float, buy_price: float, current_price: Optional[float] = None) -> Holding:
        sym = symbol.upper().strip()
        if current_price is None:
            current_price = self.market_prices.get(sym, buy_price)

        if sym in self.holdings:
            existing = self.holdings[sym]
            new_shares = existing.shares + shares
            # Weighted average buy price
            new_buy_price = ((existing.shares * existing.buy_price) + (shares * buy_price)) / new_shares
            holding = Holding(sym, new_shares, new_buy_price, current_price)
            self.holdings[sym] = holding
        else:
            holding = Holding(sym, shares, buy_price, current_price)
            self.holdings[sym] = holding
        return self.holdings[sym]

    def remove_holding(self, symbol: str) -> bool:
        sym = symbol.upper().strip()
        if sym in self.holdings:
            del self.holdings[sym]
            return True
        return False

    def update_price(self, symbol: str, new_price: float) -> bool:
        sym = symbol.upper().strip()
        if sym in self.holdings:
            self.holdings[sym].current_price = float(new_price)
            return True
        return False

    def get_summary_metrics(self) -> Dict[str, float]:
        total_invested = sum(h.total_invested for h in self.holdings.values())
        total_market_val = sum(h.current_market_value for h in self.holdings.values())
        total_pl = total_market_val - total_invested
        total_pl_pct = (total_pl / total_invested * 100.0) if total_invested > 0 else 0.0

        return {
            "total_invested": total_invested,
            "total_market_value": total_market_val,
            "total_profit_loss": total_pl,
            "total_profit_loss_pct": total_pl_pct
        }

    def export_summary_csv(self, output_path: str) -> str:
        """Persists current portfolio metrics to CSV."""
        fieldnames = [
            "Timestamp", "Symbol", "Shares", "BuyPrice", "CurrentPrice",
            "TotalInvested", "CurrentMarketValue", "ProfitLoss", "ProfitLossPct"
        ]
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file_exists = os.path.exists(output_path)
        with open(output_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            for h in self.holdings.values():
                writer.writerow([
                    now_str,
                    h.symbol,
                    f"{h.shares:.2f}",
                    f"{h.buy_price:.2f}",
                    f"{h.current_price:.2f}",
                    f"{h.total_invested:.2f}",
                    f"{h.current_market_value:.2f}",
                    f"{h.profit_loss:.2f}",
                    f"{h.profit_loss_percentage:.2f}%"
                ])

            # Summary row
            metrics = self.get_summary_metrics()
            writer.writerow([
                now_str,
                "PORTFOLIO_TOTAL",
                "-",
                "-",
                "-",
                f"{metrics['total_invested']:.2f}",
                f"{metrics['total_market_value']:.2f}",
                f"{metrics['total_profit_loss']:.2f}",
                f"{metrics['total_profit_loss_pct']:.2f}%"
            ])
        return output_path

    def print_table(self) -> None:
        if not self.holdings:
            print("\nPortfolio is currently empty. Add positions to get started.")
            return

        header = f"{'Symbol':<8} {'Shares':>8} {'Buy Price':>12} {'Curr Price':>12} {'Invested':>12} {'Market Val':>12} {'P&L ($)':>12} {'P&L (%)':>10}"
        print("\n" + "=" * len(header))
        print("               DATHEON STOCK PORTFOLIO PERFORMANCE TRACKER")
        print("=" * len(header))
        print(header)
        print("-" * len(header))

        for h in self.holdings.values():
            pl_sign = "+" if h.profit_loss >= 0 else ""
            print(
                f"{h.symbol:<8} {h.shares:>8.2f} ${h.buy_price:>11.2f} ${h.current_price:>11.2f} "
                f"${h.total_invested:>11.2f} ${h.current_market_value:>11.2f} "
                f"{pl_sign}${h.profit_loss:>10.2f} {pl_sign}{h.profit_loss_percentage:>9.2f}%"
            )

        print("-" * len(header))
        m = self.get_summary_metrics()
        pl_sign = "+" if m['total_profit_loss'] >= 0 else ""
        print(
            f"{'TOTAL':<8} {'-':>8} {'-':>12} {'-':>12} "
            f"${m['total_invested']:>11.2f} ${m['total_market_value']:>11.2f} "
            f"{pl_sign}${m['total_profit_loss']:>10.2f} {pl_sign}{m['total_profit_loss_pct']:>9.2f}%"
        )
        print("=" * len(header))


def interactive_cli():
    base_dir = os.path.dirname(__file__)
    csv_dataset = os.path.join(base_dir, "sp500_tickers.csv")
    tracker = PortfolioTracker(csv_dataset)

    # Pre-populate with realistic starter holdings
    tracker.add_holding("AAPL", 15, 185.00)
    tracker.add_holding("MSFT", 10, 390.00)
    tracker.add_holding("NVDA", 25, 110.00)

    summary_file = os.path.join(base_dir, "portfolio_summary.csv")

    while True:
        tracker.print_table()
        print("\nOptions:")
        print("1. Add/Update Stock Position")
        print("2. Remove Stock Position")
        print("3. Update Current Market Price")
        print("4. Export Summary to CSV ('portfolio_summary.csv')")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()
        if choice == "1":
            sym = input("Enter ticker symbol (e.g. GOOGL): ").strip().upper()
            try:
                shares = float(input("Enter number of shares: ").strip())
                buy_price = float(input("Enter buy price ($): ").strip())
                tracker.add_holding(sym, shares, buy_price)
                print(f"Successfully added/updated {sym}!")
            except ValueError:
                print("Invalid number entered. Please enter valid numeric values.")

        elif choice == "2":
            sym = input("Enter ticker symbol to remove: ").strip().upper()
            if tracker.remove_holding(sym):
                print(f"Removed {sym} from portfolio.")
            else:
                print(f"Symbol {sym} not found in portfolio.")

        elif choice == "3":
            sym = input("Enter ticker symbol: ").strip().upper()
            try:
                price = float(input("Enter new market price ($): ").strip())
                if tracker.update_price(sym, price):
                    print(f"Updated price for {sym} to ${price:.2f}.")
                else:
                    print(f"Symbol {sym} not found in active portfolio.")
            except ValueError:
                print("Invalid numeric price.")

        elif choice == "4":
            tracker.export_summary_csv(summary_file)
            print(f"Exported portfolio summary successfully to {summary_file}")

        elif choice == "5":
            tracker.export_summary_csv(summary_file)
            print(f"Saved latest portfolio status to {summary_file}. Exiting.")
            break
        else:
            print("Invalid option. Please enter 1-5.")


if __name__ == "__main__":
    interactive_cli()
