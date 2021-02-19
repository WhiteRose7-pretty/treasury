
import TQapis.TQConnection as TQConnection
import TQapis.TQRequests as TQRequests
import app.modules.settings as settings

import datetime
import json
import os

class TokenContext:
    def __init__(self, token='',expiry=None):
        self.secret=token
        self.expiry=datetime.datetime.now()
        if expiry  is not None:
            self.expiry=expiry #assuming it is time.

    def to_string(self):
        results=dict()
        results['secret']=self.secret
        results['expiry']=self.expiry.strftime("%Y-%m-%d %H:%M:%S")
        return json.dumps(results)

    def from_string(self, string_json):
        if string_json=='':
            return
        content=json.loads(string_json)
        self.secret=content['secret']
        self.expiry=datetime.datetime.strptime(content['expiry'],"%Y-%m-%d %H:%M:%S")


def token_from_file(token_path):
    token_context=TokenContext()
    with open(token_path, 'rt') as file:
        content=file.read()
        token_context.from_string(content)
    return token_context


def token_to_file(token_path,token_context):
    file= open(token_path, 'w')
    file.writelines(token_context.to_string())


class WebConnection (TQConnection.Connection):
    def __init__(self,email, url, token_path):
        self.__minutes_to_expiry=1
        self.__function_name_account_token_create = 'account_token_create'  # the function name for creating the token
        TQConnection.Connection.__init__(self,email, url, minutes_to_expiry=1)
        self.token_path=token_path
        self.token_context = token_from_file(self.token_path)
        self.token=self.token_context.secret
        self.expiry=self.token_context.expiry

    def send_web(self, request):
        if self.token=='':
            self.expiry=datetime.datetime.now()
        result = self.send(request)
        if self.token!=self.token_context.secret: # we now have an updated tokenl
            self.token_context=TokenContext(self.token,self.expiry)
            token_to_file(self.token_path, self.token_context)
        return result


# print(os.getcwd())
#
# token=TokenContext("ABC",datetime.datetime.now())
# token_to_file(settings.token_path,token)
# print(token_from_file(settings.token_path).to_string())