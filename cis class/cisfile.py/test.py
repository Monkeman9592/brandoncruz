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
    x = 0 
    while x < 3:
        try:
            balance = int(input("What is your current acount balance: "))
            x = x + 1
            if balance > 0: 
                print(name + " your balance is ", balance)
                break
        except:
            x = x + 1
            print("invalid input")
    while True and x <= 3:
        try:
            menu = input("Menu options: deposit, withdrawal, else: ")
        except:
            print("invalid input")
        if menu == "deposit":
            i = 0
            while i <= 3:
                try:
                    dep = int(input("how much would you like to deposit: "))
                    i = i + 1
                    if dep > 0 :
                        break
                except:
                    i = i + 1
                    print("invalid input")
            if dep > 0:   
                deposit(dep)
                print("Do the deposit")
                print("your new balance is: ")
            else:
                print("do not deposit")
        elif menu == "withdrawal":
            i = 0
            while i<=3:
                try:
                    wd = int(input("how much would you like to withdrawal: ")) 
                    i = i + 1
                    if wd > 0 :
                        break 
                except:
                    i = i + 1
                    print("invalid input") 
            if wd <= balance:
                withdrawal(wd)
                print("your new balance is: ")
                print (balance)
                break
            else:
                print("invalid withdrawal")
        else:
            x = x + 1
            print("invalid input")
       

main()

