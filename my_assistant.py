# my_assistant.py
# Author: Michael Daly


HANDOFF_WORDS = ["cancel", "address", "payment", "refund"]


class OrderAssistant:
    """An order assistant that uses rules, a tool, and an AI model."""

    def __init__(self, name, instructions, order_tool, model):
        """Set up the assistant with a name, tool, and empty history."""
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, and record the reply."""
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Use rules first, then ask the model for other questions."""
        text = user_message.lower()

        if self.needs_human(text):
            return (
                "I can't make changes to an order. "
                "I'm passing you to a customer service representative."
            )

        if "order" in text or "status" in text:
            return self.order_reply(user_message)

        return self.model_reply()

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

    def model_reply(self):
        """Ask the model for a response and handle any missing answers."""
        reply = self.model.reply(self.instructions, self.history)

        if reply is None:
            return (
                "Sorry, I can't answer that right now. "
                "Please try again in a few moments."
            )
        return reply
