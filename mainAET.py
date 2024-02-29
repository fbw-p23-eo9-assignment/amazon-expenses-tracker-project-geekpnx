import os
import re
import time
import sys

MAX_ATTEMPTS = 3
DELAY_SECONDS = 5

#--------------- SPINNING BAR ---------------------

def spinning_bar():
    chars = "/—\\|"
    for _ in range(20):
        for char in chars:
            sys.stdout.write('\r' + f'Loading {char} ')
            sys.stdout.flush()
            time.sleep(0.1)
    print("\nLoading complete!")

#------------------- LABEL ----------------------------------

def label(text,pipe_val, space_val):
    text = text.capitalize()
    pipe = '|'*pipe_val
    space = ' '*space_val  
    print(f'{pipe}{space}{text}{space}{pipe}')

#-------------------- PADDING -----------------

def padding():
    print('\n'*0)

#------------------- LINE DASHES --------------------------

def lineFunc():
    lines= '-'*50
    return print(lines)

#-------------------- BANNER -----------------------------

def print_box_with_text(width=None, text=None):
    width = 49
    space = ' '*47
    text = "amazon expenses tracker".upper()

    print("╔" + "═" * (width - 2) + "╗")

    text_padding = " " * ((width - len(text)) // 2 - 1)
    print(f"║{space}║\n║{text_padding}{text}{text_padding}║\n║{space}║")

    print("╚" + "═" * (width - 2) + "╝")

#-------------------------- REGISTRATION -------------------------

def register_user(users_dict):
    os.system('clear')
    print_box_with_text(width=None, text=None)
    padding()
    label('registration',3, 1)
    lineFunc()
    padding()
    while True:
        username = input("Create username: ")

        if username in users_dict:
            print("\nUsername already exists. Please choose a different username.")
        elif not re.match(r'^[a-zA-Z0-9_]+$', username):
            print("\nInvalid username. Please follow the criteria.")
        else:
            break

    while True:
        password = input("Create password: ")

        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{6,20}$', password):
            print("\nInvalid password. Please follow the criteria.")
        else:
            break

    while True:
        phone_number = input("Enter your mobile number (with the code +49): ")

        if not re.match(r'^\+49\d{10}$', phone_number):
            print("\nInvalid German phone number format. Please enter a valid number.")
        else:
            break

    users_dict[username] = {'password': password, 'phone_number': phone_number}
    print(f"\nRegistration successful! {username}, you can select option 2. to login.")
    return True

#--------------------------------------- LOGIN -----------------------------------------

def login(users_dict):
    os.system('clear')
    print_box_with_text(width=None, text=None)
    padding()
    label('login',3, 1)
    lineFunc()
    padding()
    username = input("Enter username: ")

    if username in users_dict:
        attempts = 0
        while attempts < MAX_ATTEMPTS:
            password = input("Enter password: ")
            if users_dict[username]['password'] == password:
                print(f"\nLogin successful! Phone number: {users_dict[username]['phone_number']}")
                return username #added username
            else:
                attempts += 1
                print(f"\nIncorrect password. Attempts remaining: {MAX_ATTEMPTS - attempts}")

        print(f"\nYou have used all attempts. Waiting for {DELAY_SECONDS} seconds.")
        time.sleep(DELAY_SECONDS)
        return None #login(users_dict) edited
    else:
        print("\nUsername not found. Please register first.")
        return  None #### edited

if __name__ == "__main__":
    user_credentials = {}

#------------------------------------ MAIN 2 -------------------------------
import os
import re
import time


def print_menu():
    print("\n•••\n1. Enter a purchase\n2. Generate a report\n3. Quit")


def calculate_delivery_charges(purchases):
    total_weight = sum(purchase['weight'] * purchase['quantity'] for purchase in purchases)
    return total_weight


def calculate_item_costs(purchases):
    return sum(purchase['total_cost'] for purchase in purchases)


def find_expensive_orders(purchases):
    if not purchases:
        return None, None
    
    most_expensive = max(purchases, key=lambda x: x['total_cost'])
    least_expensive = min(purchases, key=lambda x: x['total_cost'])
    
    return most_expensive, least_expensive


def calculate_average_cost(purchases):
    if not purchases:
        return 0
    
    total_cost = sum(purchase['total_cost'] for purchase in purchases)
    return total_cost / len(purchases)


def check_spending_limit(purchases, limit=500):
    total_cost = sum(purchase['total_cost'] for purchase in purchases)
    return total_cost > limit


def display_final_message(username):
    print(f"\nThank you, {username}, for using the Amazon Expense Tracker!")


def enter_purchase(purchases):
    os.system('clear')
    print_box_with_text(width=None, text=None)
    padding()
    label(f"You may enter your purchase here",3, 1)
    lineFunc()
    padding()
    date = input("Enter the date of the purchase (MM/DD/YYYY or MM-DD-YYYY): ")
    item = input("Enter the item purchased (at least 3 characters): ")
    
    while True:
        try:
            total_cost = float(input("Enter the total cost of the item (including delivery charges): "))
            weight = float(input("Enter the weight of the item (in kg): "))
            quantity = int(input("Enter the quantity purchased (should be an integer from 1 and above): "))
            
            if quantity <= 0:
                raise ValueError("\nQuantity should be an integer from 1 and above.")
            
            break
        except ValueError as e:
            print(f"\nInvalid input: {e}. Please enter the correct value.")

    purchases.append({
        'date': date,
        'item': item,
        'total_cost': total_cost,
        'weight': weight,
        'quantity': quantity
    })
    
    print("\nPurchase entered successfully!")


def generate_report(purchases):
    os.system('clear')
    print_box_with_text(width=None, text=None)
    padding()
    label(f'We will generate the report',3, 1)
    lineFunc()   
    if not purchases:
        print("\nNo purchases entered. Please enter at least one purchase.")
        return

    delivery_charges = calculate_delivery_charges(purchases)
    item_costs = calculate_item_costs(purchases)
    most_expensive, least_expensive = find_expensive_orders(purchases)
    average_cost = calculate_average_cost(purchases)
    spending_limit_exceeded = check_spending_limit(purchases)
    spinning_bar()
    print("\nGenerating report... (please wait)")
    time.sleep(2)

    print("\n*** Amazon Expense Tracker Report ***")
    print(f"\nTotal charges for delivery: {delivery_charges:.2f} EURO")
    print(f"Costs of items (excluding delivery charges): {item_costs:.2f} EURO")
    
    if most_expensive and least_expensive:
        print(f"Most expensive order: {most_expensive['item']} ({most_expensive['total_cost']:.2f} EURO)")
        print(f"Least expensive order: {least_expensive['item']} ({least_expensive['total_cost']:.2f} EURO)")
    
    print(f"Average cost per order: {average_cost:.2f} EURO")
    
    if spending_limit_exceeded:
        print("\nWarning: You have exceeded the spending limit of 500 EURO.")

#--------------------------------------  MAIN ------------------------------
    
def main():
    os.system('clear') 
    print_box_with_text(width=None, text=None)
    padding()
    label('welcome',3, 1)
    lineFunc()
    while True:
        print("\n•••\n1. Registration\n2. Login\n3. Exit")
        choice = input("\nSelect an option (1/2/3): ")

        if choice == '1':
            register_user(user_credentials)
        elif choice == '2':
            username = login(user_credentials) # added username before login function
            if username: # added this if statement
                main2(username) # added this too

        elif choice == '3':
            print("\nExiting program.")
            exit()
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

#--------------------------------- MAIN2 ---------------

def main2(username):
    os.system('clear')
    purchases = []
    print_box_with_text(width=None, text=None)
    padding()
    label(f'{username}, you ready to enter your purchese!',3, 1)
    lineFunc()
    while True:
        print_menu()
        choice = input("\nPick a choice (1/2/3): ")

        if choice == '1':
            enter_purchase(purchases)
        elif choice == '2':
            generate_report(purchases)
        elif choice == '3':
            display_final_message(username)
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()