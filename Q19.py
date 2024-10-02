#Write a menu driven program for count, reverse,sort the members of created list dynamically

def main_menu():
    lst = []

    while True:
        print("\nMenu:")
        print("1. Add an item to the list")
        print("2. Count items in the list")
        print("3. Reverse the list")
        print("4. Sort the list")
        print("5. Display the list")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            lst.append(item)
            print(f"'{item}' added to the list.")
        elif choice == '2':
            print(f"Count of items in the list: {len(lst)}")
        elif choice == '3':
            lst.reverse()
            print("List reversed.")
        elif choice == '4':
            lst.sort()
            print("List sorted.")
        elif choice == '5':
            print("Current list:", lst)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

