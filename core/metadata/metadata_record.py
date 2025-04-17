class MetadataRecord:
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
