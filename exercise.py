def ask_user_name():
    user_name = input("put your username here or press '0' to quit:")
    return user_name

def ask_password():
    user_password = input("put your password here or press '0' to quit:")
    return user_password
user = ask_user_name()
if user != '0':
    password = ask_password()
    if password != '0':
        with open ("exercise.txt", "w") as file:
            file.write(f"{user} {password}")
print("application is closed")