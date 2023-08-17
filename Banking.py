# Initialize an empty dictionary called 'accounts'
accounts = {}

def create_account():
    name = input("Enter your name: ")
    account_number = len(accounts) + 1
    accounts[account_number] = {
        'name': name,
        'balance': 0
    }
    print("Account created successfully. Your account number is ", account_number)

def deposit_funds(account_number):
    if account_number in accounts:
        amount = float(input("Enter the deposit amount: "))
        accounts[account_number]['balance'] += amount
        print("Deposit successful")
    else:
        print("Account not found.")

def withdraw_funds(account_number):
    if account_number in accounts:
        amount = float(input("Enter the withdrawal amount: "))
        if amount <= accounts[account_number]['balance']:
            accounts[account_number]['balance'] -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    else:
        print("Account not found")

def check_balance(account_number):
    if account_number in accounts:
        balance = accounts[account_number]['balance']
        print("Your account balance is:", balance)
    else:
        print("Account not found.")

while True:
    print("\nMenu")
    print("1. Create an account")
    print("2. Deposit funds")
    print("3. Withdraw funds")
    print("4. Check balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        acc_number = int(input("Enter your account number: "))
        deposit_funds(acc_number)
    elif choice == '3':
        acc_number = int(input("Enter your account number: "))
        withdraw_funds(acc_number)
    elif choice == '4':
        acc_number = int(input("Enter your account number: "))
        check_balance(acc_number)
    elif choice == '5':
        print("Exiting the program. Goodbye")
        break
    else:
        print("Invalid choice. Please choose a valid option")