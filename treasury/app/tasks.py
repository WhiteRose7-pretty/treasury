from celery.task.schedules import crontab
from celery.decorators import periodic_task
from app.modules import cron_grids
import datetime
import pytz
from app.models import ApiStatus


@periodic_task(run_every=(crontab(minute='*/15')))
def main():
    try:
        status = cron_grids.download_fx_data()
    except:
        status = False
    return status


@periodic_task(run_every=(crontab(minute='*/5')))
def check_connection():
    (status, error) = cron_grids.check_connection()
    api_status = ApiStatus.objects.first()
    if api_status:
        api_status.status = status
    else:
        api_status = ApiStatus()
        api_status.status = status
    api_status.save()
    return status, error


@periodic_task(run_every=(crontab(minute='*/180')))
def download_rates_data():
    return cron_grids.download_rates_data()


def check_hour(set_hour, time_zone):
    tz = pytz.timezone(time_zone)
    london_now = datetime.datetime.now(tz)
    current_hour = london_now.hour
    if current_hour == set_hour:
        return True
    return False

