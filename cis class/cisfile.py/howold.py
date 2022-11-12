name = input("Please enter your name: ")
age = int(input("how old are you?"))

if 0 <= age <=  100:
    print(name + " and will be" , age + 5 , " in 10 years")
elif age <= 0:
    print("People cannot have a negative age")
elif age >= 100:
    print("100 is the maximum age for this program")