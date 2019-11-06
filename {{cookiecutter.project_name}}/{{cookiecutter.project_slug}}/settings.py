import os


BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# Set Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s:%(lineno)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'error.log',
            'mode': 'a',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 5,
        },
        'control': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        '{{ cookiecutter.project_slug }}': {
            'handlers': ['file', 'control'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
