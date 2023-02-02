import requests

# Set up your API key and trading pair
API_KEY = "YOUR_API_KEY"
TRADING_PAIR = "ETH/BTC"


# Define a function to get the current price of the trading pair
def get_current_price():
    response = requests.get(f"https://api.exchange.com/v1/ticker/{TRADING_PAIR}")
    response_json = response.json()
    return response_json["last"]


# Define a function to create a new order
def create_order(side, quantity, price):
    payload = {
        "apiKey": API_KEY,
        "side": side,
        "quantity": quantity,
        "price": price
    }
    response = requests.post(f"https://api.exchange.com/v1/orders", json = payload)
    response_json = response.json()
    return response_json["orderId"]


# Define a function to check the status of an order
def check_order_status(order_id):
    response = requests.get(f"https://api.exchange.com/v1/orders/{order_id}")
    response_json = response.json()
    return response_json["status"]


# Set your desired quantity and price threshold
quantity = 1.0
price_threshold = 100.0

# Get the current price of the trading pair
current_price = get_current_price()

# Check if the current price is above the threshold
if current_price > price_threshold:
    # If so, create a new buy order
    order_id = create_order("buy", quantity, current_price)
    # Check the status of the order until it is filled
    order_status = check_order_status(order_id)
    while order_status != "filled":
        order_status = check_order_status(order_id)
    # Print a success message
    print(f"Successfully bought {quantity} {TRADING_PAIR} at {current_price}")
else:
    # If not, print a message saying that no action was taken
    print(f"Price of {TRADING_PAIR} is not above {price_threshold}. No action taken.")
