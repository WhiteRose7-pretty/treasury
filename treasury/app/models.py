from django.db import models


class CurrencyData:
    def __init__(self, title, head_data, data, tenors, data1=[], data2=[]):
        self.title = title
        self.head_data = head_data
        self.data = data
        self.tenors = tenors
        self.data1 = data1
        self.data2 = data2


class DataFile(models.Model):
    csv_file = models.FileField(upload_to='currency_data')

    class Meta:
        verbose_name = 'Currrency File'
        verbose_name_plural = 'Currency File'

    def __str__(self):
        return self.csv_file.name
