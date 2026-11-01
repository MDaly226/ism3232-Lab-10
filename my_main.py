# my_main.py
# Author: Michael Daly

from my_assistant import OrderAssistant
from my_tool import OrderStatusTool

ORDERS = {
    "E200": "being prepared",
    "E201": "shipped",
    "E202": "out for delivery",
    "E203": "delivered",
}


order_tool = OrderStatusTool(ORDERS)

assistant = OrderAssistant(
    "Kelly",
    order_tool,
)


print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
