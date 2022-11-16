# Name: Jay Williams
# Program Purpose: this rogram finds the cost of Pizza
#   Price for Small: $9.99
#   Price for Medium: $12.99
#   Price for Large: $14.99
#   Price for X-Large: $17.99
#   Sales tax rate: 5.5%

import datetime

############### define global variables ##############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_SMALL = 9.99
PR_MEDIUM = 12.99
PR_LARGE = 14.99
PR_ELARGE = 17.99
pizza_price = 0

# define global variables
size_pizza = 0
num_pizza = 0
subtotal = 0
sales_tax = 0
total = 0

############    define program functions    ##############
def main():
    order_again = True
    while order_again:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Do you want to order again? (Y/N) ")
        if yesno == "N" or yesno == 'n':
            order_again = False
            print("Thank you for ordering from Palermo Pizza! Please come again")
            return()

def get_user_data():
    global size_pizza, num_pizza
    size_pizza = input("Size of pizza \nS for Small \nM for Medium \nL for Large \nE for Extra Large\nEnter size:  ")
    num_pizza = int(input("Number of pizzas: "))

def perform_calculations():
    global subtotal, sales_tax, total, pizza_price
    if size_pizza.upper()== "S":
        pizza_price =  PR_SMALL
    if size_pizza.upper()== "M":
        pizza_price =  PR_MEDIUM
    if size_pizza.upper()== "L":
        pizza_price =  PR_LARGE
    if size_pizza.upper()== "E":
        pizza_price =  PR_ELARGE          
    subtotal = num_pizza * pizza_price
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-------------------------')
    print('**** Palermo Pizza ****')
    print('Best Pizza in Virginia')
    print('-------------------------')
    print('Subtotal     $' + format(subtotal, '8,.2f'))
    print('Sales Tax    $' + format(sales_tax, '8,.2f'))
    print('Total        $' + format(total,'8,.2f' ))
    print('------------------------')
    print(str(datetime.datetime.now()))
    print("Thank  you for ordering from Palermo Pizza!")

main()
