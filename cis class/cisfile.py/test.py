
def deposit(dep):
    global balance
    balance = (balance + dep)
    print(balance)
def withdrawal(wd):
    global balance
    balance = (balance - wd )
    print(balance)

def main():
    global balance
    name = str(input("Enter name: "))
    print(name + " Welcome to your Bank Account")
    balance = int(input("What is your current acount balance: "))
    print(name + " Welcome to your bank account")
    menu = input("Menu options: deposit, withdrawal, else: ")
    
    if menu == "deposit":
        dep = int(input("how much would you like to deposit: "))
        if dep > 0:   
            deposit(dep)
            print("Do the deposit")
            print("your new balance is: ")
        else:
            print("do not deposit")
    elif menu == "withdrawal":
        wd = int(input("how much would you like to withdrawal: "))    
        if wd <= balance:
            withdrawal(wd)
            print("your new balance is: ")

        else:
            print("invalid withdrawal")
    else:
        print("invalid input")
    print(balance)
main()

