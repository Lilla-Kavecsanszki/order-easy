 #https://stackoverflow.com/questions/74665788/how-to-convert-string-to-number-in-python
 how to convert data into integers and floats 

 https://docs.gspread.org/en/latest/user-guide.html#updating-cells
 How to update cells and work the spreadsheet
 https://docs.gspread.org/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column
 https://stackoverflow.com/questions/14625617/how-to-delete-remove-row-from-the-google-spreadsheet-using-gspread-lib-in-pytho

 https://stackoverflow.com/questions/30989213/can-i-control-the-output-of-insert-row-in-gspread

checking data types
 https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!