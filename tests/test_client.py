"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: {Karanpreet Singh}
Date: {September 16, 2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import os
import sys
import unittest
from ..client.client import Client  

class TestClient(unittest.TestCase):
    
    def test_client_initialization(self):
        client = Client(396924, "Karanpreet", "Singh", "karanpreetsingh2@rrc.ca")
        self.assertEqual(client.client_number, 396924)
        self.assertEqual(client.first_name, "Karanpreet")
        self.assertEqual(client.last_name, "Singh")
        self.assertEqual(client.email_address, "karanpreetsingh2@rrc.ca")

    def test_invalid_email(self):
        client = Client(396924, "Karanpreet", "Singh", "invalidemail")
        self.assertEqual(client.email_address, "email@pixell-river.com")  

    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            Client("invalid_number", "Karanpreet", "Singh", "karanpreetsingh2@rrc.ca")

    def test_empty_first_name(self):
        with self.assertRaises(ValueError):
            Client(396924, "", "Singh", "karanpreetsingh2@rrc.ca")

if __name__ == "__main__":
    unittest.main()

