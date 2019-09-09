# -*- coding: utf-8 -*-
import logging.config

from {{ cookiecutter.project_slug }} import settings


__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.author_name }}"


logging.config.dictConfig(settings.LOGGING)
