bill_amount = float(input("Enter the total bill amount: $"))
payment_amount = float(input("Enter the payment amount: $"))

due_amount = bill_amount - payment_amount

if due_amount > 0:
    print(f"Amount due: ${due_amount:.2f}")
elif due_amount == 0:
    print("Bill paid in full. No amount due.")
else:
    print(f"Overpayment (refund): ${abs(due_amount):.2f}")