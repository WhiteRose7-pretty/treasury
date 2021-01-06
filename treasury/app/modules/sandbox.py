from TQapis import TQConnection  # version 0.12.4 and above
from app.modules import settings
from app.modules import utility_grids
from app.modules import utility_email
from app.modules import utility_common

# todo: Shahram to remove the content once the scheduled grid population is complete.

#
# Usage example for creating fx and swap rate grids.
#


# we need a global (across sessions) connection for all our API calls
connection = TQConnection.Connection(settings.email_default, settings.url_server)


def download_fx_data():
    (status, results) = utility_grids.utility_download_formatted_grid_swap_rates(connection,
                                                                                 ['USD', 'GBP', 'CHF', 'EUR', 'JPY'],
                                                                                 settings.grid_swap_tenors,
                                                                                 settings.grid_folder)

    if not status:
        # Do Failure
        print(status, results)
        # utility_email.send_email("operations@treasuryquants.com", "web cron error",
        #                          utility_common.dict_to_string(results))
    else:
        # Do success
        print(status, results)

    (status, results) = utility_grids.utility_download_formatted_grid_fx(
        ['USD', 'GBP', 'CHF', 'EUR', 'JPY', 'AUD', 'SGD', 'NZD'], "USD", settings.grid_folder)
    if not status:
        # Do Failure
        print(status, results)
        # utility_email.send_email("operations@treasuryquants.com", "web cron error",
        #                          utility_common.dict_to_string(results))
    else:
        # Do success
        print(status, results)

    return status
