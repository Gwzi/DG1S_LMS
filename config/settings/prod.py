from .base import *

ALLOWED_HOSTS = ['34.121.225.165', '12th.dg1s.o-r.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
MIDDLEWARE += ['django.middleware.clickjacking.XFrameOptionsMiddleware', ]
X_FRAME_OPTIONS = 'http://12th.dg1s.o-r.kr/'
