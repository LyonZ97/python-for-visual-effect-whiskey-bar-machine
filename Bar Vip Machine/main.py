import sys

from database import get_database


def main():
    vip_greeting()
    database = get_database()
    account_number = user_logging(database)
    user_welcome(account_number, database)
    make_whiskey_selection(account_number, database)
    display_user_profile(account_number, database)
    confirm_display_user_profile(account_number, database)
    display_special_offers(account_number, database)
    goodbye_message(account_number, database)


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
    print("")
    print(f"Welcome {username}!")
    print(f"Our honourable {vip_grade} vip to our whiskey club!")


def make_whiskey_selection(account_number, database):
    whiskey_options = database[account_number]["Whiskey_Selection"]

    while True:
        print("Available Whiskey Options:")
        whiskey_selection = database[account_number]["Whiskey_Selection"]
        print(f"{ whiskey_selection}")
        print("----------------------------")

        selection = input("Choose your whiskey: ")

        if selection in whiskey_options:
            database[account_number]["Whiskey_Selection"] = selection
            print("Whiskey selection updated successfully!")
            print("")
            break
        else:
            print("Invalid selection. Please choose from the available options.")


def display_user_profile(account_number, database):
    user_data = database[account_number]
    print("User Profile:")
    print(f"Username: {user_data['username']}")
    print(f"VIP Grade: {user_data['vip_grade']}")
    print(f"Whiskey Selection: {user_data['Whiskey_Selection']}")


def confirm_display_user_profile(account_number, database):
    confirmation = input("Profile confirmed? (yes/no): ").lower()

    if confirmation == "yes":
        print("")
        print("Your order is on the way!")
    else:
        print("")
        print("User profile display cancelled.")


def display_special_offers(account_number, database):
    vip_grade = database[account_number]["vip_grade"]
    print("-----------------------------------")
    print("Special Offers for VIP Members:")

    if vip_grade == "Bronze":
        print("10 Percent discount on your next visit!")

    elif vip_grade == "Gold":
        print("Free appetizer with every whiskey purchase!")

    elif vip_grade == "Diamond":
        print("Exclusive access to limited edition whiskeys!")


def goodbye_message(account_number, database):
    print("")
    print("Thank you for using our service, hope to meet you next time!")


if __name__ == "__main__":
    main()
