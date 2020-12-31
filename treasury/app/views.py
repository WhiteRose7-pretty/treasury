
from django.shortcuts import render, get_list_or_404
from .models import CurrencyData, DataFile
from .modules import settings



def home(request):
    return render(request, 'app/home.html')

def read_data(file_path):
    with open(file_path, 'rt') as f:
        data = csv.reader(f)
        result = []
        row_count=0
        for row in data:
            #
            # Capitalized the heading
            #
            if row_count==0:
               row[1]=  row[1].upper()
            #
            # adjust the decimals
            #
            if row_count>1:
                row[1] = "{:.4f}".format(round(float(row[1]), settings.grid_decimals))
                row[2] = "{:.4f}".format(round(float(row[2]), settings.grid_decimals))
                row[3] = "{:.4f}".format(round(float(row[3]), settings.grid_decimals))

            result.append(row)
            row_count+=1
        obj = CurrencyData(result[0][1], result[1], result[2:])
        obj.head_data[0] = ''
        return obj



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