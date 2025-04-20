class MetadataRecord:
    
    """
    Represents a single metadata record for an image file.

    This class functions as a container for specific file data, such as
    its filename, format, size, and URL. It allows updating its fields
    individually and exporting its data to a dictionary.

    Attributes:
        filename (str): The filename of the image file.
        format (str): The file format (e.g., 'PNG', 'JPG').
        size (float): The size of the file in bytes.
        url (str): The URL associated with the file (if applicable).

    Methods:
        __init__(filename: str, format: str, size: float, url: str):
            Initializes a new metadata record with the provided data.
        update_field(field: str, value):
            Updates the value of a specific field in the record.
            Raises KeyError if the field does not exist.
        to_dict():
            Returns a dictionary containing all the record's data.

    """

    def __init__(self, filename: str, format: str, size: float, url: str):
        self.filename = filename
        self.format = format
        self.size = size
        self.url = url

    def update_field(self, field: str, value):
        if hasattr(self, field):
            setattr(self, field, value)
        else:
            raise KeyError(f"Field '{field}' does not exist.")

    def to_dict(self):
        return {
            "file name": self.filename,
            "format": self.format,
            "size": self.size,
            "url": self.url,
        }
