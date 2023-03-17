import pandas as pd
import getpass
import random

# Create an Excel sheet called “products” with the list of available products and their prices
Products_df = pd.DataFrame({
    'Product': [ 'Dell', 'lenovo' ,'macbook'],
    'Price': [100, 200, 300]
})
Products_df.to_excel('products.xlsx', index=False)

# Create an Excel sheet called “accounts” to store user information
Accounts_df = pd.DataFrame(columns=['Email', 'Password', 'Wallet'])
Accounts_df.to_excel('accounts.xlsx', index=False)

# Function to validate user input
def validate_input(input_str, choices):
    while True:
        user_input = input(input_str)
        if user_input in choices:
            return user_input
        else:
            print('Invalid input. Please try again.')

# Function to generate a random transaction ID
def generate_transaction_id():
    return random.randint(100000, 999999)

# Function to display the products
def display_products():
    products_df = pd.read_excel('products.xlsx')
    print(products_df.to_string(index=False))

# Function to calculate the total bill
def calculate_total_bill(cart):
    #Products_df = pd.read_excel('products.xlsx')
    total_bill = 0
    for item in cart:
        total_bill += Products_df.loc[item]['Price']
    return total_bill

# Function to print the receipt
def checkout(cart, wallet_balance):
    total_bill = calculate_total_bill(cart)
    print('------ RECEIPT ------')
    print('Transaction ID:', generate_transaction_id())
    print('Items Purchased: ')
    products_df = pd.read_excel('products.xlsx')
    for item in cart:
        print(Products_df.loc[item]['Product'], '-', Products_df.loc[item]['Price'])
    print('Total Bill:', total_bill)
    if total_bill > wallet_balance:
        print("Your wallet balance is not enough to pay for your cart. Would you like to remove some items from your cart or top up your wallet balance?")
        response = input("Enter '1' to remove items, '2' to top up your wallet balance, or '3' to cancel: ")
        if response == '1':
            # Remove items from cart
            cart = remove_items_from_cart(cart)
            checkout(cart, wallet_balance)
        elif response == '2':
            wallet_balance = top_up_wallet(wallet_balance)
            checkout(cart, wallet_balance)
        else:
            print("Checkout cancelled.")
    else:
        print("Your wallet balance is enough to pay for your cart.")
        wallet_balance -= total_bill
        update_wallet_balance(wallet_balance)
    print('---------------------')

# Function to remove items from the cart
def remove_items_from_cart(cart):
    while True:
        item = input('Enter the index of the item you want to remove: ')
        if item.isdigit() and int(item) <= len(cart):
            del cart[int(item)-1]
            break
        else:
            print('Invalid input. Please try again.')
    return cart

# Function to top up the wallet balance
def top_up_wallet(wallet_balance):
    while True:
        amount = input('Enter the amount you want to top up: ')
        if amount.isdigit():
            wallet_balance += int(amount)
            break
        else:
            print('Invalid input. Please try again.')
    update_wallet_balance(wallet_balance)
    return wallet_balance

# Function to update the wallet balance
def update_wallet_balance(wallet_balance):
    accounts_df = pd.read_excel('accounts.xlsx')
    email = input('Enter your email address: ')
    accounts_df.loc[accounts_df['Email'] == email, 'Wallet'] = wallet_balance

def main():
    # Load the accounts dataframe from the accounts.xlsx file
    accounts_df = pd.read_excel('accounts.xlsx')
    
    # Prompt the user to log in or sign up
    print('Welcome to the online store!')
    while True:
        action = validate_input("Enter '1' to log in, '2' to sign up, or '3' to quit: ", ['1', '2', '3'])
        if action == '1':
            # Log in
            email = input('Enter your email address: ')
            password = getpass.getpass('Enter your password: ')
            if accounts_df[(accounts_df['Email'] == email) & (accounts_df['Password'] == password)].empty:
                print('Incorrect email or password. Please try again.')
            else:
                print('Logged in successfully!')
                wallet_balance = accounts_df.loc[accounts_df['Email'] == email, 'Wallet'].item()
                break
        elif action == '2':
            # Sign up
            email = input('Enter your email address: ')
            if not accounts_df[accounts_df['Email'] == email].empty:
                print('An account with this email already exists. Please log in instead.')
            else:
                password = getpass.getpass('Enter a password: ')
                accounts_df = accounts_df.append({'Email': email, 'Password': password, 'Wallet': 0}, ignore_index=True)
                accounts_df.to_excel('accounts.xlsx', index=False)
                print('Account created successfully!')
                wallet_balance = 0
                break
        else:
            # Quit
            print('Goodbye!')
            return
    
    # Show the list of products
    display_products()
    
    # Initialize an empty cart
    cart = []
    
    # Main shopping loop
    while True:
        action = validate_input("Enter '1' to add an item to your cart, '2' to view your cart, '3' to checkout, or '4' to quit: ", ['1', '2', '3', '4'])
        if action == '1':
            # Add an item to the cart
            while True:
                item = input('Enter the index of the item you want to add: ')
                if item.isdigit() and int(item) <= len(Products_df):
                    cart.append(int(item)-1)
                    print('Item added to cart!')
                    break
                else:
                    print('Invalid input. Please try again.')
        elif action == '2':
            # View the cart
            if not cart:
                print('Your cart is empty.')
            else:
                print('Your cart:')
                products_df = pd.read_excel('products.xlsx')
                for i, item in enumerate(cart):
                    print(f"{i+1}. {Products_df.loc[item]['Product']} - {Products_df.loc[item]['Price']}")
        elif action == '3':
            # Checkout
            if not cart:
                print('Your cart is empty.')
            else:
                checkout(cart, wallet_balance)
                cart = []
                wallet_balance = accounts_df.loc[accounts_df['Email'] == email, 'Wallet'].item()
        else:
            # Quit
            print('Goodbye!')
            return
if __name__ == '__main__':
    main()