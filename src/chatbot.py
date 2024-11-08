"""
Description: Chatbot application.  Allows user to perform balance 
inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: Kimi Sevilla
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

def get_account() -> int:

    try:
        account_number = int(input("Please enter your account number: "))
    except ValueError:
        raise ValueError("Account number must be a whole number.")

    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")

    return account_number

def get_balance(account_number):

    account = ACCOUNTS.get(account_number)
    if account:
        return account["balance"]
    return None

def deposit(account_number, amount):
    account = ACCOUNTS.get(account_number)
    if account and amount > 0:
        account["balance"] += amount
        return True
    return False

def handle_user_input(account_number, task, amount=0):
    if task not in VALID_TASKS:
        return "Invalid task. Please choose from: balance, deposit, exit."

    if task == "balance":
        balance = get_balance(account_number)
        if balance is not None:
            return f"Your balance is: ${balance:.2f}"
        return "Account not found."

    elif task == "deposit":
        success = deposit(account_number, amount)
        if success:
            return f"Deposited ${amount:.2f}. New balance is: ${get_balance(account_number):.2f}"
        return "Deposit failed. Please check the amount and account number."

    elif task == "exit":
        return "Thank you for using the service. Goodbye!"



## REQUIRES REVISION

def chatbot():
    """Simulates a simple chatbot interaction."""
    print("Welcome to the Bank Chatbot!")
    
    try:
        account_number = get_account()
    except ValueError as e:
        print(f"Error: {e}")
        return 

    while True:
        task = input("What would you like to do? (balance, deposit, exit): ").strip().lower()
        
        if task == "exit":
            print(handle_user_input(account_number, task))
            break
        
        if task == "deposit":
            try:
                amount = float(input("Enter the amount to deposit: "))
                print(handle_user_input(account_number, task, amount))
            except ValueError:
                print("Please enter a valid amount.")
        else:
            print(handle_user_input(account_number, task))
"""
def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:

            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:

                        valid_account = True
                    except ValueError as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except ValueError as e:
                            # Invalid amount.
                            print(e)
                ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                ## VARIABLES account AND amount DEFINED ABOVE AND 
                ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""
