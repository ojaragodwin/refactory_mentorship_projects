## 2. printing receipts after shopping

"""- Create a small shop with some products and prices where a buyer can view the list of a vailable products and their prices.
- when program runs, it should prompt buyer to create account using password and email and store this in an excel sheet.
- Then ask user for login if he has registered account else register
- The products shoulf be fetched from an excel sheet called products.
- Buyer can choose what to buy.
- Buyer can pay for what they have have bought
- Then print a reciept for the buyer.
Simple receipt example
![image](https://user-images.githubusercontent.com/38132692/223027176-8116fdb3-86eb-46d0-bf04-5d6b9c81e16a.png)
This receipt should printed on terminal, dont bother about pdf printing for now

NB. This simulates the real world ecommerce situation, consider all possible human errors and catch them e.g buyer puts a price less that the total of items he has bought, buyer putting wrong. Use functions to break down your work into small codes. You can use modules and import them as well."""

#To create the program, I followed these steps
#1.Create a list of available products and their prices.
#2.Prompt the buyer to create an account using a password and email, and store this information in an excel sheet.
#3.Ask the user to login or register if they haven't already.
#4.Fetch the list of available products and their prices from an excel sheet called "products".
#5.Allow the buyer to choose what they want to buy.
#6.Calculate the total cost of the items bought by the buyer.
#7.Prompt the buyer to pay for their purchases.
#8.If the payment is successful, print a receipt for the buyer.

import csv

# Step 1: Create a dictionary of available products and their prices
products = {
    "apple": 1000,
    "banana": 300,
    "orange": 1500,
    "grape": 5000,
    "watermelon": 10000,
}

# Step 2: Prompt the buyer to create an account using a password and email, and store this information in a CSV file.
def create_account():
    # Ask the user for their email and password
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Write the email and password to a CSV file
    with open("accounts.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([email, password])

# Step 3: Ask the user to login or register if they haven't already.
def login():
    # Ask the user for their email and password
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if the email and password match a row in the accounts CSV file
    with open("accounts.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == email and row[1] == password:
                print("Login successful!")
                return
        print("Email or password is incorrect. Please try again.")

    # If the email and password don't match any rows in the CSV file, ask the user to create a new account
    create_account()

# Step 4: Fetch the list of available products and their prices from a CSV file called "products".
def fetch_products():
    products = {}
    with open("products.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            products[row[0]] = float(row[1])
    return products

# Step 5: Allow the buyer to choose what they want to buy.
def choose_products(products):
    cart = {}
    while True:
        print("Available products:")
        for product, price in products.items():
            print(f"{product}: ${price:.2f}")
        choice = input("What would you like to buy? (or 'done' to finish): ")
        if choice == "done":
            break
        elif choice not in products:
            print("That product is not available. Please choose another.")
            continue
        else:
            if choice in cart:
                cart[choice] += 1
            else:
                cart[choice] = 1
            print(f"Added {choice} to your cart.")

    return cart

# Step 6: Calculate the total cost of the items bought by the buyer.
def calculate_total(cart, products):
    total = 0
    for product, quantity in cart.items():
        if product in products:
            total += products[product] * quantity
        else:
            print(f"Product {product} is not available.")
    return total

# Step 7: Prompt the buyer to pay for their purchases.
def pay(total):
    while True:
        payment = input(f"Your total is ${total:.2f}. Please enter your payment amount: ")
        try:
            payment = float(payment)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if payment < total:
            print("Insufficient payment. Please enter a higher amount.")
        else:
            change = payment - total
            print(f"Thank you for your purchase! Your change is ${change:.2f}.")
            break

# Step 8: Print a receipt for the buyer.
def print_receipt(cart, total):
    # Print out header for receipt
    print("\n\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("         RECEIPT")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    # Print out each item purchased and its cost
    for product, quantity in cart.items():
        print(f"{product} x {quantity}: ${cart[product] * products[product]:.2f}")
        
    # Print out total cost of all items purchased
    print(f"Total: ${total:.2f}")
    
    # Print out footer for receipt
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Step 9: Put it all together
def main():
    # Step 2: Prompt the user to create an account using their email and password
    create_account()

    # Step 3: Ask the user to log in or register if they haven't already
    login()

    # Step 4: Fetch the list of products and their prices from an Excel sheet
    products = fetch_products()

    # Step 5: Allow the user to choose which products they want to buy
    cart = choose_products(products)

    # Step 6: Calculate the total cost of all items in the user's cart
    total = calculate_total(cart, products)

    # Step 7: Prompt the user to pay for their purchases
    pay(total)

    # Step 8: Print out a receipt for the user showing the items purchased and the total cost
    print_receipt(cart, total)

# This line of code ensures that the main() function is only called when this script is run directly, not when it is imported by another script
if __name__ == "__main__":
    main()
