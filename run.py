import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('order_spreadsheet')

spirits = SHEET.worksheet('spirits')
wines = SHEET.worksheet('wines')
beers = SHEET.worksheet('beers')
soft_drinks = SHEET.worksheet('soft_drinks')

spirit_stock = spirits.get_all_values()
wine_stock = wines.get_all_values()
beer_stock = beers.get_all_values()
soft_drink_stock= soft_drinks.get_all_values()

#wines
def get_current_stocks_data():
    """
    Get current stock holoding figures input from the user
    """
    while True:

        print("Please enter current stock data.") 
        print("Data should be 7 numbers, separated by commas.")
        print("Examlpe: 12,23,34,36,46,37,49\n")

        data_str = input("Enter your numbers here: ")

        current_stock = data_str.split(",")
        
        if validate_data(current_stock):
            print("Data is valid")
            break

    return current_stock
        
def validate_data(values):
    """
    Inside the try, make sure all the string values are numbers, 
    raises ValueError, if strings are not numbers, 
    or if there are not exactly 7 values
    """

    #https://stackoverflow.com/questions/74665788/how-to-convert-string-to-number-in-python
    try:
        [int(value) if value.isdigit() else float(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 numbers required, you provided {len(values)}. If an item has run out completely, put 0")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


data = get_current_stocks_data()