import csv

from django.shortcuts import render, get_list_or_404

from .models import CurrencyData, DataFile
from .modules import settings
from .modules import utility_grids

files = [
    'app/media/currency_data/EUR.csv',
    'app/media/currency_data/USD.csv',
    'app/media/currency_data/GBP.csv',
    'app/media/currency_data/CHF.csv',
    'app/media/currency_data/FX.csv',
    'app/media/currency_data/JPY.csv',
]

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
    data_list = []
    for item in files:
        obj = read_data(item)
        data_list.append(obj)
    context = {
        'currency_data' : data_list,
    }
    return render(request, 'app/home.html', context)

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


def search(request):
    pass
