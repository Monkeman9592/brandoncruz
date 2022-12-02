
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
    try:
        name = str(input("Enter name: "))
    except:
        print("invalid input")
    print(name + " Welcome to your Bank Account")
    try:
        balance = int(input("What is your current acount balance: "))
        print(name + " Welcome to your bank account")
    except:
        print("invalid input")
    try:
        menu = input("Menu options: deposit, withdrawal, else: ")
    except:
        print("invalid input")
    if menu == "deposit":
        try:
            dep = int(input("how much would you like to deposit: "))
        except:
            print("invalid input")
        if dep > 0:   
            deposit(dep)
            print("Do the deposit")
            print("your new balance is: ")
        else:
            print("do not deposit")
    elif menu == "withdrawal":
        try:
            wd = int(input("how much would you like to withdrawal: "))   
        except:
            print("invalid input") 
        if wd <= balance:
            withdrawal(wd)
            print("your new balance is: ")

        else:
            print("invalid withdrawal")
    else:
        print("invalid input")
    try:
        print(balance)
    except:
        print("invalid input")
main()

