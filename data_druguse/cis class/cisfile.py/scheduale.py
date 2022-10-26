def schedule(name,city,major,enrolled):
    print(name +" lives in " + city)
    print(name + " is majoring in " + major + " and is enrolled in "+enrolled)

def main():
    name = input("Enter the person's name: ")
    city = input("Enter the person's city: ")
    major = input("Enter the person's major: ")
    enrolled = input("Enter the person's enrollment: ")
    schedule(name,city,major,enrolled)

main()