import pandas as pd
from .metadata_record import MetadataRecord
from .metadata_validator import MetadataValidator

class MetadataManager:
    VALID_CATEGORIES = [
        "COVID", "Normal", "Lung_Opacity", "Viral Pneumonia"
    ]

    def __init__(self, category: str, metadata_dir: str):
        if category not in self.VALID_CATEGORIES:
            raise ValueError(f"Invalid category: {category}")
        self.category = category
        self.records = {}
        self._load_metadata(metadata_dir)

    def _load_metadata(self, metadata_dir: str):
        file_path = f"{metadata_dir}/{self.category}.metadata.xlsx"
        df = pd.read_excel(file_path)
        df.columns = [col.strip().lower() for col in df.columns]
        for _, row in df.iterrows():
            data = row.to_dict()
            MetadataValidator.validate(data)
            record = MetadataRecord(
                filename=data["file name"],
                format=data["format"],
                size=data["size"],
                url=data["url"]
            )
            self.records[record.filename] = record

    def list_all(self):
        return list(self.records.values())

    def add_record(self, data: dict):
        MetadataValidator.validate(data)
        record = MetadataRecord(
            filename=data["file name"],
            format=data["format"],
            size=data["size"],
            url=data["url"]
        )
        self.records[record.filename] = record

    def edit_record(self, filename: str, field: str, new_value):
        if filename not in self.records:
            raise KeyError(f"Filename '{filename}' not found")
        self.records[filename].update_field(field, new_value)

    def delete_record(self, filename: str):
        if filename in self.records:
            del self.records[filename]
