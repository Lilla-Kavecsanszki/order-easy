import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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

#to get all the products printed (wines)
def get_wine_product_list():
    wine_list = wines.col_values(1)
    for item in range(len(wine_list)):
        print(wine_list[item])

    x = wine_list[item]




#wines
def get_current_stocks_data():
    """
    Get current stock holoding figures input from the user,
    running a while loop, to get a valid string of data, which must be a string of 6 whole or float numbers separeted by 
    commas. The loop will keep repeating the request until gets the valid data
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

def show_date():
    wines_countsheet = SHEET.worksheet('wines')
    the_date = datetime.now().date()
    
    x = f'Current Stock Holding {the_date}'
    wines_countsheet.update_cell(1, 5, x)
    print(x)




def update_stocks_countsheet(data):
    """
    Update stocks worksheet, add new column with the list of data provided
    """
    print("Updating stocks countsheet...\n")
    wines_countsheet = SHEET.worksheet('wines')
    
    for count in range(len(current_stocks_data)):
        print(current_stocks_data[count])

    x = current_stocks_data[count]

    wines_countsheet.update_cell(2, 5, x)
    print("Wine stocks countsheet updated successfully.\n")   

def main():
    """
    Run all program functions
    """

data = get_current_stocks_data()
current_stocks_data = [int(num) if num.isdigit() else float(num)for num in data]
update_stocks_countsheet(current_stocks_data)
get_wine_product_list()
show_date() #show only when update the stock levels

main()
