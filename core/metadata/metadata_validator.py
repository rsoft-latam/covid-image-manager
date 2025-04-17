class MetadataValidator:
    @staticmethod
    def validate(record: dict):
        # Validate the presence and type of 'file name'
        if "file name" not in record or not isinstance(record["file name"], str):
            raise ValueError("Invalid or missing 'file name'")

        # Validate the presence and type of 'format'
        if "format" not in record or not isinstance(record["format"], str):
            raise ValueError("Invalid or missing 'format'")

        # Validate the presence of 'size'
        if "size" not in record:
            raise ValueError("Missing 'size'")

        size_value = record["size"]
        try:
            # Try to convert the size directly to a float
            float(size_value)
        except:
            # If conversion fails, attempt to interpret a string format like "256*256"
            if isinstance(size_value, str) and "*" in size_value:
                parts = size_value.split("*")
                # Ensure both parts are numeric strings
                if all(p.strip().isdigit() for p in parts):
                    # Convert to a numeric value by multiplying width * height
                    record["size"] = int(parts[0]) * int(parts[1])
                else:
                    raise ValueError("Invalid 'size' format")
            else:
                raise ValueError("Invalid 'size' value")

        # Validate the presence and type of 'url'
        if "url" not in record or not isinstance(record["url"], str):
            raise ValueError("Invalid or missing 'url'")
