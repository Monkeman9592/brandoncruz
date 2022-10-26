def bank(name,balence,deposit,withdrawal):
    print(+ name + "Welcome to your bank account")
    print("your current account balence is ", balence ,)
    print("your new balence is")

def User_Name__Input():
    name = input("Enter name: ")
    balence = int(input("What is your current acount balance: "))
    print(f"{balence}")
    deposit = int(input("how much would you like to deposit: "))
    if deposit > 0:
        
        print("Do the deposit")
    else:
        print("do not deposit")
    print(balence + deposit )



    withdrawal = int(input("how much would you like to withdrawal: "))
    if withdrawal > 0:
        print("make the withdraw ")
        if withdrawal > balence:
            print(" to big of a withdrawl")

    print(f"{balence}")

    bank(name,balence,deposit,withdrawal)

User_Name__Input()


