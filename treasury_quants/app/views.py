from django.shortcuts import render
import json
from app.modules import utility_common, settings, cron_grids
from django.http import JsonResponse
from app.templatetags.app_tags import get_market_data


# Market page, title: Swap & FX Market Rates
def home(request):
    context = {
        'navbar': 'Swap & FX Market Rates',
    }
    return render(request, 'app/home.html', context)


def about_us(request):
    context = {
        'navbar': 'About us',
    }
    return render(request, 'app/about_us.html', context)


def workbench(request):
    api_names = ['price_fx_forward',
                 'price_vanilla_swap',
                 'price',
                 'risk_ladder',
                 'pnl_attribute',
                 'pnl_predict',
                 'workspace_list',
                 'workspace_read',
                 'workspace_delete',
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
        'navbar': 'Workbench',
        'user_email': user_email,
        'target_url': settings.url_server,
        'target_ip': settings.target_url,
        'descriptions': json.dumps(descriptions),
        'list': arrays,
    }

    return render(request, 'app/workbench.html', context)


def policy_notice(request):
    context = {
        'navbar': 'Policy Notice',
    }
    return render(request, 'app/policy_notice.html', context)


def terms_service(request):
    context = {
        'navbar': 'Terms of Service',
    }
    return render(request, 'app/terms.html', context)


# This function is used to loading graph data In Market page with Ajax,post request.
# If request is not Ajax, not post, return 404 error.
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


def post_message(request):
    subject = request.POST.get('subject', 'post message')
    message = request.POST.get('message', '')
    utility_common.process_fatal_error(subject, message, settings.path_error_file, settings.email_webmaster,
                                       settings.is_development)
    return JsonResponse('success', safe=False)


def handler404(request, exception):
    context = {
        'navbar': '400 Error',
        'message': 'This page doesn’t exist. Please check your URL or return to Treasury Quants home.',
    }
    return render(request, 'app/error_page.html', context, status=404)


def handler500(request):
    context = {
        'navbar': '500 Error',
        'message': 'This page doesn’t exist. Please check your URL or return to Treasury Quants home.',
    }
    return render(request, 'app/error_page.html', context,status=500)


def test_connection(request):
    status, error = cron_grids.check_connection()
    print("check connection:")
    print(status, error)
    context = {
        'navbar': 'Terms of Service',
    }
    return render(request, 'app/terms.html', context)


def server_down(request):
    context = {
        'navbar': 'Server Error',
        'message': 'Server is down. Please try again later.',
    }
    return render(request, 'app/error_page.html', context)

