
from app.modules import settings
from app.modules import utility_grids
from app.modules import utility_common
from app.modules import utility_connection

# we need a global (across sessions) connection for all our API calls
connection = utility_connection.WebConnection(settings.email_default, settings.url_server, settings.token_path)


def download_fx_data():
    (status, results) = utility_grids.utility_download_formatted_grid_fx(
        ['USD', 'GBP', 'CHF', 'EUR', 'JPY', 'AUD', 'SGD', 'NZD'], "USD", settings.grid_folder)
    if not status:
        # Do Failure
        utility_common.process_fata_error(utility_common.dict_to_string(results),settings.is_development)
    return status


def download_rates_data():
    (status, results) = utility_grids.utility_download_formatted_grid_swap_rates(connection,
                                                                                 ['USD', 'GBP', 'CHF', 'EUR', 'JPY'],
                                                                                 settings.grid_swap_tenors,
                                                                                 settings.grid_folder)
    if not status:
        # Do Failure
        utility_common.process_fata_error(utility_common.dict_to_string(results),settings.is_development)
    return status



# print(download_fx_data())
# print(download_rates_data())

