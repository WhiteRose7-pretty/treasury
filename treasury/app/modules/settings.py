#
# this is the email used for creating a connection object. You can/should use your own for testing.
#


email_default = "webmaster.b@treasuryquants.com"  # Prod's server 2, master
# email_default = "web.user@treasuryquants.com"  # Prod's
# email_default = "valya.varechkina.76@bk.ru"       # Daria's
# email_default = "test.account@treasuryquants.com" # Shahram's


#
# server's url
#
url_server = "http://operations.treasuryquants.com"
# url_server="http://192.168.1.80:8080" #Shahram's local server


target_url = "http://77.68.119.98/"
# target_url=url_server
# url_server="http://192.168.1.80:8080" #Shahram's local server


# this means set the backend for the dev environment. i.e.
# 1) don't send emails,
# 2) use is_test=True for the api calls
# 3) ... ?
#
is_development = False

#
# Location of the token files
#
token_path = "app/configs/token.json"

api_status_path = "app/configs/api_status.txt"

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
