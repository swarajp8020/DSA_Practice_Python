transaction = {
    "transaction_id": "TXN1001",
    "customer_id": "CUST123",
    "amount": 4500.00,
    "transaction_type": "DEBIT"
}

print("printing obj: ", transaction)
print("printing data:")
print(transaction["transaction_id"])
print(transaction["customer_id"])
print(transaction["amount"])
print(transaction["transaction_type"])