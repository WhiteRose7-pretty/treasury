#
# common and generic utilities
#

def dict_to_string(results):
    message = ""
    for key, value in results.items():
        message += key + "=>" + value + "\n"
    return message