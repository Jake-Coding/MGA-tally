import tally_logic
# [START sheets_quickstart]
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
ID = '1LLqkFhWBiNKbcoiL60iYnr5VsZ-Qlq7oW2UWBgPTWmI'
RANGE = 'Sheet1!A1:G1000'
basic_info = {"ID": ID, "RANGE": RANGE}

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string


def get_spreadsheet():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service

def append(values : dict, info : dict, sheet):
    body = {
        "values" : values
    }
    sheet.values().append(spreadsheetId = info["ID"],range = info["RANGE"], body = body, valueInputOption = "USER_ENTERED").execute()


def get_data(info : dict, sheet):
    result = sheet.values().get(
    spreadsheetId=info["ID"], range=info["RANGE"]).execute()
    rows = result.get('values', [])

    return rows

def main():

    service = get_spreadsheet()
    # Call the Sheets API
    sheet = service.spreadsheets()
    # result = sheet.values().get(spreadsheetId=ID,range=RANGE).execute()
    # values = result.get('values', [])
    test_append_values = [ ["CaWU", "4", "US West"]    ]
    append(test_append_values, {"ID": ID, "RANGE": RANGE}, sheet)
    # if not values:
    #     print('No data found.')
    # else:
    #     print('Val:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print(row[0])

if __name__ == '__main__':
    main()
# [END sheets_quickstart]