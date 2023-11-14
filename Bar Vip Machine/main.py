import sys

from database import get_database


def main():
    vip_greeting()
    database = get_database()
    account_number = user_logging(database)
    user_welcome(account_number, database)


def vip_greeting():
    print("")
    print("Welcome to the Seneca Whiskey Bar!")
    print("----------------------------------")


def user_logging(database):
    additional_attempts = 2
    while True:
        account_number, password = get_user_data()
        if validate_user(account_number, password, database):
            break

        if additional_attempts == 0:
            print("SECURITY WARNING!!! LOGGING SESSION OUT!")
            sys.exit(1)

        additional_attempts -= 1
        print("Please try again.")
    return account_number


def get_user_data():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    return account_number, password


def validate_user(account_number, password, database):
    user_data = database.get(account_number)
    if user_data and user_data.get("password") == password:
        print("")
        print(f"Login successful! VIP Grade: {user_data.get('vip_grade')}")
        return True
    else:
        print("Invalid account number or password.")
        return False


def user_welcome(account_number, database):
    username = database[account_number]["username"]
    vip_grade = database[account_number]["vip_grade"]
    Whiskey_Selection = database[account_number]["Whiskey_Selection"]
    print("")
    print(f"Welcome {username}!")
    print(f"Our honourable {vip_grade} vip to our whiskey club!")
    print(f"Here's your selection: {Whiskey_Selection}")


if __name__ == "__main__":
    main()
