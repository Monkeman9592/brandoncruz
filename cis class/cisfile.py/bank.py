
def select(menu):
    if menu == "1":
        name = str(input("Enter name: "))
    print(name + " Welcome to your Bank Account")


def deposit(dep,):
    if dep > 0:   
        print("Do the deposit")
        print("your new balance is: ")
    else:
        print("do not deposit")

def withdrawal(wd,balance):
    if wd > balance:
        print("invalid withdrawal")
    elif wd <= balance:
        print("your new balance is: ",)
    else:
       print("can not make the withdrawal")

def main():
    menu = input("please select a menu option: ")
    select(menu)
    
    balance = int(input("What is your current acount balance: "))
    print("your current account balence is ", balance  )
    dep = int(input("how much would you like to deposit: "))
    deposit(dep,balance)
    balance = (balance + dep)
    print(balance)
    wd = int(input("how much would you like to withdrawal: "))
    withdrawal(wd,balance)
    balance = (balance- wd )
    print(balance)  
main()

