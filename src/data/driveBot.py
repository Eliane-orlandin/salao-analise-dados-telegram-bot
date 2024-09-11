import gspread
import json
from os import getenv
import pandas as pd


class driveBot:
    def __init__(self):
        self.gc = gspread.service_account(filename = "credentials.json")

    def get_data(self):
        link_google_sheet = getenv("LINK_SHEET")
        sh = self.gc.open_by_key(link_google_sheet)
        worksheet = sh.sheet1
        dataframe = pd.DataFrame(worksheet.get_all_records(numericise_ignore=['all']))
        dataframe['Valor (R$)'] = pd.to_numeric(dataframe['Valor (R$)'], errors='coerce')
    
        return dataframe