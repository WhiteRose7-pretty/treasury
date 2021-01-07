from  app.modules.apis_for_json import web_api

print(web_api("{\"function_name\":\"connection_is_ok\", \"arguments\":null, \"source_caller\":\"front-end-function[connection_is_ok]\"}", True))
print(web_api("{\"function_name\":\"account_status\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function2\"}",True))
print(web_api("{\"function_name\":\"account_create\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"user_ip\":\"127.0.0.1\", \"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function[account_status]\"}",True))
print(web_api("{\"function_name\":\"account_activation_key_status\", \"arguments\":{\"activation_key\":\"j7v3ffy_uqbggkgt-mstvc_qa1bxyp42vgfvuvj83gyvc-fwdglgla\"}, \"source_caller\":\"front-end-function[account_create]\"}",True))
print(web_api("{\"function_name\":\"account_send_activation_key\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\",\"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function[account_activation_key_status]\"}",True))
print(web_api("{\"function_name\":\"account_password_change\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"new_password\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function[account_password_change]\"}",True))
print(web_api("{\"function_name\":\"account_ip_change\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"new_ip\":\"127.0.0.1\"}, \"source_caller\":\"front-end-function[account_ip_change]\"}",True))
print(web_api("{\"function_name\":\"account_password_reset\", \"arguments\":{\"new_password\":\"test.account@treasuryquants.com\",\"activation_key\":\"j7v3ffy_uqbggkgt-mstvc_qa1bxyp42vgfvuvj83gyvc-fwdglgla\"}, \"source_caller\":\"front-end-function[account_password_reset]\"}",True))
print(web_api("{\"function_name\":\"account_profile\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\",\"password\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function[account_profile]\"}",True))

