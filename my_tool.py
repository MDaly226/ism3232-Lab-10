# my_tool.py
# Author: Michael Daly


class OrderStatusTool:
    """A tool that stores and looks up order status information."""

    def __init__(self, orders):
        """Stores the order information this tool can search."""
        self.orders = orders

    def find_order_id(self, text):
        """Return the first known order ID found in the message, or None."""
        for order_id in self.orders:
            if order_id in text.upper():
                return order_id
        return None

    def get_status(self, order_id):
        """Return the status for an order, or None if it does not exist."""
        if order_id in self.orders:
            return self.orders[order_id]
        return None
