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
    if sort_order == "asc":
        sorted_list = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        print("Invalid sort order")
        sorted_list = products_list
    
    return sorted_list



def display_products(products_list):
    print("Product list：")
    for index, (product_name, price) in enumerate(products_list, start=1):
        print(f"{index}. {product_name} - {price}")


def display_categories():
    categories = ["IT Products", "Electronics", "Groceries"]
    print("Product Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    try:
        choice = int(input("Select a category by number: ")) - 1
        if 0 <= choice < len(categories):
            return choice
        else:
            print("Invalid choice. Please select a valid category.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None




def add_to_cart(cart, product, quantity):
    for item in cart:
        if item[0] == product[0]: 
            item[2] += quantity ##item[2] indicates the current quantity of the item
            break 
    else:
        cart.append((product[0], product[1], quantity)) ## New product information is added to the cart


def display_cart(cart):
    total_cost = 0 
    for product_name, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{product_name} - ${price} x {quantity} = ${cost}")

    print(f"Total cost: ${total_cost}")



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
    print("------------")   



def validate_name(name):
    parts = name.strip().split()
    if len(parts) != 2:
        return False
    first_name, last_name = parts
    if not first_name.isalpha() or not last_name.isalpha():
        return False
    return True
    
def validate_email(email):
    if "@" in email:
        return True
    return False


def main():
    cart = []
    while True:
        name = input("Enter your full name (first and last name): ").strip()
        if validate_name(name):
            break
        else:
            print("Invalid name. Make sure it contains only letters and both first and last name.")
    while True:
        email = input("Enter your email address: ").strip()
        if validate_email(email):
            break
        else:
            print("Invalid email. Ensure it contains '@' symbol.")
    while True:
        display_categories()
        categories = list(products.keys())
        category_choice = input("Enter the number of the category you want to explore: ").strip()
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
            category_index = int(category_choice) - 1
            selected_category = categories[category_index]
        else:
            print("Invalid choice. Please enter a valid category number.")
            continue

        while True:
            products_list = products[selected_category]
            display_products(products_list)
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            option = input("Enter your choice (1-4): ").strip()
            if option == '1':
                product_choice = input("Enter the number of the product you want to buy: ").strip()
                if product_choice.isdigit() and 1 <= int(product_choice) <= len(products_list):
                    product_index = int(product_choice) - 1
                    selected_product = products_list[product_index]
                    while True:
                        quantity_input = input(f"Enter the quantity of {selected_product[0]} you want to buy: ").strip()
                        if quantity_input.isdigit() and int(quantity_input) > 0:
                            quantity = int(quantity_input)
                            add_to_cart(cart, selected_product, quantity)
                            print(f"Added {quantity} {selected_product[0]} to your cart.")
                            break
                        else:
                            print("Invalid quantity. Please enter a positive integer.")
                else:
                    print("Invalid product number. Please try again.")
            elif option == '2':
                print("Sort products by price:")
                print("1. Ascending")
                print("2. Descending")
                sort_order = input("Enter your choice (1 or 2): ").strip()
                if sort_order in ['1', '2']:
                    products_list = display_sorted_products(products_list, sort_order)
                    display_products(products_list)
                else:
                    print("Invalid choice. Please try again.")
            elif option == '3':
                break
            elif option == '4':
                if cart:
                    total_cost = sum(price * quantity for _, price, quantity in cart)
                    display_cart(cart)
                    address = input("Enter your delivery address: ").strip()
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our platform. We hope you shop with us next time. Have a nice day!")
                return
            else:
                print("Invalid option. Please choose a number between 1 and 4.")

    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
