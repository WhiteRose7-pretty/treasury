from django.shortcuts import render
from app.modules.apis_for_json import api_gateway
import json
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


def home(request):
    return HttpResponseRedirect(reverse('account_cycle:login'))


def login(request):
    context = {
        'navbar': 'Login'
    }
    if request.session.get('login', False):
        return HttpResponseRedirect(reverse('account_cycle:profile'))
    return render(request, 'account_cycle/login.html', context)


def logout(request):
    request.session['login'] = False
    request.session['user_email'] = ''
    request.session['password'] = ''
    return HttpResponseRedirect(reverse('account_cycle:login'))


def profile(request):
    if not request.session.get('login', False):
        return HttpResponseRedirect(reverse('account_cycle:login'))

    post_data = {
        'function_name': 'account_profile',
        'arguments': {
            'user_email': request.session['user_email'],
            'password': request.session['password'],
        },
        'source_caller': 'front-end-function10',
    }
    result = api_gateway(json.dumps(post_data))
    result_dic = json.loads(result)

    icons = ['user', 'credit-card', 'dollar-sign', 'share-2', 'clock']
    context = {
        'navbar': 'My Account',
        'result_dic': result_dic,
        'user_email': request.session['user_email'],
        'password': request.session['password'],
        'icons': icons,
        'current_ip': get_client_ip(request)
    }

    return render(request, 'account_cycle/profile.html', context)


def call_account_api(request):
    data = json.loads(request.body)
    post_data = json.dumps(data)
    result = api_gateway(post_data)
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
    context = {
        'navbar': "Password Reset"
    }
    return render(request, 'account_cycle/password_reset.html', context)


def check_activation_key(key):
    post_data = {
        'function_name': 'account_activation_key_status',
        'arguments': {
            'activation_key': key,
        },
        'source_caller': 'password_reset_call_back_function',
    }
    result = api_gateway(json.dumps(post_data))
    print(result)
    result_dic = json.loads(result)
    if result_dic['error']:
        output_str = result_dic['error']
    elif result_dic['results']['is_exist'] == 'False':
        output_str = 'The key is not exist.'
    elif result_dic['results']['is_active'] == 'False':
        output_str = 'The key expired.'
    else:
        output_str = ''

    if output_str != '':
        input_disabled = 'disabled'
    else:
        input_disabled = ''

    return output_str, input_disabled


def password_reset_call_back(request):
    key = request.GET.get("activation_key", False)

    if not key:
        return HttpResponseRedirect(reverse('account_cycle:invalid_page-call'))

    result_dic, input_disabled = check_activation_key(key)

    context = {
        'navbar': "Password Reset",
        'result_dic': result_dic,
        'key': key,
        'input_disabled': input_disabled
    }
    return render(request, 'account_cycle/password-reset-call-back.html', context)


def invalid_page_call(request):
    context = {
        'navbar': "Invalid Page",
    }
    return render(request, 'account_cycle/invalid_page.html', context)


def create_account(request):
    context = {
        'navbar': 'Create Account'
    }
    return render(request, 'account_cycle/create_account.html', context)


def account_activation_callback(request):
    key = request.GET.get("activation_key", False)
    if not key:
        return HttpResponseRedirect(reverse('account_cycle:invalid_page-call'))

    result_dic, input_disabled = check_activation_key(key)
    context = {
        'navbar': 'Activate Account',
        'result_dic': result_dic,
        'key': key,
    }
    return render(request, 'account_cycle/account-activation-callback.html', context)


def confirm_email_activate_account(request):
    context = {
        'navbar': 'Activate Account',
    }
    return render(request, 'account_cycle/confirm-email-activate-account.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



