from core.images.dataset_utils import download_dataset, show_dataset_summary
from core.images.image_manager import ImageManager

def image_crud_menu():
    """
    Implements the command-line interface for image management.

    Presents a menu with options to download the dataset, list images by category,
    add, edit, and delete images. Interacts with the ImageManager class to perform
    management operations and with functions for dataset download.
    The menu runs in a loop until the user chooses to  exit.
    """
    print("\n--- Image Management CLI ---")
    image_manager = ImageManager()

    while True:
        print("\n1. Download images from Kaggle")
        print("2. List images by category (COVID, Normal, Lung_Opacity, Viral Pneumonia)")
        print("3. Add new image")
        print("4. Edit image")
        print("5. Delete image")
        print("0. Return to main menu")

        option = input("Select an option: ")

        if option == "1":
            download_dataset()

        elif option == "2":
            category = input("Enter category (COVID, Normal, Lung_Opacity, Viral Pneumonia): ")
            try:
                images = image_manager.list_images(category)
                print(f"\nImages in '{category}':")
                for img in images:
                    print(f" - {img}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "3":
            path = input("Full path to the image file: ")
            category = input("Category (COVID, Normal, Lung_Opacity, Viral Pneumonia): ")
            new_name = input("New filename (optional): ").strip() or None
            try:
                result = image_manager.add_image(path, category, new_name)
                print(f"Image added: {result}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "4":
            old_category = input("Current category of the image: (COVID, Normal, Lung_Opacity, Viral Pneumonia)").strip()
            old_filename = input("Current filename: ").strip()
            new_category = input("New category (leave blank to keep current): ").strip() or None
            new_filename = input("New filename (leave blank to keep current): ").strip() or None

            try:
                image_manager.edit_image(
                    old_category=old_category,
                    old_filename=old_filename,
                    new_category=new_category,
                    new_filename=new_filename
                )
                print("Image edited successfully.")
            except Exception as e:
                print(f"Error editing image: {e}")

        elif option == "5":
            category = input("Category of the image: ")
            filename = input("Filename to delete: ")
            if image_manager.delete_image(category, filename):
                print("Image deleted.")
            else:
                print("Image not found.")

        elif option == "0":
            print("Exiting....")
            break
        else:
            print("Invalid option.")
