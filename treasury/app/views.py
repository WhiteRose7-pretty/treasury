from django.shortcuts import render, get_list_or_404
from .models import CurrencyData, DataFile
from .modules import settings
from .modules import utility_grids
from .modules import apis
from .modules import utility_connection
from app.modules.apis_for_json import web_api
import json
from .modules import sandbox


def home(request):
    return render(request, 'app/home.html')


def login(request):
    if request.method == 'POST':
        post_data = {
            'function_name': 'account_profile',
            'arguments': {
                'user_email': request.POST.get('email'),
                'password': request.POST.get('password'),
            },
            'source_caller': 'front-end-function10',
        }
        r = json.dumps(post_data)
        result = web_api(r, True)
        result_dic = json.loads(result)

        context = {
            'result_dic': result_dic
        }

    else:
        context = {
         'result_dic': False
        }

    return render(request, 'app/login.html', context)


def about_us(request):
    return render(request, 'app/about_us.html')


def profile(request):
    #
    # Connection to the server. Contains and updates its own  token
    #
    connection = utility_connection.WebConnection(settings.email_default, settings.url_server, settings.token_path)

    our_test_account_email = 'test.account@treasuryquants.com'
    our_test_account_password = 'test.account@treasuryquants.com'

    anonymous = {
        'id': '880',
        'balance': '0.00',
        'currency': 'GBP',
        'ip': '0.0.0.0',
        'last_login': '1900-01-01 00:00:00',
        'email': ""  # empty email means anonymous
    }

    user_data = anonymous
    status, results = apis.account_profile(connection, our_test_account_email, our_test_account_password)
    if status:
        user_data['id'] = results['id']
        user_data['balance'] = results['balance']
        user_data['ip'] = results['ip']
        user_data['last_login'] = results['last_login']
        user_data['currency'] = results['currency'].upper()

    context = {
        'user_data': user_data
    }

    return render(request, 'app/profile.html', context)


def policy_notice(request):
    return render(request, 'app/policy_notice.html')


def terms_service(request):
    return render(request, 'app/terms.html')
