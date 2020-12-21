from django.shortcuts import render
from django.http import JsonResponse
import json, os

TOKEN_FILE_PATH = 'api/token.txt'


def upload_grid_file(args):
    try:
        file_name = args['file_name']
        content = args['content']
        if os.access(file_name, os.R_OK):
            f = open(file_name, 'w')
            f.write(content)
            f.close()
            status = True
            result = {
                'msg': 'Succcessfully done'
            }
        else:
            status = False
            result = {
                'msg': 'There are not file'
            }
    except:
        status = False
        result = {
            'msg': 'Error in Function'
        }
        
    output = {
        'status': status,
        'result': result,
    }
    return output

methods = {
    'upload_grid_file': upload_grid_file,
}


def update(request):
    request_data = json.loads(request.body.decode('utf-8'))

    token_request = request_data['token']
    f = open(TOKEN_FILE_PATH, 'r')
    token = f.read()
    if token != token_request:
        output = {
            'status': False,
            'result': {
                'msg': 'Token error'
            }
        }
        return JsonResponse(output, safe=False)

    function_name = request_data['function_name']
    args = request_data['arguments']
    if function_name in methods:
        output = methods[function_name](args)
        return JsonResponse(output, safe=False)
    else:
        output = {
            'status': False,
            'result': {
                'msg': 'Function no exist'
            }
        }
        return JsonResponse(output, safe=False)

