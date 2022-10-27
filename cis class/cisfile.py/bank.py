
def deposit(dep,balance):
    if dep > 0:        
        print("Do the deposit")
        print("your new balance is: ")
        
    else:
        print("do not deposit")
    
def withdrawal(wd,balance):
    if wd > balance:
        print("invalid withdrawal")
        
        

    elif wd < balance:
        print("your new balance is: ",)
    else:
       print("can not make the withdrawal")
    

def main():
    name = str(input("Enter name: "))
    balance = int(input("What is your current acount balance: "))
    print(name + " Welcome to your bank account")
    print("your current account balence is ", balance  )
    dep = int(input("how much would you like to deposit: "))
    deposit(dep,balance)
    print(balance + dep)
    wd = int(input("how much would you like to withdrawal: "))
    withdrawal(wd,balance)
    print(balance - wd )

  
main()

