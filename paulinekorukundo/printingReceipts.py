import hashlib
import pandas as pd
import xlrd
from xlwt import Workbook


'''
printing receipts after shopping
    Create a small shop with some products and prices where a buyer can 
    view the list of available products and their prices.
    when program runs, it should prompt buyer to create account using 
    password and email and store this in an excel sheet.
    Then ask user for login if he has registered account else register
    The products shoul be fetched from an excel sheet called products.
    Buyer can choose what to buy.
    Buyer can pay for what they have have bought
    Then print a reciept for the buyer. Simple receipt example image 
This receipt should printed on terminal, dont bother about pdf printing for now

NB. This simulates the real world ecommerce situation, consider all 
possible human errors and catch them e.g buyer puts a price less that 
the total of items he has bought, buyer putting wrong. Use functions to 
break down your work into small codes. 
You can use modules and import them as well.
'''
'''
Available products
milk 1600, sugar 2500, salt 1000, soda 2000, water 2500, rice  5600
'''


'''
defining the registration function
'''


def register():
    print('')
    while True:
        email = input('Enter your email address: ')
        passwrd = input('Enter your password: ')
        confPasswd = input('Confirm your password: ')
        if confPasswd == passwrd:
            enc = confPasswd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            dets = Workbook()
            sheet1 = dets.add_sheet('Credentials')
            sheet1.write(1, 0, 'email')
            sheet1.write(1, 1, 'pass')
            sheet1.write(2, 0, email)
            sheet1.write(2, 1, hash1)
            dets.save('LoginDetails.xls')
            print('Successfully registered')
            break
        else:
            print('Passwords do not match! \n')


'''
defining the login function after an account is created
'''


def login():    
    book = xlrd.open_workbook('LoginDetails.xls')
    worksheet = book.sheet_by_index(0)
    storedEmail = worksheet.cell_value(rowx = 2, colx = 0)
    storedPass = worksheet.cell_value(2, 1)
    while True:  
        email = input('Enter your email address: ')
        passwrd = input('Enter your password: ')
        auth = passwrd.encode()
        auth_hashCode = hashlib.md5(auth).hexdigest()
        if (storedEmail == email and auth_hashCode == storedPass):
            print('Successfully logged in')
            break
        else:
            print('Password and Email address combination not found')


'''
validate if product name is a string
'''


def checkInput(userInput):
    while True:
        # strip the input of quotations and check if the input is a digit
        if int(userInput.strip().isdigit()):
            print('Entered a number! ')
            userInput = input("Enter valid product name: ")
        # if stripped user input is not a digit, then that its a string
        else:
            return userInput
       

'''
create catalogue of products and save to an excel database
'''


def productsLst():
    names = ['milk', 'sugar', 'salt', 'soda', 'water', 'rice']
    prices = [1600, 2500, 1000, 2000, 2500,  5600]
    pdtLst = {
        'milk': 1600, 
        'sugar': 2500,
        'salt': 1000,
        'soda': 2000,
        'water': 2500,
        'rice': 5600}
    pdts = Workbook()
    sheet = pdts.add_sheet('Products')
    sheet.write(0, 0, 'Product Name')
    sheet.write(0, 1, 'Product Price')
    
    row = 1
    for item in names:
        sheet.write(row, 0, item)
        row += 1
    row = 1
    for prc in prices:
        sheet.write(row, 1, prc)
        row += 1
    pdts.save('Products.xls')
    
    return pdtLst



#productsLst()


def makeOrder():
    orderedList = []
    total = 0
    row = 1
    prodDb = productsLst()
    #products = xlrd.open_workbook('Products.xls')
    availPdts = pd.read_excel('Products.xls')
    print('')
    print(availPdts)


    # creat an excel file to save the ordered items and their cost
    ordered = Workbook()
    sheet1 = ordered.add_sheet('Cart')
    sheet1.write(0, 0, 'Product Name')
    sheet1.write(0, 1, 'Product Price')
    sheet1.write(0, 2, 'Cost')


    # Check that product to be ordered and price are valid
    # enter these into the Cart.xls excel
    # compute the total of the order
    for item in prodDb:
        item = input('Enter q to checkout or item to order: ')
        if (item == 'q'):
            break
        elif (item not in prodDb):
            print('Select a valid product')
            continue
        productName = checkInput(item)
        sheet1.write(row, 0, productName)
        qtty = input(f'Enter quantity for {item} to order: ')
        try:
            quantity = int(qtty)
            sheet1.write(row, 1, qtty)
        except ValueError:
            print('Quantity entered is not valid')
            continue
        cost = quantity * prodDb[productName]
        sheet1.write(row, 2, cost)
        row += 1
        total += cost

    ordered.save('Cart.xls')

    # print the receipt to the terminal
    print('')
    print('===================================================')
    print('                  PK Minimart')
    print('              255 Kyengera, Uganda')
    print('===================================================')
    # Using pandas to read the Cart excel file and print to terminal
    print(pd.read_excel('Cart.xls'))
    print('===================================================')
    # printing the total bill
    print(f'                               Total')
    print(f'                               {total}')
    print('===================================================')
    print('       Thanks for shopping with us today!')
    print('===================================================')
    print('')


register()
login()
makeOrder()
