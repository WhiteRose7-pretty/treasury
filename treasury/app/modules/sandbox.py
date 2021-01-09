from TQapis import TQConnection  # version 0.12.4 and above
from app.modules import settings
from app.modules import utility_grids
from app.modules import utility_email
from app.modules import utility_common
from app.modules.apis_for_json import web_api


def test_web_api():
    print(web_api(
        "{\"function_name\":\"connection_is_ok\", \"arguments\":null, \"source_caller\":\"front-end-function1\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_status\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function2\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_create\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"user_ip\":\"127.0.0.1\", \"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function3\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_activation_key_status\", \"arguments\":{\"activation_key\":\"j7v3ffy_uqbggkgt-mstvc_qa1bxyp42vgfvuvj83gyvc-fwdglgla\"}, \"source_caller\":\"front-end-function4\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_send_activation_key\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\",\"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function5\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_send_activation_key\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\",\"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function6\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_password_change\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"new_password\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function7\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_ip_change\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"new_ip\":\"127.0.0.1\"}, \"source_caller\":\"front-end-function8\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_password_reset\", \"arguments\":{\"new_password\":\"test.account@treasuryquants.com\",\"activation_key\":\"j7v3ffy_uqbggkgt-mstvc_qa1bxyp42vgfvuvj83gyvc-fwdglgla\"}, \"source_caller\":\"front-end-function9\"}",
        True))
    print(web_api(
        "{\"function_name\":\"account_profile\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\",\"password\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function10\"}",
        True))


def account_create():
    print(web_api(
        "{\"function_name\":\"account_create\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\","
        "\"user_email\":\"test2.account@treasuryquants.com\",\"user_ip\":\"127.0.0.1\", "
        "\"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function3\"}",
        False))


# todo: Shahram to remove the content once the scheduled grid population is complete.

#
# Usage example for creating fx and swap r#
#
#
# # we need a global (across sessions) connection for all our API calls
# connection = TQConnection.Connection(settings.email_default, settings.url_server)ate grids.


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
