import pandas as pd
import random

def create_account():
    # Creates a new bank account
    global df, account_created
    name = input("Enter your name: ")
    i_deposit = float(input("Enter initial deposit amount: "))
    pw = input("Enter a 6-digit password: ")
    
    if len(pw) != 6:
        print("Invalid password! Please enter a 6-digit password.")
        return
    
    while True:
        acc_number = random.randint(10000000, 99999999)
        if acc_number not in df["Account Number"].values:
            break

    new_account = pd.DataFrame({"Account Number": [acc_number], "Name": [name], "Balance": [i_deposit], "Password": [pw]})
    df = pd.concat([df, new_account], ignore_index=True)
    account_created = True  # Account is successfully created
    print(f"Account created successfully. Your account number is {acc_number}.")


def deposit():
    if not account_created:
        print("You need to create an account first to perform a deposit.")
        return
    
    acc_number = int(input("Enter your account number: "))
    pw = input("Enter your password:")
    if df[(df["Account Number"] == acc_number) & (df["Password"] == pw)].empty:
        print("Invalid account number or password.")
        return

    amt = float(input("Enter amount to deposit: "))
    filtered_df = df[(df["Account Number"] == acc_number) & (df["Password"] == pw)]
    df.loc[filtered_df.index, "Balance"] += amt
    print(f"Deposit successful. Your new balance is {df.loc[df['Account Number'] == acc_number, 'Balance'].values[0]}.")


def withdraw():
    if not account_created:
        print("You need to create an account first to perform a withdrawal.")
        return
    
    acc_number = int(input("Enter your account number: "))
    pw = input("Enter your password:")
    if df[(df["Account Number"] == acc_number) & (df["Password"] == pw)].empty:
        print("Invalid account number or password.")
        return

    amt = float(input("Enter amount to withdraw: "))
    if df.loc[(df["Account Number"] == acc_number) & (df["Password"] == pw), "Balance"].values[0] >= amt:
        df.loc[(df["Account Number"] == acc_number) & (df["Password"] == pw), "Balance"] -= amt
        print(f"Withdrawal successful. Your new balance is {df.loc[df['Account Number'] == acc_number, 'Balance'].values[0]}.")
    else:
        print("Insufficient balance.")


def check_balance():
    if not account_created:
        print("You need to create an account first to check the balance.")
        return
    
    acc_number = int(input("Enter your account number: "))
    pw = input("Enter your password:")
    if df[(df["Account Number"] == acc_number) & (df["Password"] == pw)].empty:
        print("Invalid account number or password.")
        return

    balance = df.loc[(df["Account Number"] == acc_number) & (df["Password"] == pw), "Balance"].values[0]
    print(f"Your current balance is {balance}.")


# Initialize an empty DataFrame to store account information
df = pd.DataFrame(columns=["Account Number", "Name", "Balance", "Password"])
account_created = False  # Flag to check if an account is created

# Main
print("\nWelcome to Govarthini Banking System")
while True:
    if not account_created:
        print("\nYou need to create an account to proceed with any other operations.")
    
    print("\nEnter your choice:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        print("Thank you for using Govarthini Banking System!")
        break
    else:
        print("Invalid choice. Please try again.")
