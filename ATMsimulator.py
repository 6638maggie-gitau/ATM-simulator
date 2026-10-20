balance = 5000

def show_menu():
    print("===MY ATM===")
    print("1.Check balance")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.Exit")


def check_balance():
    print("the balance is 5000")


def deposit():
    global balance 
    amount =int(input("how much would you like to deposit"))
    if amount >0:
        balance += amount
        print("Deposit successfully")
        print("Your new balance is ksh", balance)
    else:
        print("univalid amount")


def withdraw ():
    global balance
    amount = int(input("how much would you like to withdraw?"))
    if amount <=0:
        print("Enter a valid amount!")
    elif amount <= balance:
        balance -= amount
        print("Withdrawl successfull")
        print("Your new balance is ksh", balance)
    else:
        print("Insufficient balance")
 

def main():
    show_menu()
    choice=input("choose an option...")
    if choice == "1":
     check_balance ()
    elif choice =="2":
        deposit ()
    elif choice =="3":
        withdraw()
    elif choice =="4":
        print("Thank you for using ATM")
    else:
        print("INVALID OPTION!")

main ()
