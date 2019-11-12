{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name.capitalize()|replace('-', ' ') }}
{% for _ in cookiecutter.project_name %}={% endfor %}
{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_name }}
{%- endif %}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg
        :target: https://pypi/python.org/pypi/{{ cookiecutter.project_name }}

.. image:: https://img.shields.io/pypi/dm/{{ cookiecutter.project_name }}.svg
        :target: https://pypi/python.org/pypi/{{ cookiecutter.project_name }}
{% if cookiecutter.code_hosting == 'github' %}
.. image:: https://api.travis-ci.com/{{ cookiecutter.code_hosting_username }}/{{ cookiecutter.project_name }}.svg?branch=master
        :target: https://travis-ci.org/{{ cookiecutter.code_hosting_username }}/{{ cookiecutter.project_name }}/?branch=master

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/github/languages/code-size/caizhengxin/{{ cookiecutter.project_name }}
        :target: https://github.com/caizhengxin/{{ cookiecutter.project_name }}
{% endif %}
.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.project_name }}
        :target: https://github.com/caizhengxin/{{ cookiecutter.project_name }}/blob/master/LICENSE

{{ cookiecutter.description }}
{% if is_open_source %}
* Github repo: https://{{ cookiecutter.code_hosting }}.com/{{ cookiecutter.code_hosting_username }}/{{ cookiecutter.project_name }}
* Documentation: https://{{ cookiecutter.project_name }}.readthedocs.io
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}
Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `caizhengxin/cookiecutter-package`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`caizhengxin/cookiecutter-package`: https://github.com/caizhengxin/cookiecutter-package
