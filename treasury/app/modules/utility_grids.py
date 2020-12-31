from TQapis import TQRequests, TQConnection, TQAPIUtilities  # version 0.12.2 and above
import settings
import requests
import json
import  datetime




def utility_download_formatted_grid_swap_rates(connection, currencies, folder):
    try:
        if not TQAPIUtilities.connection_is_ok(connection):
            return (False, {'utility_download_formatted_grid_swap_rates': 'failed on connection_is_ok(connection)'})

        request_describe = TQRequests.request_function_show_available("asof_dates")
        message = connection.send(request_describe)

        #
        # Obtain all available dates
        #
        if not message.is_OK:
            return (False, {'utility_download_formatted_grid_swap_rates': 'failed on connection.send'})

        asof_dates = connection.response.results

        if len(asof_dates) < 2:
            return (False, {'utility_download_formatted_grid_swap_rates': 'too few dates'})

        #initialize the two dates
        to_date = '19000101'
        from_date = to_date
        #
        # Pick the most recent dates
        #
        for key, value in asof_dates.items():
            if value > to_date:
                to_date = value
            elif value < to_date and value > from_date:
                from_date = value

        #
        # Create a csv file for each currency
        #
        for currency in currencies:
            status, results = TQAPIUtilities.formatted_grid_swap_rates(connection, from_date, to_date, currency)
            if not status:
                return (False, {
                    'utility_download_formatted_grid_swap_rates': ' failed with from_date={}, to_date={} and currency={}'.format(from_date, to_date, currency)})
            lines=[]
            for key,value in results.items():
                line = key+","+value+"\n"
                lines.append(line)

                path=folder+currency.upper()+".csv"
                file=open(path,'w')
                file.writelines(lines)
                file.close()
    except Exception as e:
        return (False, {
            'utility_download_formatted_grid_swap_rates': 'failed while saving file with from_date={}, to_date={} and currency={}. Exception was {}'.format(from_date, to_date, currency, e)})


    return (True, dict())

def utility_download_formatted_grid_fx( currencies, base_currency,folder):

    try:

        latest_url =("https://api.exchangeratesapi.io/latest?base={}").format(base_currency.upper())

        results=requests.get(latest_url)
        latest_dictionary=dict()
        latest_dictionary=json.loads(results.text)['rates']
        formatted_date_latest=json.loads(results.text)['date']
        latest_date= datetime.datetime.strptime(formatted_date_latest,"%Y-%m-%d")

        previous_dictionary = dict()
        for i in range(1,5):
            previous_date=latest_date - datetime.timedelta(days=i)
            formattted_previous_date=previous_date.strftime("%Y-%m-%d")
            previous_url ="https://api.exchangeratesapi.io/history?start_at={}&end_at={}&base={}".format(formattted_previous_date,formattted_previous_date,base_currency.upper())
            results=requests.get(previous_url)
            previous_dictionary=json.loads(results.text)['rates']
            if len(previous_dictionary)>0:
                previous_dictionary=json.loads(results.text)['rates'][formattted_previous_date]
                break


        if len(previous_dictionary)==0:
            return (False, {'utility_download_formatted_grid_fx': 'failed retriving FX rates '})

        previous_dictionary[base_currency.upper()]=1.00
        latest_dictionary[base_currency.upper()]=1.00
        #
        # print title and heading
        #
        lines=list()
        line = "title,1 " + base_currency.upper() + "\n"
        lines.append(line)
        line = "headings,latest, " + previous_date.strftime("%Y%m%d") + ",change(%)\n"
        lines.append(line)

        for currency in currencies:
            currency=currency.upper()
            v0=previous_dictionary[currency]
            v1=latest_dictionary[currency]
            diff=(v1/v0-1)
            line = currency+","+str(v1)+","+str(v0)+","+str(diff)+"\n"
            lines.append(line)

            path=folder+"FX.csv"
            file=open(path,'w')
            file.writelines(lines)
            file.close()
    except Exception as e:
        return (False, {
            'utility_download_formatted_grid_fx': 'failed while saving file with base_currency={} and folder={}. Exception was {}'.format( base_currency,folder, e)})


    return (True, dict())

