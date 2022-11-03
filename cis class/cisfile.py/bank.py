def select(menu):
    if menu == "1":
        name = str(input("Enter name: "))
        print(name + " Welcome to your Bank Account")

def deposit(dep):
        if dep > 0:
            print("Do the deposit")
            print("your new balance is: ")
            
        else:
            print("do not deposit")

def withdrawal(balance,wd):
        if wd > balance:
            print("invalid withdrawal")
        elif wd <= balance:
            print("your new balance is: ",)
        else:
            print("can not make the withdrawal")

def pff(ahh):
    if ahh == "deposit":
            dep = int(input("how much would you like to deposit: "))
            deposit(dep)
            balance = (balance + dep)
            print(balance)
            running = True
            return running

    elif ahh == "withdrawal":
            wd = int(input("how much would you like to withdrawal: "))
            withdrawal(wd,balance)
            balance = (balance - wd )
            print(balance)
            running = True
            return running

    else:
        print("not a valid input")
        running = True
        return running


def main():
    menu = input("please select a menu option 1 to start ")
    select(menu)
    
    running = True
    while running:
        balance = int(input("What is your current acount balance: "))
        print("your current account balence is ", balance  )
        ahh = str(input("please select menu options deposit , withdrawal: "))
        running = pff(ahh,balance)
        
    
    
main()
