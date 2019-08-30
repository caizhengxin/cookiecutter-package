# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
# from pkg_resources import resource_string
# from setuptools import Extension


setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    maintainer="{{ cookiecutter.author_name }}",
    maintainer_email="{{ cookiecutter.email }}",
    url="",
    download_url="",
    license="{{ cookiecutter.open_source_license }}",
    description=__doc__,
    long_description="",
    keywords=[
        "{{ cookiecutter.project_name }}",
        "{{ cookiecutter.project_packet_name }}",
    ],
    zip_safe=False,
    packages=find_packages(),
    # cmdclass="",
    install_requires=[
    ],

    # entry_points={
    #     "console_scripts": [
    #     ],
    #     "gui_scripts": [
    #     ],
    # },

    # package_data={
    #     "": ["*.txt"],
    # },
    include_package_data=True,  # MANIFEST.in
    # exclude_packet_data=[],
    # data_files=[],

    # ext_modules=[]  # 指定扩展模块

    # 指定可执行脚本,安装时脚本会被安装到系统 PATH 路径下
    # scripts=["xxx.py"],

    # package_dir=[],  # 指定哪些目录下的文件被映射到哪个源码包
    # requires=[],  # 指定依赖的其他包
    # provides=[],  # 指定可以为哪些模块提供依赖

    # 指定运行 setup.py 文件本身所依赖的包
    setup_requires=[
        "setuptools",
    ],

    # project_urls = {
    #     "Documentation": "",
    #     "Source Code": "",
    # },

    # dependency_links=[],  # 指定依赖包的下载地址
    # extras_require=[],  # 当前包的高级/额外特性需要依赖的分发包

    platforms="any",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: {{ cookiecutter.open_source_license }} License',
    ],
)


"""
python setup.py build            仅编译，不安装
python setup.py sdist            生成压缩包(zip/tar.gz)
python setup.py bdist_wininst    生成exe
python setup.py bdist_rpm        生成rpm包
python setup.py bdist_wheel      生成wheel

python setup.py bdist --formats= rpm
                                 gztar
                                 bztar
                                 ztar
                                 tar
                                 wininst
                                 zip
"""
