#!/var/www/treeio/venv/bin/python

import os
import sys

sys.path = ['/var/www/treeio/venv/lib/python2.7/site-packages/'] + sys.path

sys.path.append('/var/www/treeio/')
sys.path.append("/var/www/")

os.environ['DJANGO_SETTINGS_MODULE'] = 'treeio.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

