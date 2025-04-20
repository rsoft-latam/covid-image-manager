import os
from core.metadata.metadata_manager import MetadataManager
from core.metadata.metadata_validator import MetadataValidator

def metadata_crud_menu():
    """
    Implements the command-line interface for metadata management.

    Presents a menu with options to load metadata by category, list them,
    add new metadata records, edit, and delete existing records.
    Requires metadata to be loaded into memory before performing most
    operations. Interacts with the MetadataManager class to manage the data.
    The menu runs in a loop until the user chooses the exit option.
    """
    print("\n--- Metadata Management CLI ---")
    managers = {}
    metadata_loaded = False
    metadata_path = os.path.join(os.path.dirname(__file__), "..", "metadata")

    while True:
        print("\n1. Load All metadata into memory")
        print("2. List metadata by category (COVID, Normal, Lung_Opacity, Viral Pneumonia)")
        print("3. Add new metadata")
        print("4. Edit metadata")
        print("5. Delete metadata")
        print("0. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            categories = ["COVID", "Normal", "Lung_Opacity", "Viral Pneumonia"]
            try:
                for category in categories:
                    manager = MetadataManager(category, metadata_path)
                    managers[category] = manager
                metadata_loaded = True
                print("All metadata loaded successfully.")
            except Exception as e:
                print(f"Error loading metadata: {e}")

        elif choice == "2":
            if not metadata_loaded:
                print("You must load metadata first.")
                continue
            category = input("Enter category: ").strip()
            if category in managers:
                for record in managers[category].list_all():
                    print(record.to_dict())
            else:
                print("Category not found.")

        elif choice == "3":
            if not metadata_loaded:
                print("You must load metadata first.")
                continue
            category = input("Enter category: ").strip()
            if category in managers:
                try:
                    data = {
                        "file name": input("File name: ").strip(),
                        "format": input("Format (JPG, PNG): ").strip(),
                        "size": input("Size (e.g. 256*256 or 123.45): ").strip(),
                        "url": input("URL: ").strip()
                    }
                    managers[category].add_record(data)
                    print("Metadata record added.")
                except Exception as e:
                    print(f"Error adding record: {e}")
            else:
                print("Category not found.")

        elif choice == "4":
            if not metadata_loaded:
                print("You must load metadata first.")
                continue
            category = input("Enter category: ").strip()
            if category in managers:
                filename = input("File name to edit: ").strip()
                field = input("Field to edit (format, size, url): ").strip()
                new_value = input("New value: ").strip()
                if field == "size" and "*" in new_value:
                    parts = new_value.split("*")
                    new_value = int(parts[0]) * int(parts[1])
                try:
                    if field == "size":
                        new_value = float(new_value)
                    managers[category].edit_record(filename, field, new_value)
                    print("Metadata record updated.")
                except Exception as e:
                    print(f"Error editing record: {e}")
            else:
                print("Category not found.")

        elif choice == "5":
            if not metadata_loaded:
                print("You must load metadata first.")
                continue
            category = input("Enter category: ").strip()
            if category in managers:
                filename = input("File name to delete: ").strip()
                try:
                    managers[category].delete_record(filename)
                    print("Metadata record deleted.")
                except Exception as e:
                    print(f"Error deleting record: {e}")
            else:
                print("Category not found.")

        elif choice == "0":
            print("Exiting....")
            break

        else:
            print("Invalid option. Try again.")

