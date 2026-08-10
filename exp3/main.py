"""
Simple Python application for GitHub Actions CI/CD testing.
"""


def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total price."""
    if price < 0:
        raise ValueError("Price cannot be negative")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    return price * quantity


def create_message(name: str) -> str:
    """Create a greeting message."""
    if not name.strip():
        raise ValueError("Name cannot be empty")

    return f"Hello, {name}! Your code is running successfully."


def main() -> None:
    """Run the application."""
    name = "Developer"
    price = 100.0
    quantity = 3

    total = calculate_total(price, quantity)
    message = create_message(name)

    print(message)
    print(f"Price: ₹{price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: ₹{total:.2f}")


if __name__ == "__main__":
    main()
