from django.db import models


class CurrencyData:
    def __init__(self, title, head_data, data, tenors, data1=None, data2=None):
        if data2 is None:
            data2 = []
        if data1 is None:
            data1 = []
        self.title = title
        self.head_data = head_data
        self.data = data
        self.tenors = tenors
        self.data1 = data1
        self.data2 = data2
