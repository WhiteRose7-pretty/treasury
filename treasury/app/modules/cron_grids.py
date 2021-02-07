from app.modules import settings
from app.modules import utility_grids
from app.modules import utility_common
from app.modules import utility_connection
from app.modules.apis_for_json import api_gateway
import json

# we need a global (across sessions) connection for all our API calls
connection = utility_connection.WebConnection(settings.email_default, settings.url_server, settings.token_path)


def download_fx_data():
    (status, results) = utility_grids.utility_download_formatted_grid_fx(
        ['USD', 'GBP', 'EUR', 'CHF', 'JPY', 'CAD', 'AUD', 'SGD', 'NZD'], "USD", settings.grid_folder)
    if not status:
        # Do Failure
        utility_common.process_fatal_error("download_fx_data", utility_common.dict_to_string(results),
                                           settings.is_development)
    return status


def download_rates_data():
    (status, results) = utility_grids.utility_download_formatted_grid_swap_rates(connection,
                                                                                 ['USD', 'GBP', 'CHF', 'EUR', 'JPY'],
                                                                                 settings.grid_swap_tenors,
                                                                                 settings.grid_folder)
    if not status:
        # Do Failure
        utility_common.process_fatal_error("download_rates_data", utility_common.dict_to_string(results),
                                           settings.is_development)
    return status, results


def check_connection():
    res = api_gateway(
        "{\"function_name\":\"connection_is_ok\", \"arguments\":{}, \"source_caller\":\"some_caller\"}")
    res_dic = json.loads(res)
    print(res)
    # if backend server is offline, error = ''
    error = res_dic['error']
    if error:
        status = False
        utility_common.process_fatal_error("check_connection", error, settings.is_development)
    elif not res_dic['results']:
        status = False
        error = 'it is not connected with backend'
    else:
        status = True

    api_status_to_file(settings.api_status_path, status)

    return status, error


def api_status_from_file(path):
    with open(path, 'rt') as file:
        content = file.read()
    if content == "True":
        return True
    else:
        return False


def api_status_to_file(path, status):
    file = open(path, 'w')
    file.writelines(str(status))
