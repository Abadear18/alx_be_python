# shopping_list_manager.py

shopping_list = []

def show_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")

    elif choice == "3":
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
        if not shopping_list:
            print("List is empty.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")