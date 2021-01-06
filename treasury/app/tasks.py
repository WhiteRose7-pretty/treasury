from celery.task.schedules import crontab
from celery.decorators import periodic_task
from app.modules import sandbox


@periodic_task(run_every=(crontab(minute='*/15')))
def main():
    try:
        status = sandbox.download_fx_data()
    except:
        status = False
    return status
