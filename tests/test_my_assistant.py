# tests/test_my_assistant.py

from my_assistant import OrderAssistant
from my_tool import OrderStatusTool


def make_assistant():
    """Create a fresh assistant for each test."""
    orders = {
        "E200": "being prepared",
        "E201": "shipped",
    }

    tool = OrderStatusTool(orders)
    return OrderAssistant("Kelly", tool)


def test_tool_finds_order_status():
    tool = OrderStatusTool({"E201": "shipped"})
    assert tool.get_status("E201") == "shipped"


def test_order_question_uses_tool():
    assistant = make_assistant()

    assert (
        assistant.respond("What is the status of order E201?")
        == "Order E201 is currently shipped."
    )


def test_missing_order_id_gets_helpful_reply():
    assistant = make_assistant()

    assert "provide an order ID" in assistant.respond("What is the status of my order?")


def test_handoff_request_goes_to_person():
    assistant = make_assistant()

    assert "customer service representative" in assistant.respond(
        "Please cancel order E201"
    )


def test_unknown_request_gets_safe_reply():
    assistant = make_assistant()

    assert "not sure" in assistant.respond("What laptops do you sell?")


def test_history_records_both_messages():
    assistant = make_assistant()

    assistant.respond("hello")

    assert len(assistant.history) == 2
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"
