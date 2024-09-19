""""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""
from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes.
    """ 
    # 1. Code a statement which creates a valid instance of the Client class.
    try:
        client = Client(client_number=396924, name="Karanpreet Singh", address="123 Winnipeg")
    except ValueError as e:
        print(f"Error creating Client: {e}")

    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a statement  
    try:
        bank_account = BankAccount(account_number=12345, client_number=client.client_number, balance=1000.00)
        print(f"BankAccount created: {bank_account}")
    except ValueError as e:
        print(f"Error creating BankAccount: {e}")

    # 4. Code a statement which creates an instance of the BankAccount class.
    try:
        invalid_account = BankAccount(account_number=54321, client_number=client.client_number, balance="invalid_balance")
    except ValueError as e:
        print(f"Error creating BankAccount with invalid balance: {e}")

    # 5. Code a statement which prints the Client instance created in step 1. 
    print(f"Client: {client}")
    print(f"BankAccount: {bank_account}")

    # 6. Attempt to deposit a non-numeric value into the BankAccount created in step 3. 
    try:
        bank_account.deposit("non_numeric_deposit")
    except ValueError as e:
        print(f"Error depositing non-numeric value: {e}")

    # 7. Attempt to deposit a negative value into the BankAccount created in step 3. 
    try:
        bank_account.deposit(-50.00)
    except ValueError as e:
        print(f"Error depositing negative value: {e}")

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount created in step 3. 
    try:
        bank_account.withdraw(200.00)
        print(f"After valid withdrawal: {bank_account}")
    except ValueError as e:
        print(f"Error withdrawing valid amount: {e}")

    # 9. Attempt to withdraw a non-numeric value from the BankAccount created in step 3. 
    try:
        bank_account.withdraw("non_numeric_withdrawal")
    except ValueError as e:
        print(f"Error withdrawing non-numeric value: {e}")

    # 10. Attempt to withdraw a negative value from the BankAccount created in step 3. 
    try:
        bank_account.withdraw(-30.00)
    except ValueError as e:
        print(f"Error withdrawing negative value: {e}")

    # 11. Attempt to withdraw a value from the BankAccount created in step 3 which 
    try:
        bank_account.withdraw(10000.00)
    except ValueError as e:
        print(f"Error withdrawing amount exceeding balance: {e}")

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print(f"Final BankAccount state: {bank_account}")

if __name__ == "__main__":
    main()
