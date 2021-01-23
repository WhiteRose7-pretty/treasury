from django.shortcuts import render, get_list_or_404
from .models import CurrencyData, DataFile
from .modules import settings
from .modules import utility_grids
from .modules import apis
from .modules import utility_connection
import app.modules.apis_for_json   as apis_for_json
import json
from .modules import sandbox
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from app.templatetags.app_tags import get_market_data
from django.core import serializers


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