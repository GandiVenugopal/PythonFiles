# Assignment 4
N = 5000

print("Welcome to Simple ATM\n 1.Check Balance \n 2.Deposit \n 3.Withdraw \n 4.Exit")
a = int(input("Choose an option: "))

while a != 4:
    if a == 1:
        print(f"Available Accounts Balance: {N}")
    elif a == 2:
        d = int(input("Enter deposit amount: "))
        N = N + d
        print("Deposit Successful")
        print(f"Available Accounts Balance: {N}")
    elif a == 3:
        w = int(input("Enter withdraw amount: "))
        if w > N:
            print("Insufficient Funds")
        else:
            N = N - w
            print("Withdraw Successful")
            print(f"Available Accounts Balance: {N}")
    else:
        print("Invalid Input")
    print("\nWelcome to Simple ATM\n 1.Check Balance \n 2.Deposit \n 3.Withdraw \n 4.Exit")
    a = int(input("Choose an option: "))

print("Thank You")

