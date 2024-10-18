# Function to process orders and reduce stock levels
def process_orders(products_stock, sales_orders, threshold=10):
    for order in sales_orders:
        product_id, quantity = order['product_id'], order['quantity']
        if product_id in products_stock:
            if products_stock[product_id] >= quantity:
                products_stock[product_id] -= quantity
                if products_stock[product_id] < threshold:
                    print(f"Alert: Product {product_id} needs restocking!")
            else:
                print(f"Error: Insufficient stock for Product {product_id}.")
        else:
            print(f"Error: Product {product_id} does not exist in stock.")
    return products_stock

# Sample data
products_stock = {
    1: 20,  # Product 1 has 20 units
    2: 5,   # Product 2 has 5 units
}

sales_orders = [
    {'product_id': 1, 'quantity': 5},
    {'product_id': 2, 'quantity': 3},
]

updated_stock = process_orders(products_stock, sales_orders)
 
 # Function to restock items
def restock_items(products_stock, restock_list):
    for item in restock_list:
        product_id, restock_qty = item['product_id'], item['quantity']
        if product_id in products_stock:
            products_stock[product_id] += restock_qty
            print(f"Product {product_id} restocked with {restock_qty} units.")
        else:
            print(f"Error: Product {product_id} does not exist in stock.")
    return products_stock

# Sample restock data
restock_list = [
    {'product_id': 2, 'quantity': 10},
]

updated_stock = restock_items(updated_stock, restock_list)
