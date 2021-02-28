# Configuration Parameter list for API server interface


# this is the email where the errors are sent
email_webmaster = 'valya.varechkina.76@bk.ru'

# email dictionary with IP where the website's own account is registered with api server
email_dictionary = {'77.68.24.21': 'webmaster.b@treasuryquants.com', '77.68.7.117': 'webmaster.a@treasuryquants.com'}

master_ip = '' \
            '' \
            ''
dev_ip = '77.68.7.117'

email_default = email_dictionary[dev_ip]

# Prod's server 2, master
# email_default = "webmaster.a@treasuryquants.com"  # Prod's server 2, dev
# email_default = "web.user@treasuryquants.com"  # Prod's
# email_default = "valya.varechkina.76@bk.ru"       # Daria's
# email_default = "test.account@treasuryquants.com" # Shahram's


# server's url
url_server = "http://operations.treasuryquants.com"
#url_server="http://192.168.1.80:8080" #Shahram's local server


target_url = "http://77.68.119.98/"
#target_url=url_server


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

path_error_file = "app/configs/errors.json"

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
