from datetime import datetime

class ImageRecord:
    """
    Represents a medical image and its associated metadata.

    This class acts as a data container to store information about a
    specific image file, including its filename, category, file system
    path, and the record's creation date/time.

    Attributes:
        filename (str): The filename of the image.
        category (str): The category the image belongs to.
        path (str): The full file system path to the image.
        created_at (str): The date and time the record was created 

    Methods:
        __init__(filename, category, path, created_at=None):
            Initializes a new ImageRecord instance.
        __str__():
            Returns a string representation of the object.
    """

    def __init__(self, filename, category, path, created_at=None):
        self.filename = filename
        self.category = category
        self.path = path
        self.created_at = created_at or datetime.now().isoformat()

    def __str__(self):
        return f"[{self.category}] {self.filename} ({self.created_at})"
