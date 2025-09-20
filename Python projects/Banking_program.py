#Banking program using python

#show balance
def show_balance(balance):
    print(f"Your current Balance is ${balance:.2f}: ")

#deposite money
def deposite():
    amount = float(input("Enter the amount you want to Deposite: "))
    if amount < 0 :
        print("Enter an valid amount to deposite.")
        return 0
    else:
        return amount

#withdraw from bank
def withdraw(balance):
    amount = float(input("Enter the amount you want to Withdraw: "))
    if amount > balance:
        print("Insuficient Balance.")
        return 0
    elif amount < 0:
        print("Try again.")
        return 0
    else:
        return amount
#main 
def main():
    balance = 0
    is_running = True

    while is_running:
        print("****************************")
        print("       Banking Program      ")
        print("****************************")
        print("1. Show My Balance.")
        print("2. I Want to Deposite. ")
        print("3. Withdraw Money.")
        print("4. Exit the Program.")
        print("#############################")
        choice = input("Enter your choice (1-4):")
        if choice =="1":
            show_balance(balance)
        elif choice == "2":
            balance +=deposite()
        elif choice == "3":
            balance-= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("This is not a valid choice.")

    print("Thank you. Have a nice day.")

if __name__ == "__main__":
    main()
