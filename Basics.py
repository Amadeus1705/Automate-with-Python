import gspread
from google.oauth2.service_account import Credentials
from gspread_formatting import *

# Scopes are the operations you can do when you are accessing files,documents using the api
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

# Client that can access different sheets
client = gspread.authorize(creds)

sheet_id = '1vTyB0C8Trn-F0gqVs6l27G9M9Id4Fqp1cm4EanTlwBM'

# There are multiple ways to do this, but we are using the key as it is the more fullproof method
workbook = client.open_by_key(sheet_id)

# Checks if the sheet is connected
try:
    values_list = workbook.sheet1.row_values(1)
    print(values_list)
except Exception as e:
    print("Error in Connecting to the workbook")

# A few basic operations
sheets = map(lambda x:x.title,workbook.worksheets())
print(list(sheets))

sheet = workbook.worksheet('Sheet1')

# sheet.update_title("Hello")
# print("Title updated")

# Add a cell based on numeric values
sheet.update_cell(1,1,"Hi this is changed")

# Get the value of a cell
# value = sheet.cell(1,1).value
# print(value)

# cell = sheet.find("I feel great")
# print(f"The cell value is {cell.row},{cell.col}")

# Formatting

# Specify cell or range of cells
sheet.format("A1",{
    "textFormat":{"bold":True}
})

# Sample Gspread formatting
fmt = cellFormat(
    backgroundColor=color(1, 0.9, 0.9),
    textFormat=textFormat(bold=True, foregroundColor=color(1, 0, 1)),
    horizontalAlignment='CENTER'
    )

format_cell_range(sheet, 'A1:J1', fmt)



# Things to add in readme, learned from techwithTim, 
# Using the gspread documentation to learn more
# Find attached the link to the test sheet
# I have removed my credentials to the main account