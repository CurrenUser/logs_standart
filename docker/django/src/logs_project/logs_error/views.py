import pytz as pytz
from django.http import HttpResponse
import logging, datetime

logger = logging.getLogger('my_errors')

def index(request):
    logger.error('AHTUNG AHTUNG AHTUNG',extra={'level': 'ERROR', 'time': datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%dT%H:%M:%S')})
    return HttpResponse(status=500)