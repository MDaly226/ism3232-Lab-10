# my_main.py
# Author: Michael Daly

from my_assistant import OrderAssistant
from my_tool import OrderStatusTool
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """Your are Kelly, a helpful customer service assistant.
Answer customer questions in one short and friendly sentence.
Our business hours are Monday through Saturday, 9 AM to 6 PM.
Orders typically ship within 3 to 5 business days from date of purchase.
Returns are accepted within 30 days but only if the customer has their receipt.
Only provide facts that appear in these instructions.
If you do not know an answer, say you don't know and offer to connect the customer with a customer service representative."""

ORDERS = {
    "E200": "being prepared",
    "E201": "shipped",
    "E202": "out for delivery",
    "E203": "delivered",
}


order_tool = OrderStatusTool(ORDERS)
model = OllamaModel(MODEL_NAME)

assistant = OrderAssistant("Kelly", INSTRUCTIONS, order_tool, model)


print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
