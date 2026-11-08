# tests/test_my_assistant.py

from mock_model import MockModel
from my_assistant import OrderAssistant
from my_tool import OrderStatusTool


def make_assistant(model=None):
    """Create a fresh assistant for each test."""
    orders = {
        "E200": "being prepared",
        "E201": "shipped",
    }

    tool = OrderStatusTool(orders)

    if model is None:
        model = MockModel()

    return OrderAssistant(
        "Kelly", "You are Kelly, a helpful customer service assistant.", tool, model
    )


class SilentModel:
    """A model that returns with no answer."""

    def reply(self, instructions, history):
        return None


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


def test_unknown_request_uses_model():
    assistant = make_assistant()

    assert assistant.respond("hello") == "Hello! How can I help you today?"


def test_history_records_both_messages():
    assistant = make_assistant()

    assistant.respond("hello")

    assert len(assistant.history) == 2
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"


def test_model_returns_none():
    assistant = make_assistant(SilentModel())

    assert "try again" in assistant.respond("hello")
