#!/usr/bin/env python
# coding: utf-8

# In[ ]:



'''*******************************************************************************************************************
    * Name:-    Tejas Vishal Mishra
    * College:- PES Modern College of Engineering
    * Branch:-  Information Technology
    * Mini Project:- Atm Software with Pin Authentication in python
 **********************************************************************************************************************'''

print("************** Welcome to Team 08 ATM *****************")

# Account holder details
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
pin = input("Enter a 4-digit pin: ")
while len(pin) != 4:  # Check if pin is 4 digits long
    print("Pin must be 4 digits long. Please try again.")
    pin = input("Enter a 4-digit pin: ")

balance = 0  # Initial balance is set to 0
print("Account created successfully.")

# Authentication menu
while True:
    print("Choose an option:")
    print("1. Authenticate")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        # Authentication
        authentication = False
        while not authentication:
            user_pin = input("Enter your 4-digit pin to authenticate: ")
            if user_pin == pin:
                print("Authentication successful\n")
                print("Hey",name)
                print("How may I help you?")
                authentication = True
            else:
                print("Incorrect pin. Please try again.")
        # Account menu
        while authentication:
            print("Choose an option:")
            print("1. Account info")
            print("2. Check balance")
            print("3. Withdraw money")
            print("4. Deposit money")
            print("5. Change pin")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                # Display account holder info
                print("Account holder name:", name)
                print("Account number:", account_number)
            elif choice == "2":
                # Display current balance
                print("Current balance:", balance)
            elif choice == "3":
                # Withdraw money
                amount = int(input("Enter the amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print("Withdrawal successful. Current balance:", balance)
            elif choice == "4":
                # Deposit money
                amount = int(input("Enter the amount to deposit: "))
                balance += amount
                print("Deposit successful. Current balance:", balance)
            elif choice == "5":
                # Change pin
                new_pin = input("Enter a new 4-digit pin: ")
                pin = new_pin
                print("Pin changed successfully.")
            elif choice == "6":
                # Quit
                print("Goodbye!....Thanks for using Team 08 ATM")
                print("****************************************")
                authentication = False
                break
            else:
                # Invalid choice
                print("Invalid choice. Please try again.")
    elif choice == "2":
        # Quit
        print("Goodbye!..Thanks for using Team 08 ATM")
        print("**************************************")
        break
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")


# In[ ]:




