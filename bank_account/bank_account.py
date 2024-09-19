class BankAccount:
    def __init__(self, account_number, client_number, balance=0.0):
        # Validate account_number and client_number are integers
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        
        # Assign validated values to instance attributes
        self._account_number = account_number
        self._client_number = client_number
        
        # Validate and assign the balance
        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

    # Accessors using @property
    @property
    def account_number(self):
        return self._account_number

    @property
    def client_number(self):
        return self._client_number

    @property
    def balance(self):
        return round(self._balance, 2)
    
    # update_balance method
    def update_balance(self, amount):
        try:
            amount = float(amount)
            self._balance += amount
        except ValueError:
            # If amount cannot be converted to float, do nothing
            pass
    
    # deposit method
    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError(f"Deposit amount: ${amount:.2f} must be positive.")
            self.update_balance(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
    
    # __str__ method for string representation of the object
    def __str__(self):
        return f"Account Number: {self._account_number} Balance: ${self._balance:.2f}"
    
    # withdraw method
    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError(f"Withdrawal amount: ${amount:.2f} must be positive.")
            if amount > self._balance:
                raise ValueError(f"Withdrawal amount: ${amount:.2f} must not exceed the account balance: ${self._balance:.2f}")
            # Use update_balance with a negative amount for withdrawal
            self.update_balance(-amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")

if __name__ == '__main__':
    try:
        # Prompt user for input
        account_number = int(input("Enter account number: "))
        client_number = int(input("Enter client number: "))
        balance = float(input("Enter initial balance: "))

        # Create BankAccount instance
        account = BankAccount(account_number, client_number, balance)
        print(f"Created account: {account}")

        # Perform deposit
        deposit_amount = float(input("Enter deposit amount: "))
        account.deposit(deposit_amount)
        print(f"After deposit: {account}")

        # Perform withdrawal
        withdraw_amount = float(input("Enter withdrawal amount: "))
        account.withdraw(withdraw_amount)
        print(f"After withdrawal: {account}")

    except ValueError as e:
        print(f"Error: {e}")
