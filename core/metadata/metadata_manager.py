import pandas as pd
from .metadata_record import MetadataRecord
from .metadata_validator import MetadataValidator

class MetadataManager:
    """
    Manages metadata for a specific category of images.

    This class loads, stores, and allows manipulating metadata records
    from an Excel file associated with a predefined image category.
    It depends on the existence of a validator (MetadataValidator) and
    a record model (MetadataRecord).

    Class Attributes:
        VALID_CATEGORIES (list): A list of strings representing the valid image categories.

    Instance Attributes:
        category (str): The metadata category managed by this instance.
        records (dict): A dictionary where keys are filenames (str) and values
                        are MetadataRecord objects.

    Methods:
        __init__(category: str, metadata_dir: str):
            Initializes the metadata manager for a given category and loads data
            from the specified directory. Validates the category.
        _load_metadata(metadata_dir: str):
            Internal method to load metadata from the Excel file corresponding
            to the category. Processes, validates, and stores the records.
        list_all():
            Returns a list of all loaded MetadataRecord objects.
        add_record(data: dict):
            Adds a new metadata record to the collection. Validates the input data.
        edit_record(filename: str, field: str, new_value):
            Edits a specific field of an existing record identified by its filename.
        delete_record(filename: str):
            Deletes a metadata record from the collection based on its filename.
    """
    VALID_CATEGORIES = [
        "COVID", "Normal", "Lung_Opacity", "Viral Pneumonia"
    ]

    def __init__(self, category: str, metadata_dir: str):
        if category not in self.VALID_CATEGORIES:
            raise ValueError(f"Invalid category: {category}")
        self.category = category
        self.records = {}
        try:
            self._load_metadata(metadata_dir)
        except FileNotFoundError:
            print(f"Warning: Metadata file not found for category '{category}' in directory '{metadata_dir}'. Starting with an empty record set.")
        except Exception as e:
            print(f"Error loading metadata: {e}")
    
    def _load_metadata(self, metadata_dir: str):
        file_path = f"{metadata_dir}/{self.category}.metadata.xlsx"
        try:
            df = pd.read_excel(file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Metadata file not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading metadata file: {e}")
        df.columns = [col.strip().lower() for col in df.columns]
        for _, row in df.iterrows():
            data = row.to_dict()
            try:
                MetadataValidator.validate(data)
            except ValueError as e:
                print(f"Validation error for record: {data.get('file name', 'Unknown')}. Error: {e}")
                continue  # Skip this record if validation fails
            except ValueError as e:
                print(f"Validation error for record: {data.get('file name', 'Unknown')}. Error: {e}")
                continue  # Salta este registro si hay un error de validación
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
        try:
            MetadataValidator.validate(data)
        except ValueError as e:
            raise ValueError(f"Error adding record: {e}")
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
        try:
            self.records[filename].update_field(field, new_value)
        except Exception as e:
            raise ValueError(f"Error updating field '{field}': {e}")
        except ValueError as e:
            raise ValueError(f"Error updating field '{field}': {e}")  
        
    def delete_record(self, filename: str):
        if filename in self.records:
            del self.records[filename]
