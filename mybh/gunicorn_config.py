command = '/home/www/pyproject/buhon/env/bin/gunicorn'
pythonpath = '/home/www/pyproject/buhon/mybh'
bind = '0.0.0.0:8001'
workers = 3
user = 'www'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=mybh.settings'
