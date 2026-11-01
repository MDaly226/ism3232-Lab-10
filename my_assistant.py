# my_assistant.py
# Author: Michael Daly


HANDOFF_WORDS = ["cancel", "address", "payment", "refund"]


class OrderAssistant:
    """A mock customer service assistant that checks order status."""

    def __init__(self, name, order_tool):
        """Set up the assistant with a name, tool, and empty history."""
        self.name = name
        self.order_tool = order_tool
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, and record the reply."""
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a response based on simple keyword rules."""
        text = user_message.lower()

        if self.needs_human(text):
            return (
                "I can't make changes to an order. "
                "I'm passing you to a customer service representative."
            )

        if "order" in text or "status" in text:
            return self.order_reply(user_message)

        if "hello" in text or "hi" in text:
            return (
                f"Hello! I'm {self.name}. I can help you check the status of an order."
            )

        return "I'm not sure how to help with that. I can check the status of an order."

    def needs_human(self, text):
        """Return True when the request needs a customer service employee."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def order_reply(self, user_message):
        """Use the order tool to answer an order-status question."""
        order_id = self.order_tool.find_order_id(user_message)

        if order_id is None:
            return "Which order? Please provide an order ID like E200."

        status = self.order_tool.get_status(order_id)

        if status is None:
            return "I couldn't find that order. Please check the order ID."

        return f"Order {order_id} is currently {status}."
