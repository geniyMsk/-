import httplib2
import apiclient
from config import spreadsheetId
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'XXX.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)




def input():
    ranges = ["Input!A2:G1000"]
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    result = results['valueRanges'][0]['values']
    return result


def clean_sheet(range):
    service.spreadsheets().values().clear(spreadsheetId=spreadsheetId, range=range,
                                          body={}).execute()

def output(n, name, username, num1, num2):
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId,
        body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": f"Output!A{n}:D{n}",
             "majorDimension": "ROWS",
             "values": [
                 [name, username,num1, num2]
             ]}
        ]
    }).execute()

def messages_man():
    ranges = ["Сообщения!F2:F18"]
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    result = results['valueRanges'][0]['values']
    return result

def messages_woman():
    ranges = ["Сообщения!G2:G18"]
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    result = results['valueRanges'][0]['values']
    return result








