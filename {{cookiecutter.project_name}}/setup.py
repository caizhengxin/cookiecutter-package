import os
import sys
{% if cookiecutter.use_cython == 'y' %}import glob{% endif %}

from setuptools import setup, find_packages
{% if cookiecutter.use_cython == 'y' %}from setuptools import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
{% endif %}

with open('README.rst') as f:
    long_description = f.read()


def pip_install(packet_name: str) -> None:
    """
    Install packet

    Args:
        param packet_name (str): Packet name.

    Returns:
        void: None
    """

    os.system(f"{sys.executable}" -m pip install {packet_name})


def read_requirements(path):
    """
    Read requirements

    :param path: path
    """

    requires = []

    with open(path) as f:
        install_requires = f.read().split("\n")

        for ir in install_requires:
            if "-r" in ir:
                path = os.path.join(os.path.split(path)[0], ir.split(" ")[1])
                requires.extend(read_requirements(path))
            elif "git" not in ir:
                ir and requires.append(ir)

    return requires
{% if cookiecutter.use_cython == 'y' %}

# local or publish
USE_CYTHON = True if glob.glob("{{ cookiecutter.project_slug }}/*.pyx") else False
ext = '.pyx' if USE_CYTHON else '.c'


ext_modules = [
    Extension(
        "{}/{}".format(directory, file.split(".")[0]).replace("/", "."),
        sources=["{}/{}".format(directory, file)],
        libraries=["m"],
        # include_dirs=["src"],
        # extra_compile_args=[],
        # extra_link_args=[],
    )
    for directory, dirs, files in os.walk("{{ cookiecutter.project_slug }}")
    for file in files if ext in file and ".pyc" not in file
]

ext_modules = cythonize(ext_modules) if USE_CYTHON else ext_modules

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
    long_description=long_description,
    keywords=[
        "{{ cookiecutter.project_name }}",
        "{{ cookiecutter.project_slug }}",
    ],
    zip_safe=False,
    packages=find_packages(),
    {% if cookiecutter.use_cython == 'y' %}cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,{% endif %}
    install_requires=read_requirements("requirements/publish.txt"),
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.cli:main",
        ],
    },
    include_package_data=True,  # MANIFEST.in
    setup_requires=[
        "setuptools",
    ],
    project_urls={
        "Documentation": "https://{{ cookiecutter.project_name }}.readthedocs.io",
        "Source Code": "https://{{ cookiecutter.code_hosting }}.com/{{ cookiecutter.code_hosting_username }}/{{ cookiecutter.project_name }}",
    },
    platforms="any",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: {{ cookiecutter.open_source_license }} License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
)
