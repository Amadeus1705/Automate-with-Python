## Automating Google Sheets with Python

This project demonstrates how to automate tasks in Google Sheets using Python, the gspread library, and Google's API.

### Getting Started

Follow the tutorial by [Tech With Tim](https://www.youtube.com/watch?v=zCEJurLGFRk&ab_channel=TechWithTim) to set up your Google Sheets automation project.

1. **Set Up Your Service Account**:
   - Create a Google Cloud Project: Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
   - Enable the Google Sheets API: Within your project, enable the Google Sheets API.
   - Create a Service Account: Generate a service account key and download the `credentials.json` file. Place this file in the same directory as your Python scripts.

2. **Install Dependencies**:
   - Make sure you have Python installed.
   - Create a virtual environment (recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

### Project Structure

- `basics.py`: Contains examples of basic operations like reading/writing cell values, formatting, and finding cells. Use this as a reference to learn the core gspread functions.
- `main.py`: Your main script where you'll write your custom automation logic. Replace the placeholder `sheet_id` with the ID of your own Google Sheet.
- `requirements.txt`: Lists the project dependencies.

### Additional Resources

- [gspread Documentation](https://gspread.readthedocs.io/en/latest/)
- [gspread Formatting Documentation](https://github.com/robin900/gspread-formatting)

### Basic Operations Example

Here's a brief example from `basics.py` showing how to read cell values and update a cell:

```python
# ... (authentication and sheet setup code) ...

sheet = workbook.worksheet('Sheet1')  # Select the sheet you want to work with

values_list = sheet.row_values(1)   # Get values from the first row
print("Values in the first row:", values_list)

sheet.update_cell(1, 1, "This cell has been updated!")  # Update a cell's value
```

### Tips and Troubleshooting

- **Double-Check Credentials**: Ensure your `credentials.json` file is valid and has the correct permissions.
- **Share Your Sheet**: The service account email associated with your credentials needs edit access to your Google Sheet.

### Sources

- [Stack Overflow](https://stackoverflow.com/questions/76827026/how-to-read-google-sheet-using-google-sheet-url-and-google-auth-login-in-python)
- [GitHub Repository](https://github.com/esenthil2018/ML_API)

---
