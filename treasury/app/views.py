from django.shortcuts import render
import app.modules.apis_for_json as apis_for_json
import json
from .modules import sandbox, utility_common, settings
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from app.templatetags.app_tags import get_market_data
from app.modules import cron_grids
from app.models import ApiStatus


def home(request):
    context = {
        'navbar': 'home',
    }
    return render(request, 'app/home.html', context)


def about_us(request):
    context = {
        'navbar': 'about_us',
    }
    return render(request, 'app/about_us.html', context)


def workbench(request):
    api_names = ['price_fx_forward',
                 'price_vanilla_swap',
                 'price',
                 'risk_ladder',
                 'pnl_attribute',
                 'pnl_predict',
                 'market_swap_rates',
                 'market_fx_rates',
                 'describe',
                 'show_available']

    descriptions = utility_common.get_workbench_descriptions_json_string(api_names)
    user_email = ''
    if 'user_email' in request.session:
        user_email = request.session['user_email']

    context = {
        'navbar': 'workbench',
        'user_email': user_email,
        'target_url': settings.url_server,
        'target_ip': settings.target_url,
        'descriptions': json.dumps(descriptions)
    }

    return render(request, 'app/workbench.html', context)


def workbench2(request):
    api_names = ['price_fx_forward',
                 'price_vanilla_swap',
                 'price',
                 'risk_ladder',
                 'pnl_attribute',
                 'pnl_predict',
                 'market_swap_rates',
                 'market_fx_rates',
                 'describe',
                 'show_available']

    descriptions = utility_common.get_workbench_descriptions_json_string(api_names)
    user_email = ''
    if 'user_email' in request.session:
        user_email = request.session['user_email']
    arrays = range(1, 8)

    context = {
        'navbar': 'workbench',
        'user_email': user_email,
        'target_url': settings.url_server,
        'target_ip': settings.target_url,
        'descriptions': json.dumps(descriptions),
        'list': arrays,
    }

    return render(request, 'app/workbench2.html', context)


def policy_notice(request):
    context = {
        'navbar': 'policy_notice',
    }
    return render(request, 'app/policy_notice.html', context)


def terms_service(request):
    context = {
        'navbar': 'terms',
    }
    return render(request, 'app/terms.html', context)


def rates_data_graph(request):
    query = get_market_data()
    query_temp = [
        {
            "title": item.title,
            "tenor": item.tenors,
            "legend1": item.head_data[1],
            "legend2": item.head_data[2],
            "data1": item.data1,
            "data2": item.data2,
        }
        for item in query]
    json_string = json.dumps({'data': query_temp})

    return JsonResponse(json_string, safe=False)


def api_gateway(request):
    data = json.loads(request.body)
    post_data = json.dumps(data)
    result = apis_for_json.api_gateway(post_data, apis_for_json.general_apis_factory)
    result_dic = json.loads(result)
    return JsonResponse(result_dic, safe=False)


def post_message(request):
    data = request.body.decode('utf-8')
    subject = request.POST.get('subject', 'post message')
    message = request.POST.get('message', data)
    utility_common.process_fatal_error(subject, message, settings.is_development)
    return JsonResponse('success', safe=False)


def cron_test(request):
    (status, result) = cron_grids.download_rates_data()
    print(status, result)
    context = {
        'navbar': 'terms',
    }
    return render(request, 'app/terms.html', context)


def connection_test(request):
    (status, error) = cron_grids.check_connection()
    print(status, error)
    context = {
        'navbar': 'terms',
    }
    return render(request, 'app/terms.html', context)
