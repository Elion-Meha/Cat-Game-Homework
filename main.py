def create_cat():
    name = input("Enter your cat's name: ")
    color = input("Enter your cat's color: ")

    cat = {
        "name": name,
        "color": color,
        "intelligence": 10,
        "energy": 50,
        "weight": 10
    }
    return cat

def play(cat):
    print("\nYou play with your cat!")
    cat["energy"] -= 10
    cat["weight"] -= 1

def train(cat):
    print("\nYou train your cat!")
    cat["intelligence"] += 5
    cat["energy"] -= 15

def feed(cat):
    print("\nYou feed your cat!")
    cat["weight"] += 3
    cat["energy"] += 10

def sleep(cat):
    print("\nYour cat takes a nap.")
    cat["energy"] += 20

def main():
    cat = create_cat()
    while True:
        print("\nWhat would you like to do with your cat?")
        print("1. Play with your cat")
        print("2. Train your cat")
        print("3. Feed your cat")
        print("4. Put your cat to sleep")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            play(cat)
        elif choice == "2":
            train(cat)
        elif choice == "3":
            feed(cat)
        elif choice == "4":
            sleep(cat)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()