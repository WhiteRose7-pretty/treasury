import csv

from django.shortcuts import render, get_list_or_404

from .models import CurrencyData, DataFile
from .modules import settings
from .modules import utility_grids
from .modules import apis
from TQapis import TQConnection

#
# location of the swap rates files
#
swap_rate_files = [
    'app/media/currency_data/EUR.csv',
    'app/media/currency_data/USD.csv',
    'app/media/currency_data/GBP.csv',
    'app/media/currency_data/CHF.csv',
    'app/media/currency_data/FX.csv',  #todo: shahram to remove this entry once the front-end FX is accessing its own data
    'app/media/currency_data/JPY.csv',
]

#
# location of the fx rates single file
#
fx_rate_file = 'app/media/currency_data/FX.csv'  # this is where the fx is going to be


#
# Global connection to the server. Contains and updates its own  token
#
connection=TQConnection.Connection(settings.email_default,settings.url_server)



#todo: Shahram to remove this after a discusison with Daria.
def read_data_old(file_path):
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
                row[1] = "{:.4f}".format(round(float(row[1]),settings.grid_decimals))
                row[2] = "{:.4f}".format(round(float(row[2]), settings.grid_decimals))
                row[3] = "{:.4f}".format(round(float(row[3]), settings.grid_decimals))

            result.append(row)
            row_count+=1
        obj = CurrencyData(result[0][1], result[1], result[2:])
        obj.head_data[0] = ''
        return obj

def read_data(file_path):
    obj=CurrencyData('', ['','',''], [[0,0,0,0]]) #to ensure we do not crash and we always return something
    grid=utility_grids.Grid()
    status, message=grid.load(file_path)
    if not status:
        return obj
    elements=list()
    for i in range(0,len(grid.y1)):
        tenor = grid.tenors[i]
        col1 = "{:.4f}".format(round(float(grid.y1[i]),settings.grid_decimals))
        col2 = "{:.4f}".format(round(float(grid.y2[i]), settings.grid_decimals))
        col3 = "{:.4f}".format(round(float(grid.y3[i]), settings.grid_decimals))

        elements.append([tenor,col1,col2,col3])
    obj = CurrencyData(grid.title, grid.headings, elements)
    obj.head_data[0] = ''

    return obj


def home(request):
    swap_rates_data_list = []
    for item in swap_rate_files:
        swap_rates_data_obj = read_data(item)
        swap_rates_data_list.append(swap_rates_data_obj)

    fx_rates_data_obj=read_data(fx_rate_file)

    context = {
        'currency_data' : swap_rates_data_list,
        'fx_rates_data' : fx_rates_data_obj
    }
    return render(request, 'app/home.html', context)



def profile(request):


    our_test_account_email='test.account@treasuryquants.com'
    our_test_account_password='test.account@treasuryquants.com'

    anonymous = {
        'id': '880',
        'balance': '0.00',
        'currency': 'GBP',
        'ip': '0.0.0.0',
        'last_login': '1900-01-01 00:00:00',
        'email': "" #empty email means anonymous
    }

    user_data=anonymous
    status, results=apis.account_profile(connection,our_test_account_email,our_test_account_password)
    if status:
        user_data['id']=results['id']
        user_data['balance']=results['balance']
        user_data['ip']=results['ip']
        user_data['last_login']=results['last_login']
        user_data['currency']=results['currency'].upper()



    context = {
        'user_data': user_data
    }

    return render(request, 'app/profile.html', context)


def search(request):
    pass
