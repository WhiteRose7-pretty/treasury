import app.modules.apis as apis
import app.modules.settings as settings
import app.modules.utility_common as utility_common
import app.modules.utility_connection as utility_connection

import json


#
# this factory is to support the front end by receiving jason request and returning a json response.
#


class WebRequest:
    def __init__(self):
        self.function_name = ""
        self.arguments = dict()
        self.source_caller = ""

    def from_string(self, string_json):

        try:
            request = json.loads(string_json)
            if 'function_name' not in request:
                return False, "key 'function_name' is missing"
            if 'arguments' not in request:
                return False, "key 'arguments' is missing"
            if 'source_caller' not in request:
                return False, "key 'source_caller' is missing"

            self.function_name = request['function_name'].strip()
            self.arguments = request['arguments']
            self.source_caller = request['source_caller'].strip()

            if len(self.function_name) == 0:
                return False, "key 'function_name' has no value"
            if len(self.source_caller) == 0:
                return False, "key 'source_caller' has no value"

            return True, ''
        except Exception as e:
            raise Exception("WebRequest.from_string:" + str(e))


class WebResponse:
    def __init__(self):
        self.results = dict()
        self.error = ""
        self.source_caller = ''

    def to_string(self):
        response = dict()
        # backend server disconnected
        if not self.error and not self.results:
            self.error = 'There is not internet connection with backend server.'
        response['error'] = self.error
        response['results'] = self.results
        response['source_caller'] = self.source_caller
        return json.dumps(response)


class functionCall:
    def __init__(self, name):
        self.name = name

    def is_valid(self, web_request):
        pass

    def call(self, connection, is_test):
        pass

    def create_new(self):
        pass

    def _make_response(self, status, results):
        web_response = WebResponse()
        web_response.source_caller = self.name
        if not status:
            web_response.error = utility_common.dict_to_string(results)
        else:
            web_response.results = results
        return web_response


class ConnectionIsOK(functionCall):
    def __init__(self):
        super(ConnectionIsOK, self).__init__("connection_is_ok")

    def is_valid(self, web_request):
        return True, ''  ## no arguments

    def call(self, connection, is_test):
        status, results = apis.connection_is_ok(connection)
        return self._make_response(status, results)

    def create_new(self):
        return ConnectionIsOK()


class AccountStatus(functionCall):
    def __init__(self):
        super(AccountStatus, self).__init__("account_status")
        self.user_email = ''

    def is_valid(self, web_request):
        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()
        if len(self.user_email) == 0:
            return False, "user_email is empty"

        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_status(connection, self.user_email)
        return self._make_response(status, results)

    def create_new(self):
        return AccountStatus()


class AccountCreate(functionCall):
    def __init__(self):
        super(AccountCreate, self).__init__("account_create")
        self.user_email = ''
        self.user_password = ''
        self.user_ip = ''
        self.callback_url = ''

    def is_valid(self, web_request):
        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()
        if len(self.user_email) == 0:
            return False, "user_email is empty"

        if 'user_password' not in web_request.arguments:
            return False, " key 'user_password' is missing"
        self.user_password = web_request.arguments['user_password'].strip()
        if len(self.user_password) == 0:
            return False, "user_password is empty"

        if 'user_ip' not in web_request.arguments:
            return False, " key 'user_ip' is missing"
        self.user_ip = web_request.arguments['user_ip'].strip()
        if len(self.user_ip) == 0:
            return False, "user_ip is empty"

        if 'callback_url' not in web_request.arguments:
            return False, " key 'callback_url' is missing"
        self.callback_url = web_request.arguments['callback_url'].strip()
        if len(self.callback_url) == 0:
            return False, "callback_url is empty"

        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_create(connection, self.user_email, self.user_password, self.user_ip,
                                              self.callback_url, is_test)
        return self._make_response(status, results)

    def create_new(self):
        return AccountCreate()


class AccountActivationKeyStatus(functionCall):
    def __init__(self):
        super(AccountActivationKeyStatus, self).__init__("account_activation_key_status")
        self.activation_key = ''

    def is_valid(self, web_request):
        if 'activation_key' not in web_request.arguments:
            return False, " key 'activation_key' is missing"
        self.activation_key = web_request.arguments['activation_key'].strip()
        if len(self.activation_key) == 0:
            return False, "activation_key is empty"

        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_activation_key_status(connection, self.activation_key)
        return self._make_response(status, results)

    def create_new(self):
        return AccountActivationKeyStatus()


class AccountSendActivationKey(functionCall):
    def __init__(self):
        super(AccountSendActivationKey, self).__init__("account_send_activation_key")
        self.user_email = ''
        self.callback_url = ''

    def is_valid(self, web_request):
        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()
        if len(self.user_email) == 0:
            return False, "user_email is empty"

        if 'callback_url' not in web_request.arguments:
            return False, " key 'callback_url' is missing"
        self.callback_url = web_request.arguments['callback_url'].strip()
        if len(self.callback_url) == 0:
            return False, "callback_url is empty"

        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_send_activation_key(connection, self.user_email, self.callback_url, is_test)
        return self._make_response(status, results)

    def create_new(self):
        return AccountSendActivationKey()


class AccountPasswordChange(functionCall):
    def __init__(self):
        super(AccountPasswordChange, self).__init__("account_password_change")
        self.user_email = ''
        self.user_password = ''
        self.new_password = ''

    def is_valid(self, web_request):
        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()
        if len(self.user_email) == 0:
            return False, "user_email is empty"

        if 'user_password' not in web_request.arguments:
            return False, " key 'user_password' is missing"
        self.user_password = web_request.arguments['user_password'].strip()
        if len(self.user_password) == 0:
            return False, "user_password is empty"

        if 'new_password' not in web_request.arguments:
            return False, " key 'new_password' is missing"
        self.new_password = web_request.arguments['new_password'].strip()
        if len(self.user_email) == 0:
            return False, "new_password is empty"

        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_password_change(connection, self.user_email, self.user_password,
                                                       self.new_password,
                                                       is_test)
        return self._make_response(status, results)

    def create_new(self):
        return AccountPasswordChange()


class AccountIPChange(functionCall):
    def __init__(self):
        super(AccountIPChange, self).__init__("account_ip_change")
        self.user_email = ''
        self.user_password = ''
        self.new_ip = ''

    def is_valid(self, web_request):
        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()
        if len(self.user_email) == 0:
            return False, "user_email is empty"

        if 'user_password' not in web_request.arguments:
            return False, " key 'user_password' is missing"
        self.user_password = web_request.arguments['user_password'].strip()
        if len(self.user_password) == 0:
            return False, "user_password is empty"

        if 'new_ip' not in web_request.arguments:
            return False, " key 'new_ip' is missing"
        self.new_ip = web_request.arguments['new_ip'].strip()
        if len(self.new_ip) == 0:
            return False, "new_ip is empty"

        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_ip_change(connection, self.user_email, self.user_password, self.new_ip,
                                                 is_test)
        return self._make_response(status, results)

    def create_new(self):
        return AccountIPChange()


class AccountPasswordReset(functionCall):
    def __init__(self):
        super(AccountPasswordReset, self).__init__("account_password_reset")
        self.activation_key = ''
        self.new_password = ''

    def is_valid(self, web_request):
        if 'activation_key' not in web_request.arguments:
            return False, " key 'activation_key' is missing"
        self.activation_key = web_request.arguments['activation_key'].strip()
        if len(self.activation_key) == 0:
            return False, "activation_key is empty"

        if 'new_password' not in web_request.arguments:
            return False, " key 'new_password' is missing"
        self.new_password = web_request.arguments['new_password'].strip()
        if len(self.new_password) == 0:
            return False, "new_password is empty"

        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_password_reset(connection, self.activation_key, self.new_password,
                                                      is_test)
        return self._make_response(status, results)

    def create_new(self):
        return AccountPasswordReset()


class AccountProfile(functionCall):
    def __init__(self):
        super(AccountProfile, self).__init__("account_profile")
        self.user_email = ''
        self.password = ''

    def is_valid(self, web_request):
        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()
        if len(self.user_email) == 0:
            return False, "user_email is empty"

        if 'password' not in web_request.arguments:
            return False, " key 'password' is missing"
        self.password = web_request.arguments['password'].strip()
        if len(self.password) == 0:
            return False, "password is empty"

        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_profile(connection, self.user_email, self.password)
        return self._make_response(status, results)

    def create_new(self):
        return AccountProfile()


class AccountActivate(functionCall):
    def __init__(self):
        super(AccountActivate, self).__init__("account_activate")
        self.activation_key = ''

    def is_valid(self, web_request):
        if 'activation_key' not in web_request.arguments:
            return False, " key 'activation_key' is missing"
        self.activation_key = web_request.arguments['activation_key'].strip()
        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_activate(connection, self.activation_key, is_test)
        return self._make_response(status, results)

    def create_new(self):
        return AccountActivate()


class AccountTokenCreate(functionCall):
    def __init__(self):
        super(AccountTokenCreate, self).__init__("account_token_create")
        self.email = ''

    def is_valid(self, web_request):
        if 'email' not in web_request.arguments:
            return False, " key 'email' is missing"
        self.email = web_request.arguments['email'].strip()
        return True, ''

    def call(self, connection, is_test):
        status, results = apis.account_token_generate(connection, self.email)
        return self._make_response(status, results)

    def create_new(self):
        return AccountTokenCreate()


account_apis_factory = dict()
account_apis_factory[AccountTokenCreate().name] = AccountTokenCreate()
account_apis_factory[ConnectionIsOK().name] = ConnectionIsOK()
account_apis_factory[AccountStatus().name] = AccountStatus()
account_apis_factory[AccountCreate().name] = AccountCreate()
account_apis_factory[AccountActivationKeyStatus().name] = AccountActivationKeyStatus()
account_apis_factory[AccountIPChange().name] = AccountIPChange()
account_apis_factory[AccountPasswordChange().name] = AccountPasswordChange()
account_apis_factory[AccountProfile().name] = AccountProfile()
account_apis_factory[AccountSendActivationKey().name] = AccountSendActivationKey()
account_apis_factory[AccountPasswordReset().name] = AccountPasswordReset()
account_apis_factory[AccountActivate().name] = AccountActivate()


class Describe(functionCall):
    def __init__(self):
        super(Describe, self).__init__("describe")

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"

        self.user_email = web_request.arguments['user_email'].strip()

        self.element = ''
        if 'element' in web_request.arguments:
            self.element = web_request.arguments['element'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.describe(connection, self.user_email, self.element)
        return self._make_response(status, results)

    def create_new(self):
        return Describe()


class ShowAvailable(functionCall):
    def __init__(self):
        super(ShowAvailable, self).__init__("show_available")

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"

        self.user_email = web_request.arguments['user_email'].strip()

        self.element = ''
        if 'element' in web_request.arguments:
            self.element = web_request.arguments['element'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.show_available(connection, self.user_email, self.element)
        return self._make_response(status, results)

    def create_new(self):
        return ShowAvailable()


class PnlAttribute(functionCall):
    def __init__(self):
        super(PnlAttribute, self).__init__("pnl_attribute")
        self.load_as = ''
        self.from_date = ''
        self.to_date = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        self.load_as = ''
        if 'load_as' not in web_request.arguments:
            return False, " key 'load_as' is missing"
        self.load_as = web_request.arguments['load_as'].strip()

        self.from_date = ''
        if 'from_date' not in web_request.arguments:
            return False, " key 'from_date' is missing"
        self.from_date = web_request.arguments['from_date'].strip()

        self.to_date = ''
        if 'to_date' not in web_request.arguments:
            return False, " key 'to_date' is missing"
        self.to_date = web_request.arguments['to_date'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.pnl_attribute(connection, self.user_email, self.load_as, self.from_date, self.to_date)
        return self._make_response(status, results)

    def create_new(self):
        return PnlAttribute()


class PnlPredict(functionCall):
    def __init__(self):
        super(PnlPredict, self).__init__("pnl_predict")
        self.load_as = ''
        self.from_date = ''
        self.to_date = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        self.load_as = ''
        if 'load_as' not in web_request.arguments:
            return False, " key 'load_as' is missing"
        self.load_as = web_request.arguments['load_as'].strip()

        self.from_date = ''
        if 'from_date' not in web_request.arguments:
            return False, " key 'from_date' is missing"
        self.from_date = web_request.arguments['from_date'].strip()

        self.to_date = ''
        if 'to_date' not in web_request.arguments:
            return False, " key 'to_date' is missing"
        self.to_date = web_request.arguments['to_date'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.pnl_predict(connection, self.user_email, self.load_as, self.from_date, self.to_date)
        return self._make_response(status, results)

    def create_new(self):
        return PnlPredict()


class RiskLadder(functionCall):
    def __init__(self):
        super(RiskLadder, self).__init__("risk_ladder")
        self.load_as = ''
        self.from_date = ''
        self.to_date = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        self.load_as = ''
        if 'load_as' not in web_request.arguments:
            return False, " key 'load_as' is missing"
        self.load_as = web_request.arguments['load_as'].strip()

        self.asof = ''
        if 'asof' not in web_request.arguments:
            return False, " key 'asof' is missing"
        self.asof = web_request.arguments['asof'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.risk_ladder(connection, self.user_email, self.asof, self.load_as)
        return self._make_response(status, results)

    def create_new(self):
        return RiskLadder()


class Price(functionCall):
    def __init__(self):
        super(Price, self).__init__("price")
        self.load_as = ''
        self.from_date = ''
        self.to_date = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        self.load_as = ''
        if 'load_as' not in web_request.arguments:
            return False, " key 'load_as' is missing"
        self.load_as = web_request.arguments['load_as'].strip()

        self.asof = ''
        if 'asof' not in web_request.arguments:
            return False, " key 'asof' is missing"
        self.asof = web_request.arguments['asof'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.price(connection, self.user_email, self.asof, self.load_as)
        return self._make_response(status, results)

    def create_new(self):
        return Price()


class PriceVanillaSwap(functionCall):
    def __init__(self):
        super(PriceVanillaSwap, self).__init__("price_vanilla_swap")
        self.asof = ''
        self.type_ = ''
        self.notional = ''
        self.trade_date = ''
        self.trade_maturity = ''
        self.index_id = ''
        self.discount_id = ''
        self.floating_leg_period = ''
        self.fixed_leg_period = ''
        self.floating_leg_daycount = ''
        self.fixed_leg_daycount = ''
        self.fixed_rate = ''
        self.is_payer = ''
        self.spread = ''
        self.business_day_rule = ''
        self.business_centres = ''
        self.spot_lag_days = ''
        self.save_as = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        self.asof = ''
        if 'asof' not in web_request.arguments:
            return False, " key 'asof' is missing"
        self.asof = web_request.arguments['asof'].strip()

        self.type_ = ''
        if 'type' not in web_request.arguments:
            return False, " key 'type' is missing"
        self.type_ = web_request.arguments['type'].strip()

        self.notional = ''
        if 'notional' not in web_request.arguments:
            return False, " key 'notional' is missing"
        self.notional = web_request.arguments['notional'].strip()

        self.trade_date = ''
        if 'trade_date' not in web_request.arguments:
            return False, " key 'trade_date' is missing"
        self.trade_date = web_request.arguments['trade_date'].strip()

        self.trade_maturity = ''
        if 'trade_maturity' not in web_request.arguments:
            return False, " key 'trade_maturity' is missing"
        self.trade_maturity = web_request.arguments['trade_maturity'].strip()

        self.index_id = ''
        if 'index_id' not in web_request.arguments:
            return False, " key 'index_id' is missing"
        self.index_id = web_request.arguments['index_id'].strip()

        self.discount_id = ''
        if 'discount_id' not in web_request.arguments:
            return False, " key 'discount_id' is missing"
        self.discount_id = web_request.arguments['discount_id'].strip()

        self.floating_leg_period = ''
        if 'floating_leg_period' not in web_request.arguments:
            return False, " key 'floating_leg_period' is missing"
        self.floating_leg_period = web_request.arguments['floating_leg_period'].strip()

        self.fixed_leg_period = ''
        if 'fixed_leg_period' not in web_request.arguments:
            return False, " key 'fixed_leg_period' is missing"
        self.fixed_leg_period = web_request.arguments['fixed_leg_period'].strip()

        self.floating_leg_daycount = ''
        if 'floating_leg_daycount' not in web_request.arguments:
            return False, " key 'floating_leg_daycount' is missing"
        self.floating_leg_daycount = web_request.arguments['floating_leg_daycount'].strip()

        self.fixed_leg_daycount = ''
        if 'fixed_leg_daycount' not in web_request.arguments:
            return False, " key 'fixed_leg_daycount' is missing"
        self.fixed_leg_daycount = web_request.arguments['fixed_leg_daycount'].strip()

        self.fixed_rate = ''
        if 'fixed_rate' in web_request.arguments:
            self.fixed_rate = web_request.arguments['fixed_rate'].strip()

        self.is_payer = ''
        if 'is_payer' not in web_request.arguments:
            return False, " key 'is_payer' is missing"
        self.is_payer = web_request.arguments['is_payer'].strip()

        self.spread = ''
        if 'spread' not in web_request.arguments:
            return False, " key 'spread' is missing"
        self.spread = web_request.arguments['spread'].strip()

        self.business_day_rule = ''
        if 'business_day_rule' not in web_request.arguments:
            return False, " key 'business_day_rule' is missing"
        self.business_day_rule = web_request.arguments['business_day_rule'].strip()

        self.business_centres = ''
        if 'business_centres' not in web_request.arguments:
            return False, " key 'business_centres' is missing"
        self.business_centres = web_request.arguments['business_centres'].strip()

        self.spot_lag_days = ''
        if 'spot_lag_days' not in web_request.arguments:
            return False, " key 'spot_lag_days' is missing"
        self.spot_lag_days = web_request.arguments['spot_lag_days'].strip()

        self.save_as = ''
        if 'save_as' in web_request.arguments:
            self.save_as = web_request.arguments['save_as'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.price_vanilla_swap(
            connection
            , self.user_email
            , self.asof
            , self.type_
            , self.notional
            , self.trade_date
            , self.trade_maturity
            , self.index_id
            , self.discount_id
            , self.floating_leg_period
            , self.fixed_leg_period
            , self.floating_leg_daycount
            , self.fixed_leg_daycount
            , self.fixed_rate
            , self.is_payer
            , self.spread
            , self.business_day_rule
            , self.business_centres
            , self.spot_lag_days
            , self.save_as)

        return self._make_response(status, results)

    def create_new(self):
        return PriceVanillaSwap()


class PriceFxForward(functionCall):
    def __init__(self):
        super(PriceFxForward, self).__init__("price_fx_forward")
        self.asof = ''
        self.type_ = ''
        self.trade_date = ''
        self.trade_expiry = ''
        self.pay_amount = ''
        self.pay_currency = ''
        self.receive_amount = ''
        self.receive_currency = ''
        self.save_as = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        self.asof = ''
        if 'asof' not in web_request.arguments:
            return False, " key 'asof' is missing"
        self.asof = web_request.arguments['asof'].strip()

        self.type_ = ''
        if 'type' not in web_request.arguments:
            return False, " key 'type' is missing"
        self.type_ = web_request.arguments['type'].strip()

        self.trade_date = ''
        if 'trade_date' not in web_request.arguments:
            return False, " key 'trade_date' is missing"
        self.trade_date = web_request.arguments['trade_date'].strip()

        self.trade_expiry = ''
        if 'trade_expiry' not in web_request.arguments:
            return False, " key 'trade_maturity' is missing"
        self.trade_expiry = web_request.arguments['trade_expiry'].strip()

        self.pay_amount = ''
        if 'pay_amount' not in web_request.arguments:
            return False, " key 'pay_amount' is missing"
        self.pay_amount = web_request.arguments['pay_amount'].strip()

        self.pay_currency = ''
        if 'pay_currency' not in web_request.arguments:
            return False, " key 'pay_currency' is missing"
        self.pay_currency = web_request.arguments['pay_currency'].strip()

        self.receive_amount = ''
        if 'receive_amount' not in web_request.arguments:
            return False, " key 'receive_amount' is missing"
        self.receive_amount = web_request.arguments['receive_amount'].strip()

        self.receive_currency = ''
        if 'receive_currency' not in web_request.arguments:
            return False, " key 'receive_currency' is missing"
        self.receive_currency = web_request.arguments['receive_currency'].strip()

        self.save_as = ''
        if 'save_as' in web_request.arguments:
            self.save_as = web_request.arguments['save_as'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.price_fx_forward(connection
                                                , self.user_email
                                                , self.asof
                                                , self.type_
                                                , self.trade_date
                                                , self.trade_expiry
                                                , self.pay_amount
                                                , self.pay_currency
                                                , self.receive_amount
                                                , self.receive_currency
                                                , self.save_as)
        return self._make_response(status, results)

    def create_new(self):
        return PriceFxForward()


class MarketSwapRates(functionCall):
    def __init__(self):
        super(MarketSwapRates, self).__init__("market_swap_rates")
        self.asof = ''
        self.currency = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        self.asof = ''
        if 'asof' not in web_request.arguments:
            return False, " key 'asof' is missing"
        self.asof = web_request.arguments['asof'].strip()

        self.currency = ''
        if 'currency' not in web_request.arguments:
            return False, " key 'currency' is missing"
        self.currency = web_request.arguments['currency'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.market_swap_rates(connection, self.user_email, self.asof, self.currency)
        return self._make_response(status, results)

    def create_new(self):
        return MarketSwapRates()


class MarketFxRates(functionCall):
    def __init__(self):
        super(MarketFxRates, self).__init__("market_fx_rates")
        self.base_date = ''
        self.base_currency = ''
        self.asof = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        self.asof = ''
        if 'asof' not in web_request.arguments:
            return False, " key 'asof' is missing"
        self.asof = str(web_request.arguments['asof']).strip()

        self.base_currency = ''
        if 'base_currency' not in web_request.arguments:
            return False, " key 'base_currency' is missing"
        self.base_currency = web_request.arguments['base_currency'].strip()

        self.to_date = ''
        if 'to_date' not in web_request.arguments:
            return False, " key 'to_date' is missing"
        self.to_date = str(web_request.arguments['to_date']).strip()

        return True, ''

    def call(self, connection, is_test=False):

        status, results = apis.market_fx_rates(connection, self.user_email, self.asof, self.to_date, self.base_currency)
        return self._make_response(status, results)

    def create_new(self):
        return MarketFxRates()


class Workspace(functionCall):
    def __init__(self):
        super(Workspace, self).__init__("workspace")
        self.delete = ''
        self.list = ''

    def is_valid(self, web_request):

        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email = web_request.arguments['user_email'].strip()

        if 'list' in web_request.arguments:
            self.list = web_request.arguments['list'].strip()
        else:
            if 'delete' in web_request.arguments:
                self.delete = web_request.arguments['delete'].strip()

        return True, ''

    def call(self, connection, is_test=False):
        status, results = apis.workspace(connection, self.user_email, self.list, self.delete)
        return self._make_response(status, results)

    def create_new(self):
        return Workspace()


general_apis_factory = dict()
general_apis_factory[Describe().name] = Describe()
general_apis_factory[ShowAvailable().name] = ShowAvailable()
general_apis_factory[PnlPredict().name] = PnlPredict()
general_apis_factory[PnlAttribute().name] = PnlAttribute()
general_apis_factory[RiskLadder().name] = RiskLadder()
general_apis_factory[Price().name] = Price()
general_apis_factory[PriceVanillaSwap().name] = PriceVanillaSwap()
general_apis_factory[PriceFxForward().name] = PriceFxForward()
general_apis_factory[MarketSwapRates().name] = MarketSwapRates()
general_apis_factory[MarketFxRates().name] = MarketFxRates()
general_apis_factory[Workspace().name] = Workspace()


# def account_api(json_request_string, is_test=settings.is_development):
#     return api_gateway(json_request_string, account_apis_factory)


def api_gateway(json_request_string, factory=None):
    if factory is None:
        factory = account_apis_factory

    connection = utility_connection.WebConnection(settings.email_default, settings.url_server, settings.token_path)
    #
    # create an empty response
    #
    web_response = WebResponse()
    try:
        #
        # ceate a request, parse it and validate it
        #
        web_request = WebRequest()
        status, error = web_request.from_string(json_request_string)
        if not status:
            web_response.error = error
            return web_response.to_string()

        function_name = web_request.function_name
        if function_name not in factory:
            web_response.error = "function_name '" + function_name + "' not found"
            return web_response.to_string()
        #
        # all good we have a valid function name.
        #
        function = factory[function_name].create_new()
        #
        # validate the arguments
        #
        status, error = function.is_valid(web_request)
        if not status:
            web_response.error = error
            return web_response.to_string()

        #
        # call the function and return values
        #
        web_response = function.call(connection, settings.is_development)

        #
        # and off we go
        #
        print(web_response.to_string())
        return web_response.to_string()
    except Exception as e:
        web_response.error = str(e)
        return web_response.to_string()
