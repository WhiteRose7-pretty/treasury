from TQapis import TQRequests
from . import utility_common


# All functions below return
# 1) status[Boolean] - was the call successful?
# 2) results[dictionary] - a dictionary of the results if status=True, a dictionary of the errors if status =False

def make_results(message, connection):
    if not message.is_OK:
        return [message.is_OK, connection.response.errors]
    else:
        return [message.is_OK, connection.response.results]


def connection_is_ok(connection):
    #
    # Check if we have connections
    #
    request_ip_return = TQRequests.request_ip_return()
    message = connection.send_web(request_ip_return)
    return make_results(message, connection)


def account_status(connection, user_email):
    #
    # check the status of the account
    #
    request_account_create = TQRequests.request_account_status(user_email)
    message = connection.send_web(request_account_create)
    return make_results(message, connection)


def account_create(connection, user_email, user_password, user_ip, callback_url, is_test):
    #
    # Creates a  account
    #
    request_account_create = TQRequests.request_account_create(user_email, user_password, user_ip, callback_url,
                                                               is_test)
    message = connection.send_web(request_account_create)
    return make_results(message, connection)


def account_activation_key_status(connection, activation_key):
    #
    # Activates a  (disabled) account
    #
    request_account_activation_key_status = TQRequests.request_account_activation_key_status(activation_key)
    message = connection.send_web(request_account_activation_key_status)
    return make_results(message, connection)


def account_activate(connection,  activation_key, is_test):
    #
    # Activates a  (disabled) account
    #
    request_account_activate = TQRequests.request_account_activate(activation_key, is_test)
    message = connection.send_web(request_account_activate)
    return make_results(message, connection)


def account_send_activation_key(connection, user_email, callback_url, is_test):
    #
    # sends (resends) activation key
    #
    request_account_send_activation_key = TQRequests.request_account_send_activation_key(user_email, callback_url,
                                                                                         is_test)
    message = connection.send_web(request_account_send_activation_key)
    return make_results(message, connection)


def account_token_generate(connection, email):
    #
    # sends (resends) activation key
    #
    request_account_token_create = TQRequests.request_account_token_create(email)
    message = connection.send_web(request_account_token_create)
    return make_results(message, connection)


def account_password_change(connection,user_email, password, new_password, is_test):
    #
    # Changes the existing password
    #
    request_account_password_change = TQRequests.request_account_password_change(user_email, password, new_password,
                                                                                 is_test)
    message = connection.send_web(request_account_password_change)
    return make_results(message, connection)


def account_ip_change(connection,user_email, password, _ip, is_test):
    #
    # Changes the registered IP
    #
    request_account_ip_change = TQRequests.request_account_ip_change(user_email, password, _ip, is_test)
    message = connection.send_web(request_account_ip_change)
    return make_results(message, connection)


def account_password_reset(connection,  activation_key, new_password, is_test):
    #
    # Changes/resets the password
    #
    request_account_password_reset_dict = TQRequests.request_account_password_reset(activation_key,
                                                                                    new_password,
                                                                                    is_test)
    message = connection.send_web(request_account_password_reset_dict)
    return make_results(message, connection)


def account_password_ip_change(connection, user_email, password, new_password, new_ip, is_test):
    #
    # Changes password and IP at the same time
    #
    request_account_password_ip_change = TQRequests.request_account_password_ip_change(user_email, password,
                                                                                       new_password, new_ip,is_test)
    message = connection.send_web(request_account_password_ip_change)
    return make_results(message, connection)



def account_profile(connection, user_email, password):
    #
    # Changes/resets the password
    #
    request_account_profile_dict = TQRequests.request_account_profile(user_email, password)
    message = connection.send_web(request_account_profile_dict)
    return make_results(message, connection)

def formatted_grid_swap_rates(connection, from_date, to_date,currency, tenors):
    #
    # Creates a grid of swap rates
    #
    request_formatted_grid_swap_rates = TQRequests.request_function_formatted_grid_swap_rates(from_date,
                                                                                              to_date, currency)
    # todo: Shahram to remove below after TQapis version 0.12.5
    if 'tenors' not in request_formatted_grid_swap_rates.params:
        request_formatted_grid_swap_rates.params['tenors'] = utility_common.list_to_csv(tenors)
    # end todo

    message = connection.send(request_formatted_grid_swap_rates)
    return make_results(message, connection)




def describe(connection, user_email, element=''):

    request_function_describe = TQRequests.request_function_describe(element)
    request_function_describe.params['email']=user_email
    message = connection.send_web(request_function_describe)
    return make_results(message, connection)

def show_available(connection, user_email, element=''):
    request_function_show_available = TQRequests.request_function_show_available(element)
    request_function_show_available.params['email']=user_email
    message = connection.send_web(request_function_show_available)
    return make_results(message, connection)

def pnl_attribute(connection, user_email,load_as, from_date, to_date):
    request_function_pnl_attribute = TQRequests.request_function_pnl_attribute(load_as, from_date, to_date)
    request_function_pnl_attribute.params['email']=user_email
    message = connection.send_web(request_function_pnl_attribute)
    return make_results(message, connection)


def pnl_predict(connection, user_email,load_as, from_date, to_date):
    request_function_pnl_predict = TQRequests.request_function_pnl_predict(load_as, from_date, to_date)
    request_function_pnl_predict.params['email']=user_email
    message = connection.send_web(request_function_pnl_predict)
    return make_results(message, connection)

def risk_ladder(connection, user_email,asOf, load_as):
    request_function_risk_ladder = TQRequests.request_function_risk_ladder(asOf, load_as)
    request_function_risk_ladder.params['email']=user_email
    message = connection.send_web(request_function_risk_ladder)
    return make_results(message, connection)

def price(connection, user_email,asOf, load_as):
    request_function_price = TQRequests.request_function_price(asOf, load_as)
    request_function_price.params['email']=user_email
    message = connection.send_web(request_function_price)
    return make_results(message, connection)


def workspace(connection, user_email,list='', delete=''):
    request_function_workspace = TQRequests.request_function_workspace_show_files()
    if delete!='':
        request_function_workspace = TQRequests.request_function_workspace_delete_file(delete)
    request_function_workspace.params['email']=user_email
    message = connection.send_web(request_function_workspace)
    return make_results(message, connection)



def price_vanilla_swap(
                connection
                , user_email
                , asof
                , type
                , notional
                , trade_date
                , trade_maturity
                , index_id
                , discount_id
                , floating_leg_period
                , fixed_leg_period
                , floating_leg_daycount
                , fixed_leg_daycount
                , fixed_rate
                , is_payer
                , spread
                , business_day_rule
                , business_centres
                , spot_lag_days
                , save_as=""):
    request_function_price_vanilla_swap = TQRequests.request_function_price_vanilla_swap(asof
                , type
                , notional
                , trade_date
                , trade_maturity
                , index_id
                , discount_id
                , floating_leg_period
                , fixed_leg_period
                , floating_leg_daycount
                , fixed_leg_daycount
                , fixed_rate
                , is_payer
                , spread
                , business_day_rule
                , business_centres
                , spot_lag_days
                , save_as)
    request_function_price_vanilla_swap.params['email']=user_email
    message = connection.send_web(request_function_price_vanilla_swap)
    return make_results(message, connection)

def price_fx_forward(connection
                , user_email
                , asof
                , type
                , trade_date
                , trade_expiry
                , pay_amount
                , pay_currency
                , receive_amount
                , receive_currency
                , save_as=""):
    request_function_price_fx_forward = TQRequests.request_function_price_fx_forward(asof
                , type
                , trade_date
                , trade_expiry
                , pay_amount
                , pay_currency
                , receive_amount
                , receive_currency
                , save_as)
    request_function_price_fx_forward.params['email']=user_email
    message = connection.send_web(request_function_price_fx_forward)
    return make_results(message, connection)


def market_swap_rates(connection, user_email,asof, currency):
    request_function_market_swap_rates = TQRequests.request_function_market_swap_rates(asof, currency)
    request_function_market_swap_rates.params['email']=user_email
    message = connection.send_web(request_function_market_swap_rates)
    return make_results(message, connection)


def market_fx_rates(connection, user_email,base_date,to_date,base_currency):
    request_function_market_fx_rates = TQRequests.request_function_market_fx_rates(base_date,to_date,base_currency)
    request_function_market_fx_rates.params['email'] = user_email
    message = connection.send_web(request_function_market_fx_rates)
    return make_results(message, connection)
