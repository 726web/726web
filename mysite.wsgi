# coding:utf-8

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTING_MODULE","mysite.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
