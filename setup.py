from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='coinpayments-py',
    version='0.1.0',
    description='CoinPayments API Client for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/OnGridSystems/coinpayments-py',
    author='Roman Nesytov',
    author_email='r.nesytov@ongrid.pro',

    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='coinpayments currencies crypto',

    packages=find_packages(exclude=['tests'])

    install_requires=['requests'],

    python_requires='>=3.4',

    project_urls={
        'Bug Reports': 'https://github.com/OnGridSystems/coinpayments-py/issues',
        'Source': 'https://github.com/OnGridSystems/coinpayments-py',
    },
)
