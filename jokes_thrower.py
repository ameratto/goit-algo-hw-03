from jokes import get_random_joke

def main():
    user_name = input("Please enter your name: ")
    if not user_name:
        print("Hello unknown user!")
    else:
        print(f"Hello {user_name}!")

    user_answer = ""

    while user_answer != "n":
        user_answer = input("Do you want hear a joke? (y/n): ")
        if user_answer == "y":
            print(get_random_joke())
    print(f"Bye {user_name}!")


if __name__ == "__main__":
    main()