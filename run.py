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

def get_wine_product_list():
    """
    Get the product list printed (wines) - option 1
    """
    print('Collecting data...\n')
    wine_list = wines.col_values(1)
    for product in range(len(wine_list)):
        print(wine_list[product])

    x = wine_list[product]

def get_new_product():
    """
    Get new product details input from the user,
    running a while loop, to get a valid string of data, which must be a string of 4 details separeted by 
    commas. The loop will keep repeating the request until gets the valid data
    option 2
    """
    while True:

        print("Please enter the details of the new product.") 
        print("Data should contain 4 details, separated by commas: Name,Unit,Price,Par level")
        print("Examlpe: Campari,Bottle,£14.26,18\n")

        data_str = input("Enter the new product details here:\n")

        new_product = data_str.split(",")
        print(new_product)
        
        if validate_data_add_product(new_product):
            print("Data for new product is valid")
            break

    return new_product


def validate_data_add_product(values):
    '''
    Validates the list of user input for the new product
    option 2
    '''
    print('Validating input details...\n')
       
    try: 
        if len(values) != 4:  #check the number of details matches the number required
            raise ValueError(f"Exactly 4 details required, you provided {len(values)}.")
    
        if not isinstance(int(values[3]), int):    #validate the par level (integer)
            raise ValueError("Par level must be an integer")
    
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

# new_product_data = get_new_product()

def add_new_product(new_product_data):
    '''
    Updates the worksheet with the details of the new product - option 2
    '''
    print("Updating wines stocksheet...\n")
    wines = SHEET.worksheet('wines')
    wines.append_row(new_product_data)
    
    print("Wines stocksheet updated successfully.\n")

# add_new_product(new_product_data)

def option2():
    """
    Run all program functions for option 2
    """
    new_product_data = get_new_product()
    add_new_product(new_product_data)

#Delete a product
def get_deleted_product():
    """
    Get deleted product details input from the user,
    running a while loop, to get a valid string of data, which must be a string of 1 value. The loop will keep repeating 
    the request until gets the valid data
    option 3
    """
    while True:

        print("Please enter the name of the product, that you wish to delete.") 
        print("Data should contain 1 value, the name.")
        print("Examlpe: Campari\n")

        deleting_product = input("Enter the name of the product here:\n")

        if validate_data_delete_product(deleting_product):
            print("Data for deleted product is valid")
            break

    return deleting_product


def validate_data_delete_product(values):
    '''
    Validates the list of user input for the deleted product - option 3
    '''
    print('Validating input details...\n')
       
    try: 
        if len(values) < 2:  #check the number of details matches the number required
            raise ValueError(f"Exactly 1 product name required, you provided {len(values)} details.")
    
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def delete_product(deleted_product_data):
    '''
    Finds the cell that is matching with the validated user input, than updates the worksheet based on that. Deletes the 
    entire row
    option 3
    '''
    print("Deleting product on wines stocksheet...\n")

    cell = wines.find(deleted_product_data)
    wines.delete_rows(cell.row)

    print("Wines stocksheet updated successfully.\n")

def option3():
    """
    Run all program functions for option 2
    """
    deleted_product_data = get_deleted_product()
    delete_product(deleted_product_data)


#wines
def get_current_stocks_data():
    """
    Get current stock holoding figures input from the user,
    running a while loop, to get a valid string of data, which must be a string of 6 whole or float numbers separeted by 
    commas. The loop will keep repeating the request until gets the valid data
    option 4
    """
    while True:

        print("Please enter current stock data.") 
        print("Data should be 7 numbers, separated by commas.")
        print("Examlpe: 12,23,34,36,46,37,49\n")

        data_str = input("Enter your numbers here:\n")

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
    option 4
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
    '''
    Updates the date to show today's date each times the user inputs a new entry - option 4
    '''
    wines_countsheet = SHEET.worksheet('wines')
    the_date = datetime.now().date()
    
    x = f'Current Stock Holding {the_date}'
    wines_countsheet.update_cell(1, 5, x)
    print(x)

def update_stocks_countsheet(data):
    """
    Update stocks worksheet, add new column with the list of data provided - option 4
    """
    print("Updating stocks countsheet...\n")
    wines_countsheet = SHEET.worksheet('wines')

   # stock_column = wines_countsheet.col_values(5)
   # stock_column.pop(0)

    for ind in range(len(data)):
        wines_countsheet.update_cell(ind+2, 5, data[ind])

    print("Wine stocks countsheet updated successfully.\n")
    

def update_order_list_sheet(new_order_amount_counts):
    """
    Update order amounts on the worksheet, add new column with the list of new order amount counts calculated
    option 4
    """
    print("Updating order list...\n")
    wines_order = SHEET.worksheet('wines')
    
    for amount in range(len(new_order_amount_counts)):
        wines_order.update_cell(amount+2, 6, new_order_amount_counts[amount])

    print("Order list updated successfully.\n")   

def howmuch_to_order(current_stocks_data_column):
    """
    Calculate the order list by minusing the current stock holding number from the par level number. The par level indicates how 
    much of the certain product we should have. We need to order the difference. If we got a minus number as our result, that means
    we have too many of the noted product on stock and no need to order.
    option 4
    """
    print("Collecting order list...\n")

    par_level = wines.col_values(4)
    par_level.pop(0)
    
    order_amount_counts = []
    for par, stock in zip(par_level, current_stocks_data_column):
        order_amount = int(par) - stock
        order_amount_counts.append(order_amount)
    return order_amount_counts

def print_order_list_wines():
    """
    Printing out the list of products and relevantly their information that indicates how much the user needs to order 
    (wines) - option 4
    """
    print("Collecting order list and details...\n")

    wine_order = wines.get_all_values()

    for item in range(len(wine_order)):
        print(wine_order[item])

    x = wine_order[item]

def get_the_order_list_wines():
    """
    Run all program functions for option 4
    """

    data = get_current_stocks_data()
    current_stocks_data = [int(num) if num.isdigit() else float(num)for num in data]
    update_stocks_countsheet(current_stocks_data)
    show_date()  #show current date when update the stock levels
    new_order_amount_counts = howmuch_to_order(current_stocks_data)
    update_order_list_sheet(new_order_amount_counts)
    print_order_list_wines()

# get_the_order_list_wines()


#https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/?utm_content=cmp-true
 
menu_options = {
    1: 'Print Product List',
    2: 'Add New Product',
    3: 'Delete Product',
    4: 'Get the Order List',
    5: 'Back to the main menu'
}

def print_menu():
    """
    Asks the user to select what they would like to do. Keep repeating until the user decides to go back to the main menu.
    """
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

print('\nSub-Menu - OrderEasy Application:\n')
print('Please select what you would like to do by entering a number between 1 and 5\n')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('\nEnter your number here:\n'))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           get_wine_product_list()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            get_the_order_list_wines()
        elif option == 5:
            print('Thank You, Goodbye!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 5.')

'''
menu_options = {
    1: 'Spirits',
    2: 'Wines',
    3: 'Beers',
    4: 'Soft Drinks',
    5: 'Exit'
}
# def menu():
    """
    First contact with the user, asks the user to select what they would like to do. Keep repeating until the 
    user decides to exit.
    """
        
# menu()
'''