
from django.shortcuts import render, get_list_or_404
from .models import CurrencyData, DataFile


def home(request):
    return render(request, 'app/home.html')


def about_us(request):
    return render(request, 'app/about_us.html')


def profile(request):
    user_data = {
        'id': '880',
        'balance': '1000.00',
        'currency': 'GBP',
        'ip': '195.325.214.2',
        'last_login': '2020-12-14 15:47:15',
        'email': 'test.account@treasuryquants.com',
    }

    context = {
        'user_data': user_data
    }

    return render(request, 'app/profile.html', context)


def policy_notice(request):
    return render(request, 'app/policy_notice.html')


def terms_service(request):
    return render(request, 'app/terms.html')