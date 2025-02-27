from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account key file
SERVICE_ACCOUNT_FILE = '/Users/admin/zincs-for-boats-gbt-b08832ad2486.json'

# Define the required scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Create credentials using the service account key file
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Sheets API client
service = build('sheets', 'v4', credentials=credentials)

# Define the spreadsheet ID and range
spreadsheet_id = '10G1VnYmuWXwQvmT9eedZMNQ7g9SiKP7KiFS_NxTQ-PY'
range_name = 'products.csv!A1:B'

# Call the Sheets API
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range=range_name
).execute()

values = result.get('values', [])

if not values:
    print('No data found.')
else:
    for row in values:
        print(row)

