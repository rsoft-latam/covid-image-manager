from core.images.dataset_utils import download_dataset, show_dataset_summary
from core.images.image_manager import ImageManager

def image_crud_menu():
    print("\n--- Image Management CLI ---")
    manager = ImageManager()

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
            category = input("Enter category (COVID, NORMAL, Viral Pneumonia): ")
            try:
                images = manager.list_images(category)
                print(f"\nImages in '{category}':")
                for img in images:
                    print(f" - {img}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "3":
            path = input("Full path to the image file: ")
            category = input("Category (COVID, NORMAL, Viral Pneumonia): ")
            new_name = input("New filename (optional): ").strip() or None
            try:
                result = manager.add_image(path, category, new_name)
                print(f"Image added: {result}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "4":
            print("Rename image is not implemented yet.") 

        elif option == "5":
            category = input("Category of the image: ")
            filename = input("Filename to delete: ")
            if manager.delete_image(category, filename):
                print("Image deleted.")
            else:
                print("Image not found.")

        elif option == "0":
            print("Exiting....")
            break
        else:
            print("Invalid option.")
