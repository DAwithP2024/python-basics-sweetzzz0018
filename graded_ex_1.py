# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    def sort_key(product):
        return product[1]
    if sort_order == 1:
        sorted_products = sorted(products_list, key=sort_key)
    elif sort_order == 2:
        sorted_products = sorted(products_list, key=sort_key, reverse=True)
    else:
         print("Invalid sorting option. Use 1 to sort in ascending order or 2 to sort in descending order.")
         return products_list
    
    return sorted_products


def display_products(products_list):
    print("Product list：")
    for index, (product_name, price) in enumerate(products_list, start=1):
        print(f"{index}. {product_name} ， {price}")


def display_categories():
    categories = list(products.keys())
    print("Product Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")


def add_to_cart(cart, product, quantity):
    for item in cart:
        if item[0] == product[0]: 
            item[2] += quantity  
            return
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    print("Shopping Cart:")
    
    total_cost = 0 
    for index, (product_name, price, quantity) in enumerate(cart, start=1):
        cost = price * quantity
        total_cost += cost
        print(f"{index}. {product_name} - {quantity} * {price} each = {cost}")
    
    print(f"Total cost: {total_cost}")



def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Shopping List:")
    
    for index, (product_name, price, quantity) in enumerate(cart, start=1):
        cost = price * quantity
        print(f"{index}. {product_name} - {quantity} * {price} each = {cost}")
    
    print(f"\nTotal Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("\nYour items will be delivered in 3 days. ")
    print("\nPayment will be accepted after successful delivery.")
    print("--- End ---")



def validate_name(name):
    parts = name.strip().split()
    
    if len(parts) != 2:
        return False
    
    first_name, last_name = parts
    
    if first_name.isalpha() and last_name.isalpha():
        return True
    else:
        return False
    
def validate_email(email):
    if "@" in email:
        return True
    return False


def main():
    pass
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
