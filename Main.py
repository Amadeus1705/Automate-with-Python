import gspread
from google.oauth2.service_account import Credentials
from gspread_formatting import *

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = '1vTyB0C8Trn-F0gqVs6l27G9M9Id4Fqp1cm4EanTlwBM'

workbook = client.open_by_key(sheet_id)

vals = [["Name","Score","Rank"],
        ["Sharon",92,1],
        ["John",88,2],
        ["Jane",84,3],
        ["Jerry",72,4]
        ]

worksheet_list = map(lambda x: x.title,workbook.worksheets())
name = 'Scores'

if name in worksheet_list:
    sheet = workbook.worksheet(name)
else:
    sheet = workbook.add_worksheet(name,rows=100,cols=100)
    
sheet.clear()
sheet.update(f"A1:C{(len(vals))}",vals)

sheet.format("A1:C1",{
    "textFormat":{"bold":True}
})

sheet.update_cell(len(vals)+1,2,"=sum(B2:B5)")
sheet.update_cell(len(vals)+1,3,"=average(C2:C5)")