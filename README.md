# COVID Image Management CLI

This is an object-oriented Python project designed to manage medical images (based on the COVID-19 Radiography Dataset). It allows downloading the dataset from Kaggle, adding, deleting, listing, and renaming images, as well as managing metadata in a modular and extensible way.

## 📦 Project Structure

```
covid_project/
├── main.py
├── .env.example
├── requirements.txt
├── cli/
│   └── menu.py
├── core/
│   └── images/
│       ├── dataset_utils.py
│       ├── image_manager.py
│       └── image_record.py
└── data/
    └── COVID-19_Radiography_Dataset/
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

You will see an interactive menu:

```
--- COVID Image Management ---
1. Download images from Kaggle
2. Show dataset summary
3. List images by category
4. Add new image
5. Delete image
6. Rename image
7. Exit
```

## 💡 Features

- Download the dataset from Kaggle using `.env` credentials
- Console interface (CLI)
- Modular category management (`COVID`, `NORMAL`, etc.)
- Manual image addition with metadata
- PEP8-compliant code and object-oriented architecture

## 🧪 .env File Example

Store your Kaggle credentials like this:

```
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_api_token
```

---

## ✍️ Author

Ricardo Pari – Final project for the Software Engineering Fundamentals course in Data Science
