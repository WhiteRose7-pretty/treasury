#
# common and generic utilities
#

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