from django import template
from app.models import CurrencyData, ApiStatus
from app.modules import utility_grids
from app.modules import settings
from app.modules import cron_grids

register = template.Library()

swap_rate_files = [
    'app/media/currency_data/USD.csv',
    'app/media/currency_data/GBP.csv',
    'app/media/currency_data/EUR.csv',
    'app/media/currency_data/CHF.csv',
    'app/media/currency_data/JPY.csv',
]

fx_file = 'app/media/currency_data/FX.csv'


@register.simple_tag
def get_development_status():
    return settings.is_development


@register.simple_tag
def get_api_status():
    print(cron_grids.api_status_from_file(settings.api_status_path))
    return cron_grids.api_status_from_file(settings.api_status_path)

def read_data(file_path):
    obj = CurrencyData('', ['', '', ''], [[0, 0, 0, 0]], [0],
                       [0])  # to ensure we do not crash and we always return something
    grid = utility_grids.Grid()
    status, message = grid.load(file_path)
    if not status:
        return obj
    elements = list()
    tenors = list()  # for graph
    data1 = list()  # for graph
    data2 = list()  # for graph

    for i in range(0, len(grid.y1)):
        tenor = grid.tenors[i]
        col1 = "{:.4f}".format(round(float(grid.y1[i]), settings.grid_decimals))
        col2 = "{:.4f}".format(round(float(grid.y2[i]), settings.grid_decimals))
        col3 = "{:.4f}".format(round(float(grid.y3[i]), settings.grid_decimals))

        elements.append([tenor, col1, col2, col3])
        tenors.append(tenor)
        data1.append(col1)
        data2.append(col2)
    obj = CurrencyData(grid.title, grid.headings, elements, tenors, data1, data2)
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
def get_swap_rates_data():
    data_list = []
    for item in swap_rate_files:
        obj = read_data(item)
        data_list.append(obj)
    return data_list


@register.simple_tag
def get_fx_rates_data():
    obj = read_data(fx_file)
    return obj


@register.simple_tag
def get_market_data():
    return get_swap_rates_data()


@register.simple_tag
def get_element_array_index(array, index):
    return array[index]


@register.simple_tag
def check_navbar(navbar, page_name):
    if navbar == page_name:
        return 'active'
    else:
        return ''


@register.simple_tag
def authenticated(request):
    if request.session.get('login', False):
        return True
    return False
