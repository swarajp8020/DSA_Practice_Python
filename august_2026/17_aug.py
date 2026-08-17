"""
Day 2: Python Basics
Date: 11 August 2026

Topic:
Dictionaries, types, string concatenation, f-strings,
and handling missing dictionary keys.
"""


# ---------------------------------------------------------
# 1. Dictionary
# ---------------------------------------------------------

transaction = {
    "transaction_id": "TXN1001",
    "customer_id": "CUST123",
    "amount": 4500.00,
    "transaction_type": "DEBIT"
}

# A dictionary stores data as key-value pairs.
#
# Mental model:
#
# transaction
#     |
#     v
# Dictionary
#     |
#     +-- "transaction_id"   -> "TXN1001"
#     +-- "customer_id"      -> "CUST123"
#     +-- "amount"           -> 4500.0
#     +-- "transaction_type" -> "DEBIT"


# ---------------------------------------------------------
# 2. Accessing a dictionary value
# ---------------------------------------------------------

amount = transaction["amount"]

print(amount)

# transaction["amount"] means:
# Find the key "amount" inside the transaction dictionary
# and return its associated value.


# ---------------------------------------------------------
# 3. Missing dictionary key
# ---------------------------------------------------------

# If we try to access a key that does not exist:
#
# transaction["balance"]
#
# Python raises:
#
# KeyError: 'balance'
#
# Important:
#
# Missing key != None
#
# These are different situations.


# ---------------------------------------------------------
# 4. None vs missing key
# ---------------------------------------------------------

transaction_with_none = {
    "transaction_id": "TXN1002",
    "amount": None
}

print(transaction_with_none["amount"])

# Output:
# None
#
# Here the key EXISTS.
# Its value happens to be None.


empty_transaction = {}

# This would raise:
#
# empty_transaction["amount"]
#
# KeyError: 'amount'
#
# Here the key DOES NOT EXIST.


# ---------------------------------------------------------
# 5. String concatenation
# ---------------------------------------------------------

customer_name = "Swaraj"

message = "Hello " + customer_name

print(message)

# Output:
# Hello Swaraj
#
# IMPORTANT:
# + CAN concatenate strings in Python.
#
# The problem occurs when we try to combine incompatible types.


# ---------------------------------------------------------
# 6. String + number
# ---------------------------------------------------------

amount = 4500.00

# This does NOT work:
#
# message = "Amount: " + amount
#
# Why?
#
# "Amount: " -> str
# amount     -> float
#
# Python does not automatically combine:
#
# str + float
#
# This produces:
#
# TypeError


# ---------------------------------------------------------
# 7. f-strings
# ---------------------------------------------------------

transaction_id = "TXN1001"
amount = 4500.00

message = f"Transaction {transaction_id} has amount ₹{amount:.2f}"

print(message)

# Output:
# Transaction TXN1001 has amount ₹4500.00
#
# f-strings allow us to put expressions inside {}.
#
# {transaction_id}
#     |
#     v
# Python evaluates the variable
#
# {amount:.2f}
#     |
#     v
# Format amount as a floating-point number
# with exactly 2 decimal places.


# ---------------------------------------------------------
# 8. Production thinking
# ---------------------------------------------------------

# Python knows that this is a valid number:

negative_amount = -5000

print(negative_amount)

# Python is happy with this.
#
# But that does NOT mean:
#
# -5000 is a valid banking transaction.
#
# Programming language validity
#           !=
# Business validity
#
# Business rules must be implemented by our application.


# ---------------------------------------------------------
# 9. Key production lesson
# ---------------------------------------------------------

# When working with external data such as:
#
# API requests
# Database records
# Kafka messages
# CSV files
# JSON
# ML features
#
# NEVER assume that the data is always perfect.
#
# Ask:
#
# - Is the key present?
# - Is the value None?
# - Is the datatype correct?
# - Is the value within the expected range?
# - Is the data coming from a trusted source?