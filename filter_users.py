import json


def load_users():
    """Load users from the local JSON file."""
    with open("users.json", "r") as file:
        return json.load(file)


def filter_by_name(name):
    """Filter users by name (case-insensitive)."""
    users = load_users()
    matches = [user for user in users if user["name"].lower() == name.lower()]
    for user in matches:
        print(user)


def filter_by_age(min_age):
    """Filter users by minimum age."""
    users = load_users()
    matches = [user for user in users if user["age"] >= min_age]
    for user in matches:
        print(user)


def filter_by_email(email):
    """Filter users by email address (case-insensitive)."""
    users = load_users()
    matches = [user for user in users if user["email"].lower() == email.lower()]
    for user in matches:
        print(user)


def main():
    """Prompt user and handle filtering logic."""
    filter_type = input("What would you like to filter by? (name, age, or email): ").strip().lower()

    if filter_type == "name":
        name = input("Enter a name to filter users: ").strip()
        filter_by_name(name)

    elif filter_type == "age":
        try:
            age = int(input("Enter the minimum age to filter users: ").strip())
            filter_by_age(age)
        except ValueError:
            print(" Please enter a valid number for age.")

    elif filter_type == "email":
        email = input("Enter an email address to filter users: ").strip()
        filter_by_email(email)

    else:
        print(" Filtering by that option is not supported.")


if __name__ == "__main__":
    main()
