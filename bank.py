def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient funds")
    curr_balance = balance - amount
    return curr_balance


if __name__ == "__main__":
    try:
        newBalance = withdraw(1000,1150)
        print(f"Your current balance is: {newBalance}")
    except Exception as e:
        print(f"Error: {e}")