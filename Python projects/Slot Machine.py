#Python Slot Machine

import random

def spin_row():
    symbols = ["🍒","🍉","🍋","🍓"]
    return [random.choice(symbols)for symbol in range (3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")
def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0]=="🍒":
            return bet * 3
        elif row[0]=="🍉":
            return bet * 5
        elif row[0]=="🍋":
            return bet * 10
        elif row[0]=="🍓":
            return bet * 20
    return 0

def main():
    #default balance
    balance = 100

    print("**********************************")
    print("   Welcome to SLOT MACHINE GAME   ")
    print("   Symbols 🍒 🍉 🍋 🍓    ")
    print("**********************************")
    while balance > 0:
        print(f"Current balance is ${balance} ")
        bet = input("Enter your bet ammount: ")
        if not bet.isdigit():
            print("Enter a valid amount")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insuficient balance")
            continue
        if bet <= 0:
            print("Bet can not be less then 0")
            continue
        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        #payout
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")
        balance += payout

        play_again = input("Do you wish to continue (Y/N): ").upper()

        if play_again != "Y":
            break
    
    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")

if __name__ == "__main__":
    main()
