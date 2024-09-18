"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import sys
import os
import unittest
from ..client.client import Client

class TestClient(unittest.TestCase):
    def test_client_initialization(self):
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(client.client_number, 1010)
        self.assertEqual(client.first_name, "Susan")
        self.assertEqual(client.last_name, "Clark")
        self.assertEqual(client.email_address, "susanclark@pixell.com")

    def test_invalid_email(self):
        client = Client(1010, "Susan", "Clark", "invalidemail")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            Client("invalid_number", "Susan", "Clark", "susanclark@pixell.com")

    def test_empty_first_name(self):
        with self.assertRaises(ValueError):
            Client(1010, "", "Clark", "susanclark@pixell.com")

if __name__ == "__main__":
    unittest.main()
