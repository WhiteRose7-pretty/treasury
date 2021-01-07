
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
        self.function_name=""
        self.arguments=dict()
        self.source_caller=""
    def from_string(self, string_json):

        try:
            request=json.loads(string_json)
            if 'function_name' not in request:
                return False, "key 'function_name' is missing"
            if 'arguments' not in request:
                return False, "key 'arguments' is missing"
            if 'source_caller' not in request:
                return False, "key 'source_caller' is missing"

            self.function_name=request['function_name'].strip()
            self.arguments=request['arguments']
            self.source_caller=request['source_caller'].strip()


            if len( self.function_name)==0:
                return False, "key 'function_name' has no value"
            if len(self.source_caller) == 0:
                return False, "key 'source_caller' has no value"

            return True,''
        except Exception as e:
            raise Exception("WebRequest.from_string:"+str(e))



class WebResponse:
    def __init__(self):
        self.results=dict()
        self.error=""
        self.source_caller=''

    def to_string(self):
        response=dict()
        response['error']=self.error
        response['results']=self.results
        response['source_caller']=self.source_caller
        return json.dumps(response)

class functionCall:
    def __init__(self, name):
        self.name=name

    def is_valid(self,web_request):
        pass

    def call(self,connection, is_test):
        pass

    def create_new(self):
        pass

    def _make_response(self,status,results):
        web_response=WebResponse()
        web_response.source_caller=self.name
        if not status:
            web_response.error=utility_common.dict_to_string(results)
        else:
            web_response.results=results
        return web_response



class ConnectionIsOK(functionCall):
    def __init__(self):
        super(ConnectionIsOK, self).__init__("connection_is_ok")

    def is_valid(self,web_request):
        return True, '' ## no arguments

    def call(self,connection,is_test):
        status, results = apis.connection_is_ok(connection)
        return self._make_response(status,results)

    def create_new(self):
        return ConnectionIsOK()

class AccountStatus(functionCall):
    def __init__(self):
        super(AccountStatus, self).__init__("account_status")
        self.user_email=''
    def is_valid(self,web_request):
        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email=web_request.arguments['user_email'].strip()
        if len(self.user_email)==0:
            return False ,"user_email is empty"

        return True, ''

    def call(self,connection,is_test):
        status, results = apis.account_status(connection, self.user_email)
        return self._make_response(status,results)

    def create_new(self):
        return AccountStatus()



class AccountCreate(functionCall):
    def __init__(self):
        super(AccountCreate, self).__init__("account_create")
        self.user_email=''
        self.user_password=''
        self.user_ip=''
        self.callback_url=''

    def is_valid(self,web_request):
        if 'user_email' not in web_request.arguments:
            return False, " key 'user_email' is missing"
        self.user_email=web_request.arguments['user_email'].strip()
        if len(self.user_email)==0:
            return False ,"user_email is empty"

        if 'user_password' not in web_request.arguments:
            return False, " key 'user_password' is missing"
        self.user_password=web_request.arguments['user_password'].strip()
        if len(self.user_password)==0:
            return False ,"user_password is empty"

        if 'user_ip' not in web_request.arguments:
            return False, " key 'user_ip' is missing"
        self.user_ip=web_request.arguments['user_ip'].strip()
        if len(self.user_ip)==0:
            return False ,"user_ip is empty"

        if 'callback_url' not in web_request.arguments:
            return False, " key 'callback_url' is missing"
        self.callback_url=web_request.arguments['callback_url'].strip()
        if len(self.callback_url)==0:
            return False ,"callback_url is empty"

        return True, ''

    def call(self,connection,is_test):
        status, results = apis. account_create(connection, self.user_email, self.user_password, self.user_ip, self.callback_url, is_test)
        return self._make_response(status,results)

    def create_new(self):
        return AccountCreate()


class AccountActivationKeyStatus(functionCall):
    def __init__(self):
        super(AccountActivationKeyStatus, self).__init__("account_activation_key_status")
        self.activation_key=''
    def is_valid(self,web_request):
        if 'activation_key' not in web_request.arguments:
            return False, " key 'activation_key' is missing"
        self.activation_key=web_request.arguments['activation_key'].strip()
        if len(self.activation_key)==0:
            return False ,"activation_key is empty"

        return True, ''

    def call(self,connection,is_test):
        status, results = apis.account_status(connection, self.activation_key)
        return self._make_response(status,results)

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
        status, results = apis.account_send_activation_key(connection,self.user_email, self.callback_url, is_test)
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
        status, results = apis.account_password_change(connection, self.user_email, self.user_password, self.new_password,
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



factory=dict()
factory[ConnectionIsOK().name]=ConnectionIsOK()
factory[AccountStatus().name]=AccountStatus()
factory[AccountCreate().name]=AccountCreate()
factory[AccountActivationKeyStatus().name]=AccountActivationKeyStatus()
factory[AccountIPChange().name]=AccountIPChange()
factory[AccountPasswordChange().name]=AccountPasswordChange()
factory[AccountProfile().name]=AccountProfile()
factory[AccountSendActivationKey().name]=AccountSendActivationKey()
factory[AccountPasswordReset().name]=AccountPasswordReset()



def web_api(json_request_string, is_test=False):
    connection = utility_connection.WebConnection(settings.email_default, settings.url_server, settings.token_path)
    #
    # ceate an empty response
    #
    web_response = WebResponse()
    try:
        #
        # ceate a request, parse it and validate it
        #
        web_request=WebRequest()
        status, error=web_request.from_string(json_request_string)
        if not status:
            web_response.error=error
            return web_response.to_string()

        function_name=web_request.function_name
        if function_name not in factory:
            web_response.error="function_name '"+function_name+"' not found"
            return web_response.to_string()
        #
        # all good we have a valid function name.
        #
        function=factory[function_name].create_new()
        #
        # validate the arguments
        #
        status, error=function.is_valid(web_request)
        if not status:
            web_response.error=error
            return web_response.to_string()

        #
        # call the function and return values
        #
        web_response=function.call(connection, is_test)

        #
        # and off we go
        #
        return web_response.to_string()
    except Exception as e:
        web_response.error = str(e)
        return web_response.to_string()


