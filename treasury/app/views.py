import csv

from django.shortcuts import render, get_list_or_404

from .models import CurrencyData, DataFile

files = [
    'app/media/currency_data/EUR.csv',
    'app/media/currency_data/USD.csv',
    'app/media/currency_data/GBP.csv',
    'app/media/currency_data/CHF.csv',
    'app/media/currency_data/FX.csv',
    'app/media/currency_data/JPY.csv',
]

def read_data(file_path):
    with open(file_path, 'rt') as f:
        data = csv.reader(f)
        result = []
        for row in data:
            result.append(row)
        obj = CurrencyData(result[0][1], result[1], result[2:])
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


def search(request):
    pass
