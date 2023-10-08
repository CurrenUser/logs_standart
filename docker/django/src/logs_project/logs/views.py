import pytz as pytz
from django.http import HttpResponse
import logging, datetime

logger = logging.getLogger('my_info')

def index(request):
    logger.info('Request to logs url', extra={'level': 'INFO', 'time': datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%dT%H:%M:%S')})
    return HttpResponse('Hello world')