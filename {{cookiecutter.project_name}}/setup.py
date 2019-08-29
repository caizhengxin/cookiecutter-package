# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-08-29 16:10:39
# @Last Modified by:   caizhengxin@bolean.com.cn
# @Last Modified time: 2019-08-29 16:12:52
try:
    from setuptools import Extension, setup, find_packages
except ImportError as e:
    from distutils.core import Extension, setup, find_packages


__version__ = "0.0.1"


setup(
    name="bolean-replay",
    version=__version__,
    author='JanKin Cai',
    author_email='caizhengxin@bolean.com.cn',
    maintainer="JanKin Cai",
    maintainer_email='caizhengxin@bolean.com.cn',
    url="https://gitee.com/BoleanTech/bolean_replay",
    download_url="https://gitee.com/BoleanTech/bolean_replay.git",
    description=__doc__,
    zip_safe=False,
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    include_package_data=True,
)
