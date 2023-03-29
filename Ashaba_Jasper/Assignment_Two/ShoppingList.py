"""2. printing receipts after shopping
Create a small shop with some products and prices where a buyer can view the list of a vailable products and their prices.
when program runs, it should prompt buyer to create account using password and email and store this in an excel sheet.
Then ask user for login if he has registered account else register
The products shoulf be fetched from an excel sheet called products.
Buyer can choose what to buy.
Buyer can pay for what they have have bought
Then print a reciept for the buyer. Simple receipt example image This receipt should printed on terminal, dont bother about pdf printing for now
NB. This simulates the real world ecommerce situation, consider all possible human errors and catch them e.g buyer puts a price less that the total of items he has bought, buyer putting wrong. Use functions to break down your work into small codes. You can use modules and import them as well."""


import pandas as pd

# create a dictionary of products and their prices
products = {
    "Books"   :  49.95,
    "Computer":  579.99,
    "Monitor" :  124.89,
    "Pens"    :  2.96
 }

# create a function to get user input for login or registration
def get_user_info():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    return email, password

# create a function to register a new user and store their info in an excel sheet
def register_user():
    email, password = get_user_info()
    #Used pandas
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
    print("Product Name"+"   "+"Product Price")
    for product, price in products.items():
        print(f"{product}           ${price}")

# create a function to calculate the total price of the items purchased
#def calculate_total(items):
    #total = 0
    #for item in items:
        #total += products[item]
    #return total

def calculate_total(items):
    return sum([products[item] for item in items])

# create a function to print the receipt
def print_receipt(items):
    print("****************************************************")
    print("\tCoding Temple, Inc.")
    print("\t283 Franklin St. Boston, MA")
    print("====================================================")
    print("Product Name\tProduct Price")
    for item in items:
        print(f"{item}\t\t{products[item]:.2f}")
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
        choice = input("Do you have an account? (yes/no): ")
        if choice == "yes":
            login_user()
            break
        elif choice == "no":
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
