from cli.image_menu import image_crud_menu
from cli.metadata_menu import metadata_crud_menu

def show_menu():
    while True:
        print("\n=== COVID Image Manager CLI ===")
        print("1. Image Management")
        print("2. Metadata Management")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            image_crud_menu()
        elif choice == "2":
            metadata_crud_menu()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    show_menu()
