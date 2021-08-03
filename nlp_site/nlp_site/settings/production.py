from nlp_site.settings.common import *
import os
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
