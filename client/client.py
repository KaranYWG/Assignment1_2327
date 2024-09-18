"""
Description: Developing robust and flexible Bank Account and Client classes.
Author: Karanpreet Singh
"""
import sys
import os
from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate first_name (not blank after stripping)
        if not first_name.strip():
            raise ValueError("First name cannot be blank.")
        self.__first_name = first_name.strip()

        # Validate last_name (not blank after stripping)
        if not last_name.strip():
            raise ValueError("Last name cannot be blank.")
        self.__last_name = last_name.strip()

        # Validate email address using email-validator
        try:
            validated_email = validate_email(email_address)
            self.__email_address = validated_email.email
        except EmailNotValidError:
            self.__email_address = "karanpreetsingh2@rrc.ca"

    # Property methods (accessors)
    @property
    def client_number(self) -> int:
        return self.__client_number

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email_address(self) -> str:
        return self.__email_address

    # __str__ method for formatted output
    def __str__(self) -> str:
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}\n"


try:
    client = Client(396924, "Karanpreet", "Singh", "karanpreetsingh2@rrc.ca")
    print(client)
except ValueError as e:
    print(e)
