from django.shortcuts import render, get_list_or_404
from .models import CurrencyData, DataFile
from .modules import settings
from .modules import utility_grids
from .modules import apis
from .modules import utility_connection
from app.modules.apis_for_json import account_api
import json
from .modules import sandbox
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from app.templatetags.app_tags import get_market_data
from django.core import serializers


def home(request):
    return render(request, 'app/home.html')


def about_us(request):
    return render(request, 'app/about_us.html')


def policy_notice(request):
    return render(request, 'app/policy_notice.html')


def terms_service(request):
    return render(request, 'app/terms.html')


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
