# 🦠 COVID Image Manager CLI

This project is a modular, object-oriented Python command-line tool for managing **medical images** and their **associated metadata** from the COVID-19 Radiography Dataset.

It includes two independent management systems:
- 📁 Image Management (for handling image files)
- 📊 Metadata Management (for handling metadata stored in `.xlsx` format)

---

## 📦 Project Structure

```
covid-image-manager/
├── cli/                     # Main CLI interfaces
│   ├── menu.py              # Main menu entry point
│   ├── image_menu.py        # Submenu for image CRUD operations
│   └── metadata_menu.py     # Submenu for metadata CRUD operations
│
├── core/                    # Business logic
│   ├── images/
│   │   ├── image_manager.py
│   │   ├── dataset_utils.py
│   │   └── image_record.py
│   └── metadata/
│       ├── metadata_manager.py
│       ├── metadata_record.py
│       └── metadata_validator.py
│
├── metadata/                # Metadata files (.xlsx) by category
│   ├── COVID.metadata.xlsx
│   ├── Normal.metadata.xlsx
│   ├── Lung_Opacity.metadata.xlsx
│   └── Viral Pneumonia.metadata.xlsx
│
├── data/                    # Image dataset (if used directly)
├── .env.example             # Example environment variables
├── requirements.txt         # Python dependencies
└── main.py                  # Optional entry point
```

## ⚙️ Requirements

- Python 3.7 or higher
- Virtual environment (optional but recommended)

## 📥 Installation

```bash
# Clone or extract the project
cd covid_project

# Create a virtual environment
python3 -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure your Kaggle credentials
cp .env.example .env
# Then edit .env with your Kaggle username and API key
```

## ▶️ Execution

```bash
python3 main.py
```

---

## 🚀 Features

### 🖼 Image Management (`cli/image_menu.py`)
- List images by category
- Add new images from a source path
- Delete images from a category

### 📑 Metadata Management (`cli/metadata_menu.py`)
- Load all `.xlsx` metadata files into memory
- List metadata records by category
- Add, edit, and delete records in-memory (non-persistent)
- Smart handling of `size` values like `"256*256"`

---
## 🧪 .env File Example

Store your Kaggle credentials like this:

```
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_api_token
```

---

## ✍️ Author

Ricardo Pari – Final project for the Software Engineering Fundamentals course in Data Science
