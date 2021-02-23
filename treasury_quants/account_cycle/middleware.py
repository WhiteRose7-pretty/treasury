from django.urls import resolve
from app.modules import settings
from app.modules import cron_grids
from django.http import HttpResponseRedirect
from django.urls import reverse


class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)


class ProcessViewNoneMiddleware(BaseMiddleware):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.resolver_match.app_name == 'account_cycle':
            if not cron_grids.api_status_from_file(settings.api_status_path):
                return HttpResponseRedirect(reverse('app:server_down'))
        return None
