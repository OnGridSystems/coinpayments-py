# CoinPayments API Client

[CoinPayments](https://www.coinpayments.net) | [API Documentation](https://www.coinpayments.net/merchant-tools-api)

This library will let you to easily interact with CoinPayments API directly from your Python application.

## Installation

To install coinpayments-py, simply use pip:

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

Also you can check IPN HMAC signature using `check_signature` method
```
>>> from coinpayments import CoinPaymentsAPI
>>> api = CoinPaymentsAPI(public_key=None,
                          private_key='your_ipn_secret_key')
>>> api.check_signature('ipn_message', 'ipn signautre')
False
```

## Contributing

Contributions are welcome and will be fully credited.
Contributions can be made via a Pull Request.
