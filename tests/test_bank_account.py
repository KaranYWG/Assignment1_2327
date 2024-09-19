"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: {Karanpreet Singh}
Date: {September 16, 2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from ..bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Setup test account with initial values
        self.account = BankAccount(12345, 67890, 1000.00)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.00)

    def test_valid_deposit(self):
        self.account.deposit(500.00)
        self.assertEqual(self.account.balance, 1500.00)

    def test_invalid_deposit_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit("not_a_number")
        self.assertEqual(str(context.exception), "Deposit amount: not_a_number must be numeric.")

    def test_invalid_deposit_negative(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100.00)
        self.assertEqual(str(context.exception), "Deposit amount: -100.00 must be positive.")
    
    def test_valid_withdraw(self):
        self.account.withdraw(200.00)
        self.assertEqual(self.account.balance, 800.00)

    def test_invalid_withdraw_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw("not_a_number")
        self.assertEqual(str(context.exception), "Withdrawal amount: not_a_number must be numeric.")
    
    def test_invalid_withdraw_negative(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-50.00)
        self.assertEqual(str(context.exception), "Withdrawal amount: -50.00 must be positive.")

    def test_withdraw_exceeding_balance(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(1500.00)
        self.assertEqual(str(context.exception), "Withdrawal amount: 1500.00 must not exceed the account balance: 1000.00")

    def test_update_balance_with_valid_amount(self):
        self.account.update_balance(300.00)
        self.assertEqual(self.account.balance, 1300.00)

    def test_update_balance_with_invalid_amount(self):
        self.account.update_balance("not_a_number")
        self.assertEqual(self.account.balance, 1000.00)

if __name__ == '__main__':
    unittest.main()

