from celery.task.schedules import crontab
from celery.decorators import periodic_task
from app.modules import cron_grids


@periodic_task(run_every=(crontab(minute='*/5')))
def main():
    try:
        status = cron_grids.download_fx_data()
    except:
        status = False
    return status
