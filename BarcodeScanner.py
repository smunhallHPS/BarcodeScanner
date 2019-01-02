"""
Author: Sam Munhall
Date:   12/20/2018
Env:    Win7, PyCharm CE, Python 3.7.1

This program is intended to read data from a USB barcode scanner and send it to a Google sheet.

"""

# IMPORTS:
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('creds.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("BarcodeData").sheet1 # open sheet
row = 1

while True:
    data = input("Please scan your barcode")
    if data != "":
        sheet.update_cell(row, 1, data)
        row = row+1

# END OF PROGRAM
