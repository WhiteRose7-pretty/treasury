from TQapis import  TQConnection  # version 0.12.2 and above
import settings
from utility_grids import utility_download_formatted_grid_swap_rates, utility_download_formatted_grid_fx
from utility_email import send_email
from utility_common import dict_to_string
#
# Usage example
#




# we need a global (across sessions) connection for all our API calls
connection = TQConnection.Connection(settings.email_default,settings.url_server)



(status, results) = utility_download_formatted_grid_swap_rates(connection, ['USD', 'GBP', 'CHF', 'EUR', 'JPY'], settings.grid_folder)
if not status:
    # Do Failure
    send_email("operations@treasuryquants.com","web cron error",dict_to_string(results) )
else:
    # Do success
    print (status,results)

(status, results) = utility_download_formatted_grid_fx(['USD', 'GBP', 'CHF', 'EUR', 'JPY', 'AUD', 'SGD', 'NZD'],"USD", settings.grid_folder)
if not status:
    # Do Failure
    send_email("operations@treasuryquants.com","web cron error",dict_to_string(results) )
else:
    # Do success
    print (status,results)
