import pandas as pd
from getpass import getpass
import re

def create_account():
    # Get user email and password
    email = input("Enter your email: ")
    password = getpass("Enter your password: ")

    # Check if email is valid
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email = input("Invalid email, enter your email: ")

    # Store user data in a DataFrame
    user_df = pd.DataFrame({
        "email": [email],
        "password": [password],
    })

    # Append user data to the accounts file
    user_df.to_csv("accounts.csv", index=False, mode="a", header=not pd.read_csv("accounts.csv").empty)
    print("Account created successfully.")

def login():
    # Get user email and password
    email = input("Enter your email: ")
    password = getpass("Enter your password: ")

    # Load accounts file
    accounts_df = pd.read_csv("accounts.csv")

    # Check if user exists and password is correct
    if ((accounts_df["email"] == email) & (accounts_df["password"] == password)).any():
        print("Login successful.")
    else:
        print("Invalid email or password.")
        return False

    return True

def fetch_products():
    # Load products file
    products_df = pd.read_csv("products.csv")

    # Display list of available products and prices
    print("Available products:")
    print(products_df.to_string(index=False))

    return products_df

def buy_products(products_df):
    # Initialize variables
    total_price = 0
    selected_products = []

    # Ask user to select products to buy
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == "done":
            break

        # Check if product exists
        if (products_df["name"] == product_name).any():
            # Get product price and add to total
            product_price = products_df.loc[products_df["name"] == product_name, "price"].values[0]
            total_price += product_price

            # Add selected product to list
            selected_products.append({
                "name": product_name,
                "price": product_price,
            })

            print(f"{product_name} added to cart.")
        else:
            print("Invalid product name.")

    # Ask user to pay for selected products
    while True:
        payment_amount = float(input(f"Total price is {total_price}. Enter amount to pay: "))
        if payment_amount < total_price:
            print("Payment amount is less than total price.")
        else:
            break

    return selected_products, total_price, payment_amount

def print_receipt(selected_products, total_price, payment_amount):
    # Calculate change
    change = payment_amount - total_price

    # Print receipt
    print("Receipt:")
    print("========")
    for product in selected_products:
        print(f"{product['name']}\t{product['price']}")
    print(f"\nTotal\t{total_price}")
    print(f"Paid\t{payment_amount}")
    print(f"Change\t{change}")

def main():
    # Check if accounts file exists, create it if not
    try:
        pd.read_csv("accounts.csv")
    except FileNotFoundError:
        pd.DataFrame(columns=["email", "password"]).to_csv("accounts.csv", index=False)

    # Check if user is logged in, prompt for login or account creation if not
    if not login():
        create_account()
        login()

    #
