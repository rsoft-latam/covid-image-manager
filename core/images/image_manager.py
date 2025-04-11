import os
import shutil
from .image_record import ImageRecord


class ImageManager:
    """
    Provides file operations for medical images:
    add, delete, and list images grouped by category.
    """

    def __init__(self, base_dir="data/COVID-19_Radiography_Dataset"):
        self.base_dir = base_dir

    def get_image_path(self, category, filename):
        """
        Returns the absolute path to the image file.
        """
        return os.path.join(self.base_dir, category, "images", filename)

    def add_image(self, source_path, category, new_filename=None):
        """
        Adds an image to the dataset under the specified category.
        If the structure doesn't exist, it is created automatically.
        """
        if not os.path.exists(source_path):
            raise FileNotFoundError("Source image file not found.")

        destination_dir = os.path.join(self.base_dir, category, "images")
        os.makedirs(destination_dir, exist_ok=True)

        final_filename = new_filename if new_filename else os.path.basename(source_path)
        destination_path = os.path.join(destination_dir, final_filename)

        shutil.copy(source_path, destination_path)
        return ImageRecord(final_filename, category, destination_path)

    def delete_image(self, category, filename):
        """
        Deletes an image by category and filename.
        """
        path = self.get_image_path(category, filename)
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

    def list_images(self, category):
        """
        Lists all images within the specified category.
        """
        folder = os.path.join(self.base_dir, category, "images")
        if not os.path.exists(folder):
            raise ValueError(f"The category '{category}' does not exist.")

        files = os.listdir(folder)
        return [ImageRecord(f, category, os.path.join(folder, f)) for f in files]
