from django import template
import csv
from app.models import CurrencyData

register = template.Library()


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


@register.simple_tag
def string_float(str):
    try:
        val = float(str)
    except:
        val = str
    return val


@register.simple_tag
def get_market_data():
    data_list = []
    for item in files:
        obj = read_data(item)
        data_list.append(obj)
    return data_list