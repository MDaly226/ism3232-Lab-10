README.md

Author: Michael Daly

My Mini-Project: An Order Status Assistant

The mini-project I decided to make is a mock order-status assistant for a electronics store. The assistant can look up the status of an order when the customer provides a valid order ID, though the order information is just mock data and isnt real. Requests involving cancellations, address changes, payments, or refunds are passed to a "real" customer service rep because those requests would needs permission to change customer or order info. Requests that the assistant doesn't understand receive a safe response instead of the bot making up an answer. If the system used real customer data, a potential problem could be accidentally showing private order info to someone who isnt authorized to see it.


Week 11: Adding an AI model to my assistant

This week I updated my order assistant to be able to use the Ollama AI model for questions that arent handled by its existing rules. When I asked about business hours it returned back with the correct information "Our business hours are Monday through Saturday, 9 AM to 6 PM.". I tested a question about international shipping because its not mentioned in the instructions to see if it came back with the current unkown response or if it made something up. It came back with "I don't have that information in the provided instructions.". I kept order status lookups, and requests about cancellations, refunds, payments, and address changes the same requiring a real customer service rep to step in because these are more complex tasks that should be handled by people rather than the bot. 