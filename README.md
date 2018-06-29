# CoinPayments API Client
[![Build Status](https://travis-ci.org/OnGridSystems/coinpayments-py.svg?branch=master)](https://travis-ci.org/OnGridSystems/coinpayments-py)
[![PyPI version](https://badge.fury.io/py/coinpayments-py.svg)](https://badge.fury.io/py/coinpayments-py)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/coinpayments-py.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Use this library to easily interact with [CoinPayments](https://www.coinpayments.net) crypto/coin payment gateway API directly from your Python 3 application. 

## Documentation

* [API Documentation](https://www.coinpayments.net/merchant-tools-api) on official website.

## Installation

Use pip to install coinpayments-py:

```
pip install coinpayments-py
```

## Basic Usage

Initialize api object

```
>>> from coinpayments import CoinPaymentsAPI

>>> api = CoinPaymentsAPI(public_key='your_api_public_key',
                          private_key='your_api_private_key')
```

Call any CoinPayments API method as `api` object method with corresponding arguments
```
>>> api.rates()
{'error': 'ok', 'result': 'LTCT': {'balance': 839700000, 'balancef': '8.39700000', 'status': 'available', 'coin_status': 'online'}}}

>>> api.get_callback_address(currency='BTC', ipn_url='http://example.com')
{'error': 'ok', 'result': {'address': '36v6r1XuaWPtrTuhF8iq8AfBzPS8D4eios'}}
```

Also, you can check IPN HMAC signature using `check_signature` method
```
>>> from coinpayments import CoinPaymentsAPI
>>> api = CoinPaymentsAPI(public_key=None,
                          private_key='your_ipn_secret_key')
>>> api.check_signature('ipn_message', 'ipn signautre')
False
```

## Contributing

Contributions are welcome. You can learn how from this free series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).
