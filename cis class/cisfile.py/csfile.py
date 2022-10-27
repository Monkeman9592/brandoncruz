def happyBirthday(name,age):
    print("Happy Birthday!")
    print(name)
    print("you are", age ,"today")

def main():
    name = input("Enter the Birthday person's name: ")
    age  = int(input("How old are you today: "))
    happyBirthday(name,age)

main()