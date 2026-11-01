README.md

Author: Michael Daly

My Mini-Project: An Order Status Assistant

The mini-project I decided to make is a mock order-status assistant for a electronics store. The assistant can look up the status of an order when the customer provides a valid order ID, though the order information is just mock data and isnt real. Requests involving cancellations, address changes, payments, or refunds are passed to a "real" customer service rep because those requests would needs permission to change customer or order info. Requests that the assistant doesn't understand receive a safe response instead of the bot making up an answer. If the system used real customer data, a potential problem could be accidentally showing private order info to someone who isnt authorized to see it.