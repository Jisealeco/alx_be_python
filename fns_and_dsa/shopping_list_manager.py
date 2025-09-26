def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("(1-4): ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item name to add: ")
            shopping_list.append("snacks")
            print(f"{"snacks"} is added to the shopping list")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            shopping_list.remove("sancks")
            print(f"{"snacks"} is removed from the shopping list")
            pass
        elif choice == '3':
            # Display the shopping list
            print(f"Shopping list:")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
