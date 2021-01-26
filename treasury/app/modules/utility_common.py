#
# common and generic utilities
#
from app.modules import utility_email


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


def process_fatal_error(error_message, is_development=False):
    if is_development:
        print(error_message)
    else:
        # utility_email.send_email("operations@treasuryquants.com", "web cron error", error_message)
        utility_email.send_email("valya.varechkina.76@bk.ru", "web cron error", error_message)