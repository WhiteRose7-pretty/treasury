from django.shortcuts import render, get_list_or_404
from .models import CurrencyData, DataFile
from .modules import settings
from .modules import utility_grids
from .modules import apis
from .modules import utility_connection
from app.modules.apis_for_json import web_api
import json
from .modules import sandbox
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


def home(request):
    print(sandbox.account_active())
    return render(request, 'app/home.html')


def login(request):
    if request.session['login']:
        return HttpResponseRedirect(reverse('app:profile'))
    return render(request, 'app/login.html')


def logout(request):
    request.session['login'] = False
    request.session['user_email'] = ''
    request.session['password'] = ''
    return HttpResponseRedirect(reverse('app:login'))


def about_us(request):
    return render(request, 'app/about_us.html')


def profile(request):
    #
    # Connection to the server. Contains and updates its own  token
    #
    if not request.session['login']:
        return HttpResponseRedirect(reverse('app:login'))

    post_data = {
        'function_name': 'account_profile',
        'arguments': {
            'user_email': request.session['user_email'],
            'password': request.session['password'],
        },
        'source_caller': 'front-end-function10',
    }
    result = web_api(json.dumps(post_data))
    result_dic = json.loads(result)
    context = {
        'result_dic': result_dic,
    }

    return render(request, 'app/profile.html', context)


def policy_notice(request):
    return render(request, 'app/policy_notice.html')


def terms_service(request):
    return render(request, 'app/terms.html')


def call_web_api(request):
    data = json.loads(request.body)
    post_data = json.dumps(data)
    result = web_api(post_data)
    result_dic = json.loads(result)
    if result_dic['source_caller'] == 'account_profile':
        if result_dic['error'] == '' and result_dic['results']['id']:
            request.session['login'] = True
            request.session['user_email'] = data['arguments']['user_email']
            request.session['password'] = data['arguments']['password']
        else:
            request.session['login'] = False
            request.session['user_email'] = ''
            request.session['password'] = ''

    return JsonResponse(result_dic)


def password_reset(request):
    return render(request, 'app/password_reset.html')


def password_reset_call_back(request):
    key = request.GET.get("activation_key", False)
    if not key:
        return HttpResponseRedirect(reverse('app:invalid_page-call'))

    post_data = {
        'function_name': 'account_activation_key_status',
        'arguments': {
            'activation_key': key,
        },
        'source_caller': 'password_reset_call_back_function',
    }
    result = web_api(json.dumps(post_data))
    print(result)
    result_dic = json.loads(result)
    context = {
        'result_dic': result_dic,
        'key': key,
    }
    return render(request, 'app/password-reset-call-back.html', context)


def invalid_page_call(request):
    return render(request, 'app/invalid_page.html')