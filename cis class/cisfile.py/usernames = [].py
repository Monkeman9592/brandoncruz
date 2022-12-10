usernames = []

print("Enter three options for your username")

while len(usernames) < 3:
    username = input("Choose a username: [4-10 characters] ")
    if 4 <= len(username):
        print(f"Thank you. The username {username} is valid")
        usernames.append(username)
    else:
        print("The username must be between 4 and 10 characters long")

print(usernames)