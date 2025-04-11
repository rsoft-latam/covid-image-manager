from datetime import datetime

class ImageRecord:
    """
    Represents a medical image and its associated metadata.
    """

    def __init__(self, filename, category, path, created_at=None):
        self.filename = filename
        self.category = category
        self.path = path
        self.created_at = created_at or datetime.now().isoformat()

    def __str__(self):
        return f"[{self.category}] {self.filename} ({self.created_at})"
