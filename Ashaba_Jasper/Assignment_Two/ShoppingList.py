import pandas as pd

# create a dictionary of products and their prices
products = {
    "Books"   :  49.95,
    "Computer":  579.99,
    "Monitor" :  124.89
 }

# create a function to get user input for login or registration
def get_user_info():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    return email, password

# create a function to register a new user and store their info in an excel sheet
def register_user():
    email, password = get_user_info()
    df = pd.DataFrame({"email": [email], "password": [password]})
    df.to_excel("users.xlsx", index=False)
    print("You have successfully registered.")

# create a function to log in an existing user
def login_user():
    email, password = get_user_info()
    df = pd.read_excel("users.xlsx")
    if (df["email"] == email).any() and (df["password"] == password).any():
        print("You have successfully logged in.")
    else:
        print("Incorrect email or password. Please try again.")

# create a function to display the list of available products and their prices
def display_products():
    print("Here are the available products and their prices:")
    print("Product Name\tProduct Price")
    for product, price in products.items():
        print(f"{product}\t ${price:.2f}")

# create a function to calculate the total price of the items purchased
def calculate_total(items):
    total = 0
    for item in items:
        total += products[item]
    return total

# create a function to print the receipt
def print_receipt(items):
    print("****************************************************")
    print("\tCoding Temple, Inc.")
    print("\t283 Franklin St. Boston, MA")
    print("====================================================")
    print("Product Name\tProduct Price")
    for item in items:
        print(f"{item}\t${products[item]:.2f}")
    print("====================================================")
    total = calculate_total(items)
    print(f"\t\t\tTotal\n\t\t\t${total:.2f}")
    print("====================================================")
    print("\n\tThanks for shopping with us today!\n")
    print("****************************************************")

# create a function to handle the shopping process
def shop():
    # ask the user to log in or register
    while True:
        choice = input("Do you have an account? (y/n): ")
        if choice == "y":
            login_user()
            break
        elif choice == "n":
            register_user()
            break
        else:
            print("Invalid choice. Please try again.")

    # display the list of available products
    display_products()

    # ask the user to choose what to buy
    items = []
    while True:
        item = input("Enter the name of the product you want to buy (or enter 'done' to finish): ")
        if item == "done":
            break
        elif item in products:
            items.append(item)
            print(f"{item} has been added to your cart.")
        else:
            print("Invalid product. Please try again.")

    # calculate the total price and print the receipt
    print_receipt(items)

# call the shop function to start the program
shop()
