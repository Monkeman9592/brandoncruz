
def deposit(balance,dep):
    if dep > 0:
        
        print("Do the deposit")
    else:
        print("do not deposit")
    
def withdrawal(balance,wd):
    if wd < 0:
        print("make the withdraw ")
        if wd > balance:
            print(" to big of a withdrawl")
    else:
        print("can not withdraw")
    print(balance - wd)

def main():
    name = str(input("Enter name: "))
    balance = int(input("What is your current acount balance: "))
    print(name + " Welcome to your bank account")
    print("your current account balence is ",f"{balance}"  )

    dep = int(input("how much would you like to deposit: "))
    print("your new balance is: " ,balance + dep)

    wd = int(input("how much would you like to withdrawal: "))
    print("your new balance is: ",balance - wd)

    deposit(name,balance,dep,)
    withdrawal(name,balance,wd)

main()