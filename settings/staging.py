from base import *
import dj_database_url

DEBUG = False

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME':   'heroku_c29de6da34c32c7',
#        'USER': 'b1176416fdcf8d',
#        'PASSWORD': '238a5581',
#        'HOST': 'us-cdbr-iron-east-05.cleardb.net',
#        'PORT': 'heroku_c29de6da34c32c7',
#    }}

DATABASES = {}
DATABASES['default'] = dj_database_url.config('b1176416fdcf8d:238a5581@us-cdbr-iron-east-05.cleardb.net/heroku_c29de6da34c32c7')

# Paypal environment variables
SITE_URL = '/morning-escarpment-70084.herokuapp.com/'
PAYPAL_NOTIFY_URL = '/morning-escarpment-70084.herokuapp.com//a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = '/dynamitedave1-facilitator_api1.hotmail.co.uk/'