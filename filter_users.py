import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    for user in filtered_users:
        print(user)


def filter_users_by_age(min_age):
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user["age"] >= min_age]
    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name, age, or email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        try:
            min_age = int(input("Enter the minimum age to filter users: ").strip())
            filter_users_by_age(min_age)
        except ValueError:
            print("Please enter a valid number for age.")

    elif filter_option == "email":
        email_to_search = input("Enter an email address to filter users: ").strip()
        filter_users_by_email(email_to_search)
        print("Filter by email initiated...")

    else:
        print("Filtering by that option is not yet supported.")