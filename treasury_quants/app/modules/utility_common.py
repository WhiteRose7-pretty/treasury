#
# common and generic utilities
#


import os

from app.modules.error_policy import ErrorPolicy


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


def process_fatal_error(subject, error_message, error_file,recipient_email, is_development=False):
    if is_development:
        print(error_message)
    else:
        error_policy = ErrorPolicy(error_file)
        if error_policy.should_send_email(subject):
            error_policy.process_error(recipient_email, subject, error_message)






def get_workbench_descriptions_json_string(api_names):
    descriptions = dict()
    for api_name in api_names:
        file_path = os.path.join("app/modules/workbench/descriptions/", api_name + ".txt")
        try:
            input_file= open(file_path, "rt")
            descriptions[api_name] = input_file.read().encode("utf-8").hex()
            input_file.close()
        except:
            continue

    return descriptions
