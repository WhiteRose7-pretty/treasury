from TQapis import TQRequests
import requests
import json
import datetime
import os
import csv
from . import apis
from . import utility_common


#
# A grid class owning the format of the grid structure. All changes will be inside here
#
class Grid:
    def _clear(self):
        self.file_path = ""
        self.title = ""
        self.headings = list()
        self.tenors = list()
        self.y1 = list()
        self.y2 = list()
        self.y3 = list()

    def __init__(self):
        self._clear()

    def load(self, file_path):
        self._clear()
        self.file_path = file_path
        try:
            f = open(self.file_path, 'rt')
            data = csv.reader(f)
            row_count = 0
            for row in data:
                if row_count == 0:  # title
                    self.title = row[1].upper()
                elif row_count == 1:  # headings
                    self.headings.append(row[0])
                    self.headings.append(row[1])
                    self.headings.append(row[2])
                    self.headings.append(row[3])
                else:  # body
                    self.tenors.append(row[0])
                    self.y1.append(float(row[1]))
                    self.y2.append(float(row[2]))
                    self.y3.append(float(row[3]))
                row_count += 1
            return (True, '')
        except Exception as e:
            return (False, str(e))

    def save_as(self, path):
        lines = list()
        line = "title," + self.title + "\n"
        lines.append(line)
        line = utility_common.list_to_csv(
            self.headings) + "\n"  # titles,latest, " + previous_date.strftime("%Y%m%d") + ",change(%)\n"
        lines.append(line)

        for i in range(0, len(self.y1)):
            line = str(self.tenors[i]) + "," + str(self.y1[i]) + "," + str(self.y2[i]) + "," + str(self.y3[i]) + "\n"
            lines.append(line)
        try:
            file = open(path, 'w')
            file.writelines(lines)
            file.close()
            return True, ''
        except Exception as e:
            return False, str(e)





def utility_download_formatted_grid_swap_rates(connection, currencies, tenors, folder):
    try:
        if not apis.connection_is_ok(connection):
            return (False, {'utility_download_formatted_grid_swap_rates': 'failed on connection_is_ok(connection)'})
        #
        # Obtain all available dates
        #
        request_describe = TQRequests.request_function_show_available("asof_dates")
        message = connection.send_web(request_describe)
        print(message.content)
        if not message.is_OK:
            return False, {'utility_download_formatted_grid_swap_rates': message.content}
        asof_dates = connection.response.results
        if len(asof_dates) < 2:
            return (False, {'utility_download_formatted_grid_swap_rates': 'too few dates'})

        #
        # pick the two most available dates
        #
        # initialize the two dates
        to_date = '19000101'
        from_date = to_date

        for key, value in asof_dates.items():
            if value > to_date:
                to_date = value
            elif value < to_date and value > from_date:
                from_date = value

        #
        # Create a grid for each currency and sage it in a csv file
        #
        for currency in currencies:

            status, results = apis.formatted_grid_swap_rates(connection, from_date, to_date, currency, tenors)

            if not status:
                return (False, {
                    'utility_download_formatted_grid_swap_rates': ' failed with from_date={}, to_date={} and currency={}'.format(
                        from_date, to_date, currency)})
            lines = []

            grid = Grid()
            path = os.path.join(folder, currency.upper() + ".csv")
            grid.headings.append("headings")
            for key, value in results.items():
                if 'title' in key:
                    grid.title = value
                elif 'headings' in key:
                    grid.headings.append(value)
                else:
                    tokens = value.split(",")
                    grid.tenors.append(key)
                    grid.y1.append(tokens[0])
                    grid.y2.append(tokens[1])
                    grid.y3.append(tokens[2])
            status, message = grid.save_as(path)
            if not status:
                return (False, {
                    'utility_download_formatted_grid_fx': 'failed while saving file with base_currency={} and folder={}. Exception was {}'.format(
                        currency, folder, message)})


    except Exception as e:
        return (False, {
            'utility_download_formatted_grid_swap_rates': 'failed with the following exception {}'.format(e)})

    return (True, dict())


def utility_download_formatted_grid_fx(currencies, base_currency, folder):
    try:

        latest_url = ("https://api.exchangeratesapi.io/latest?base={}").format(base_currency.upper())

        results = requests.get(latest_url)
        latest_dictionary = dict()
        latest_dictionary = json.loads(results.text)['rates']
        formatted_date_latest = json.loads(results.text)['date']
        latest_date = datetime.datetime.strptime(formatted_date_latest, "%Y-%m-%d")

        previous_date = latest_date
        previous_dictionary = dict()
        for i in range(1, 5):
            previous_date = latest_date - datetime.timedelta(days=i)
            formattted_previous_date = previous_date.strftime("%Y-%m-%d")
            previous_url = "https://api.exchangeratesapi.io/history?start_at={}&end_at={}&base={}".format(
                formattted_previous_date, formattted_previous_date, base_currency.upper())
            results = requests.get(previous_url)
            previous_dictionary = json.loads(results.text)['rates']
            if len(previous_dictionary) > 0:
                previous_dictionary = json.loads(results.text)['rates'][formattted_previous_date]
                break

        if len(previous_dictionary) == 0:
            return (False, {'utility_download_formatted_grid_fx': 'failed retriving FX rates '})

        previous_dictionary[base_currency.upper()] = 1.00
        latest_dictionary[base_currency.upper()] = 1.00
        #
        # populate the grid object
        #

        grid = Grid()
        grid.title = "1 " + base_currency.upper()
        grid.headings = ["headings", "latest", previous_date.strftime("%Y%m%d"), "change(%)"]

        for currency in currencies:
            currency = currency.upper()
            v1 = latest_dictionary[currency]
            v2 = previous_dictionary[currency]
            diff = (v1 / v2 - 1)
            grid.tenors.append(currency.upper())
            grid.y1.append(v1)
            grid.y2.append(v2)
            grid.y3.append(diff)

        path = folder + "FX.csv"

        status, message = grid.save_as(path)
        if not status:
            return (False, {
                'utility_download_formatted_grid_fx': 'failed while saving file with base_currency={} and folder={}. Exception was {}'.format(
                    base_currency, folder, message)})


    except Exception as e:
        return (False, {
            'utility_download_formatted_grid_fx': 'failed while extracting information with base_currency:{} and folder:{}. Exception was {}'.format(
                base_currency, folder, e)})

    return (True, dict())
