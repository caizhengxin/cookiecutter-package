# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages
# from pkg_resources import resource_string
{% if cookiecutter.use_cython == 'y' %}
from setuptools import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
{% endif %}
{% if cookiecutter.use_cython == 'y' %}
ext_modules = [
    Extension(
        "*",
        sources=["{}/{}".format(directory, file)],
        libraries=["m"],
        # include_dirs=["src"],
        # extra_compile_args=[],
        # extra_link_args=[],
    )
    for directory, dirs, files in os.walk("{{ cookiecutter.project_slug }}")
    for file in files if ".pyx" in file
]
{% endif %}


setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    maintainer="{{ cookiecutter.author_name }}",
    maintainer_email="{{ cookiecutter.email }}",
    url="https://{{ cookiecutter.code_hosting }}.com/{{ cookiecutter.code_hosting_username }}/{{ cookiecutter.project_name }}",
    download_url="https://{{ cookiecutter.code_hosting }}.com/{{ cookiecutter.code_hosting_username }}/{{ cookiecutter.project_name }}.git",
    license="{{ cookiecutter.open_source_license }}",
    description="{{ cookiecutter.description }}",
    long_description="{{ cookiecutter.description }}",
    keywords=[
        "{{ cookiecutter.project_name }}",
        "{{ cookiecutter.project_slug }}",
    ],
    zip_safe=False,
    packages=find_packages(),
    {% if cookiecutter.use_cython == 'y' %}
    cmdclass={
        "build_ext": build_ext
    },
    ext_modules=cythonize(ext_modules),
    {% endif %}
    install_requires=[
    ],

    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.command:main",
        ],
        # "gui_scripts": [
        # ],
    },

    # package_data={
    #     "": ["*.txt"],
    # },
    include_package_data=True,  # MANIFEST.in
    # exclude_packet_data=[],
    # data_files=[],
    # scripts=["xxx.py"],

    # package_dir=[],
    # requires=[],
    # provides=[],

    setup_requires=[
        "setuptools",
        "Cython",
    ],

    project_urls={
        "Documentation": "",
        "Source Code": "https://{{ cookiecutter.project_name }}.readthedocs.io",
    },

    # dependency_links=[],
    # extras_require=[],

    platforms="any",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: {{ cookiecutter.open_source_license }} License',
    ],
)
