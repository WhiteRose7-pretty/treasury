import app.modules.utility_common as utility_common
import app.modules.settings as settings
#
# import json
#
# from app.modules.apis_for_json import general_apis_factory, api_gateway, account_apis_factory
#
#
# def test_account_api():
#     print(api_gateway(
#         "{\"function_name\":\"connection_is_ok\", \"arguments\":null, \"source_caller\":\"front-end-function1\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_status\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function2\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_create\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"user_ip\":\"127.0.0.1\", \"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function3\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_activation_key_status\", \"arguments\":{\"activation_key\":\"j7v3ffy_uqbggkgt-mstvc_qa1bxyp42vgfvuvj83gyvc-fwdglgla\"}, \"source_caller\":\"front-end-function4\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_send_activation_key\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\",\"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function5\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_send_activation_key\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\",\"callback_url\":\"treasuryquants.com/urlcallback/\"}, \"source_caller\":\"front-end-function6\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_password_change\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"new_password\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function7\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_ip_change\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"new_ip\":\"127.0.0.1\"}, \"source_caller\":\"front-end-function8\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_password_reset\", \"arguments\":{\"new_password\":\"test.account@treasuryquants.com\",\"activation_key\":\"j7v3ffy_uqbggkgt-mstvc_qa1bxyp42vgfvuvj83gyvc-fwdglgla\"}, \"source_caller\":\"front-end-function9\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_profile\", \"arguments\":{\"user_email\":\"test.account@treasuryquants.com\",\"password\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function10\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_token_create\", \"arguments\":{\"email\":\"test.account@treasuryquants.com\",\"password\":\"test.account@treasuryquants.com\"}, \"source_caller\":\"front-end-function10\"}"))
#     print(api_gateway(
#         "{\"function_name\":\"account_token_create\", \"arguments\":{\"email\":\"valya.varechkina.76@bk.ru\"}, \"source_caller\":\"front-end-function10\"}"))
#
#
# def ip_return():
#     print(api_gateway(
#         "{\"function_name\":\"ip_return\", \"arguments\":{}, \"source_caller\":\"get_self_ip\"}"))
#
#
# def account_create():
#     print(api_gateway(
#         "{\"function_name\":\"account_ip_change\", \"arguments\":{\"user_password\":\"test.account@treasuryquants.com\",\"user_email\":\"test.account@treasuryquants.com\",\"new_ip\":\"127.0.0.1\"}, \"source_caller\":\"front-end-function8\"}"))
#
#
# def account_active():
#     print(api_gateway(
#         "{\"function_name\":\"account_activate\", \"arguments\":{"
#         "\"activation_key\":\"btfy0i37xoxam_c9bpipedxagxamxsowgez8lycbwropgtrusiovmg\" "
#         "}, \"source_caller\":\"front-end-function3\"}"))
#
#
# def check():
#     print(api_gateway(
#         "{\"function_name\":\"account_token_create\", \"arguments\":{\"email\":\"valya.varechkina.76@bk.ru\",\"password\":\"test.account\"}, \"source_caller\":\"front-end-function10\"}"))
#
#
# def call_web_api(request):
#     data = json.loads(request)
#     post_data = json.dumps(data)
#     result = api_gateway(post_data, general_apis_factory)
#     result_dic = json.loads(result)
#     return result_dic  # JsonResponse(result_dic)
#
#
# ip_return()
#
#
#
#
#


# utility_common.process_fatal_error("post_message", "message", settings.path_error_file, settings.email_webmaster,
#                                    settings.is_development)