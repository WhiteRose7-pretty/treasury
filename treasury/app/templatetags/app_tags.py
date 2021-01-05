from django import template
from app.models import CurrencyData
from app.modules import utility_grids
from app.modules import settings

register = template.Library()

swap_rate_files = [
    'app/media/currency_data/EUR.csv',
    'app/media/currency_data/USD.csv',
    'app/media/currency_data/GBP.csv',
    'app/media/currency_data/CHF.csv',
    'app/media/currency_data/FX.csv',  #todo: shahram to remove this entry once the front-end FX is accessing its own data
    'app/media/currency_data/JPY.csv',
]

files = [
    'app/media/currency_data/EUR.csv',
    'app/media/currency_data/USD.csv',
    'app/media/currency_data/GBP.csv',
    'app/media/currency_data/CHF.csv',
    'app/media/currency_data/FX.csv',
    'app/media/currency_data/JPY.csv',
]


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