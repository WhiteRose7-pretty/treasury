#
# this is the email used for creating a connection object. You can/should use your own for testing.
#
email_default = "web.user@treasuryquants.com" #prod
#email_default = "test.account@treasuryquants.com" #for local testing



#
# server's url
#
url_server = "http://operations.treasuryquants.com"
#url_server="http://192.168.1.80:8080" #Shahram's local server

#
# this means set the backend for the dev environment. i.e. don't send emails etc.
#
is_development=False


#
# Location of the grid files
#
grid_folder = "app/media/currency_data/"

#
# number of decimals to print in the grid.
#
grid_decimals = 4

#
# grid's swap tenors in years
#
grid_swap_tenors = [2, 5, 10, 15, 20, 25, 30, 35]
