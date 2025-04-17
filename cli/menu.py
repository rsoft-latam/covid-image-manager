from core.images.dataset_utils import download_dataset, show_dataset_summary
from core.images.image_manager import ImageManager

def show_menu():
    """ Display the main menu and handles user interaction.

    This funcion presents a menu of options to the user,
    allowing them to interact with radiography images.

    It includes options for downloading the dataset, 
    viewing summaries,listing,images, and managing images 
    adding, deleting, and possibly renaming.

    Parameters:
    None

    Returns:
    None

    See Also:
        download_dataset: Function to download the dataset.
        show_dataset_summary: Funcion to show dataset summary.
        ImageManger: Class for image management.
    Example:
        >>> show_menu()
        ---COVID IMAGE MANAGEMENT CLI---
             print("\n--- COVID Image Management CLI ---")
        1. Download images from Kaggle
        2. Show dataset summary
        3. List images by category
        4. Add new image
        5. Delete image
        6. Rename image
        7. Exit
        Select an option:
    """
    manager = ImageManager()

    while True:
        print("\n--- COVID Image Management CLI ---")
        print("1. Download images from Kaggle")
        print("2. Show dataset summary")
        print("3. List images by category")
        print("4. Add new image")
        print("5. Delete image")
        print("6. Rename image")
        print("7. Exit")

        option = input("Select an option: ")

        if option == "1":
            download_dataset()

        elif option == "2":
            show_dataset_summary()

        elif option == "3":
            category = input("Enter category (COVID, NORMAL, Viral Pneumonia): ")
            try:
                images = manager.list_images(category)
                print(f"\nImages in '{category}':")
                for img in images:
                    print(f" - {img}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "4":
            path = input("Full path to the image file: ")
            category = input("Category (COVID, NORMAL, Viral Pneumonia): ")
            new_name = input("New filename (optional): ").strip() or None
            try:
                result = manager.add_image(path, category, new_name)
                print(f"✅ Image added: {result}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "5":
            category = input("Category of the image: ")
            filename = input("Filename to delete: ")
            if manager.delete_image(category, filename):
                print("✅ Image deleted.")
            else:
                print("⚠️ Image not found.")

        elif option == "6":
            print("⚠️ Rename image is not implemented yet.")  # opcional si no tienes rename
        elif option == "7":
            print("👋 Exiting....")
            break
        else:
            print("❌ Invalid option.")
