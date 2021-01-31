from django.shortcuts import render
import app.modules.apis_for_json as apis_for_json
import json
from .modules import sandbox, utility_common, settings
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from app.templatetags.app_tags import get_market_data
from app.modules import cron_grids


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
    context = {
        'navbar': 'workbench',
        'user_email': request.session['user_email'],
        'target_url': settings.url_server
    }
    return render(request, 'app/workbench.html', context)


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


def fx_data_graph(request):
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
    utility_common.process_fatal_error(request.body.decode('utf-8'), settings.is_development)
    return JsonResponse('success', safe=False)


def cron_test(request):
    status = cron_grids.download_rates_data()
    print(status)
    context = {
        'navbar': 'terms',
    }
    return render(request, 'app/terms.html', context)
