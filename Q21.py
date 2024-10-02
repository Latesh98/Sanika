 #Write a menu driven program to display the keys , values , update,and pop the items from dictionary

def dictionary_menu():
    d = {}

    while True:
        print("\nMenu:")
        print("1. Add or update an item")
        print("2. Display keys")
        print("3. Display values")
        print("4. Update an item")
        print("5. Pop an item")
        print("6. Display the entire dictionary")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            d[key] = value
            print(f"Item added/updated: {key} = {value}")

        elif choice == '2':
            print("Keys in the dictionary:", list(d.keys()))

        elif choice == '3':
            print("Values in the dictionary:", list(d.values()))

        elif choice == '4':
            key = input("Enter the key to update: ")
            if key in d:
                value = input("Enter the new value: ")
                d[key] = value
                print(f"Item updated: {key} = {value}")
            else:
                print("Key not found.")

        elif choice == '5':
            key = input("Enter the key to pop: ")
            value = d.pop(key, "Key not found.")
            print(f"Popped item: {key} = {value}")

        elif choice == '6':
            print("Current dictionary:", d)

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    dictionary_menu()
