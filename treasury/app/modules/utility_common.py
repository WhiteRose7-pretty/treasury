#
# common and generic utilities
#
from app.modules import utility_email
import os
import json

def dict_to_string(results):
    message = ""
    i = 0
    for key, value in results.items():
        message += key + ":" + value
        if i < len(results) - 1:
            message += "\n"
    return message


def list_to_csv(l):
    s = ''
    for i in range(0, len(l)):
        s += str(l[i])
        if i < len(l) - 1:
            s += ","
    return s


def process_fatal_error(subject,error_message, is_development=False):
    if is_development:
        print(error_message)
    else:

        utility_email.send_email("valya.varechkina.76@bk.ru", subject, error_message)


def get_workbench_descriptions_json_string(api_names):
    descriptions = dict()
    for api_name in api_names:
        descriptions[api_name] = ''
        file_path = os.path.join("app/modules/workbench/descriptions/", api_name + ".html")
        try:
            input_file= open(file_path, "r")
            descriptions[api_name] = input_file.read().encode("utf-8").hex()
            input_file.close()
        except:
            continue

    return descriptions
