from blog.setting import *
SECRET_KEY = 'django-insecure-njm&_a)k3v%f7op1i--m1-2tb%^q8$oh5#qwr-w)@l#(-*4j2i'
DEBUG=True
ALLOWED_HOSTS=[]
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


SITE_ID=2
MEDIA_ROOT = BASE_DIR / 'media'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/
STATIC_URL = 'static/'