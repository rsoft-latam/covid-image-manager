import os
import shutil
from .image_record import ImageRecord


class ImageManager:

    """
    Manages file operations for medical images.

    This class provides methods to add, delete, list, and edit
    (move/rename) image files, organized by categories within
    a base directory structure.

    Attributes:
        base_dir (str): Base directory where images are stored.

    Methods:
        __init__(base_dir="data/COVID-19_Radiography_Dataset"):
            Initializes the manager with a base directory.
        get_image_path(category, filename):
            Returns the full path to a specific image.
        add_image(source_path, category, new_filename=None):
            Adds an image file to a category, creating directories if necessary.
        delete_image(category, filename):
            Deletes an image file by category and filename.
        list_images(category):
            Lists all image files within a category.
        edit_image(old_category, old_filename, new_category=None, new_filename=None):
            Renames and/or moves an image file to a new location or name.
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

    def edit_image(self, old_category, old_filename, new_category=None, new_filename=None):
        """
        Renames and/or moves an image to a new filename or category.

        Parameters:
        - old_category: Current category of the image
        - old_filename: Current filename
        - new_category: New category (optional)
        - new_filename: New filename (optional)
        """
        src_path = self.get_image_path(old_category, old_filename)

        if not os.path.exists(src_path):
            raise FileNotFoundError("Original image not found.")

        new_category = new_category or old_category
        new_filename = new_filename or old_filename

        dst_path = self.get_image_path(new_category, new_filename)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)

        shutil.move(src_path, dst_path)