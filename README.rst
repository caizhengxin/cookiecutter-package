====================
Cookiecutter Package
====================

.. image:: https://api.travis-ci.com/caizhengxin/cookiecutter-package.svg
    :target: https://travis-ci.org/caizhengxin/cookiecutter-package

.. image:: https://img.shields.io/github/languages/code-size/caizhengxin/cookiecutter-package
    :target: https://github.com/caizhengxin/cookiecutter-package

.. image:: https://img.shields.io/pypi/l/cookiecutter-package
    :target: https://github.com/caizhengxin/cookiecutter-package/blob/master/LICENSE

Cookiecutter_ template for a Python package.

* Github repo: https://github.com/caizhengxin/cookiecutter-package/
* Documentation: https://cookiecutter-package.readthedocs.io/
* Free software: BSD lincense

Features
--------

* Cython_
* Sphinx_ + ReadTheDocs_
* Travis-CI_
* Pre-commit_
* Tox_
* Bumpversion_
* Pytest_
* Flake8_
* Github/Gitee/Gitlab
* Logging_

Installation
------------

.. code-block:: console

	$ pip3 install cookiecutter
	$ cookiecutter https://github.com/caizhengxin/cookiecutter-package.git

Pypi
----

Setting ``vim ~/.pypirc``::

    [distutils]
    index-server=pypi

    [pypi]
    username=
    password=

.. code-block:: console

    $ pip3 install twine
    $ python3 setup sdist
    $ twine upload dist/*

Demo
----

* python-libpcap_

.. _Cython: https://cython.org/
.. _Sphinx: http://sphinx-doc.org/
.. _Travis-CI: http://travis-ci.org/
.. _Pre-commit: https://pre-commit.com/
.. _Tox: http://testrun.rog/tox/
.. _Bumpversion: https://github.om/peritus/bumpversion/
.. _ReadTheDocs: https://readthedocs.io/
.. _Pytest: http://www.pytest.org/en/latest/
.. _Flake8: https://gitlab.com/pycqa/flake8/
.. _PyPi: https://pypi.python.org/pypi/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Logging: https://docs.python.org/3.6/library/logging.html
.. _python-libpcap: https://github.com/caizhengxin/python-libpcap
