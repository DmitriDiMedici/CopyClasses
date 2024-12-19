# CopyClasses Script

This Python script automates the process of backing up Apex classes listed in an Excel file from a master repository folder to a separate backup directory. Follow the instructions below to set up and use the script.

## Prerequisites

### 1. Install Python

Make sure Python is installed on your computer. If you don't have it, you can download and install it from the [official Python website](https://www.python.org/downloads/).

### 2. Install Required Libraries

This script requires the following Python libraries:

- `pandas`
- `openpyxl`

You can install them using pip. Open a terminal or command prompt and run:

```bash
pip install pandas openpyxl
```

## How to Use

### 1. Set Up Your Environment

Make sure you have the following:

- **Excel File**: An Excel.xlsx file containing the list of Apex class names (one name per row in the first column, whose header needs to be named "Class").
- **Master Directory**: The folder containing all the Apex classes.
- **Destination Directory**: A folder where the script will create a backup directory to store the selected Apex classes (and their meta).

### 2. Update the Script with Your Paths

Edit the script to specify the full paths for the following variables:

- `EXCEL_FILE`: The path to your Excel file with the list of class names.
- `MASTER_DIR`: The path to your master repository folder containing the Apex classes.
- `DESTINATION_DIR`: The path to the folder where backups will be created.

Example:

```python
EXCEL_FILE = r"C:\path\to\your\list_of_classes.xlsx"
MASTER_DIR = r"C:\path\to\your\master\folder"
DESTINATION_DIR = r"C:\path\to\your\destination\folder"
```

### 3. Run the Script

Once you have updated the script with the correct paths:

1. Open the script in Visual Studio Code.
2. Click the `Run` button or press `F5` to execute the script.

The script will:

1. Read the Excel file to get the list of class names.
2. Search for these classes in the master folder.
3. Copy the classes found to a `backup` folder inside the destination directory.

### 4. Check the Backup Directory

After running the script, check the destination directory. A new folder named `backup` will be created, containing the copied Apex classes.

## Notes

- Ensure that the Excel file only contains valid class names in the first column. Empty rows or invalid values may cause errors.
- The script will replace any existing `backup` folder in the destination directory.

---

Your time was saved—you're welcome.&#x20;

