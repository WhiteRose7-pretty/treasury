import socket


def self_ip():
    # collects all the ips associated with this http_server
    ip_list1 = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] \
                if not ip.startswith("127.")]

    ip_list2 = [
        [(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in
         [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]

    ip_list = ip_list1 + ip_list2
    if not ip_list:
        print("IP for this http_server not found")
        return None

    if not len(ip_list) == 1:
        print("More than one found. Here is the list ....")
        print(ip_list)
        return None
    #
    # but returns only one
    #
    return ip_list[0]


#
# this is the email used for creating a connection object. You can/should use your own for testing.
#

email_dictionary = {'77.68.24.21': 'webmaster.b@treasuryquants.com', '77.68.7.117': 'webmaster.b@treasuryquants.com'}

email_default = email_dictionary[self_ip()]  # Prod's server 2, master
# email_default = "webmaster.a@treasuryquants.com"  # Prod's server 2, dev
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
