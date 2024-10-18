# User class
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)

# Product class
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

# Order class
class Order:
    def __init__(self, order_id, user, products):
        self.order_id = order_id
        self.user = user
        self.products = products
        self.status = 'pending'
        self.total_price = sum([product.price for product in products])

    def set_status(self, status):
        self.status = status

# Payment class
class Payment:
    def __init__(self, payment_id, order, amount):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.payment_date = None

    def make_payment(self, payment_date):
        self.payment_date = payment_date
        self.order.set_status('completed')
