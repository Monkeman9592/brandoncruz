def main():
    

    name = str(input("Enter name: "))
    
    balance = int(input("What is your current acount balance: "))
    print(name + "Welcome to your bank account")
    print("your current account balence is ", balance ,)

    print(f"{balance}")
    deposit = int(input("how much would you like to deposit: "))
    if deposit > 0:
        
        print("Do the deposit")
    else:
        print("do not deposit")
    print(balance + deposit )



    withdrawal = int(input("how much would you like to withdrawal: "))
    if withdrawal < 0:
        print("make the withdraw ")
        if withdrawal > balance:
            print(" to big of a withdrawl")
    else:
        print("can not withdraw")
    print(balance - withdrawal)

main()

