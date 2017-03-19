import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
gc = gspread.authorize(credentials)

file = gc.open_by_key("1DMv6B8_DLyGfjBlYUT19BTTpyWgKzf5btNvMqQV3eSY")
sheet = file.sheet1

items = sheet.row_values(1)

print(file.title)