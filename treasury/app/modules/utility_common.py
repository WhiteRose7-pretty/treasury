#
# common and generic utilities
#
from app.modules import utility_email


def dict_to_string(results):
    message = ""
    for key, value in results.items():
        message += key + "=>" + value + "\n"
    return message


def list_to_csv(l):
    s = ''
    for i in range(0, len(l)):
        s += str(l[i])
        if i < len(l) - 1:
            s += ","
    return s


def process_fatal_error(error_message, is_development=False):
    if is_development:
        print(error_message)
    else:
        utility_email.send_email("operations@treasuryquants.com", "web cron error",error_message)
