def select(menu):
    if menu == "1":
        name = str(input("Enter name: "))
        print(name + " Welcome to your Bank Account")
        balance = int(input("What is your current acount balance: "))
        print("your current account balence is ", balance  )
        run = True
        return run
    elif menu == "deposit":
            dep = int(input("how much would you like to deposit: "))
            if dep > 0:
                print("Do the deposit")
                print("your new balance is: ")
                balance = (balance + dep)
                print(balance)
                run = True
                return run
            else:
                print("do not deposit")
                run = True
                return run
    elif menu == "withdrawal":
            wd = int(input("how much would you like to withdrawal: "))
            if wd > balance:
                print("invalid withdrawal")
                run = True
                return run
            elif wd <= balance:
                print("your new balance is: ",)
                balance = (balance - wd )
                print(balance)
                run = True
                return run
            else:
                print("can not make the withdrawal")
                run = True
                return run
    else:
        print("not a valid input")
        run = True
        return run
def main():
    run = True
    while run:
        menu = input("please select a menu option 1  to start input name and balice, deposit or withdrawal ")
        run = select(menu)
    

main()