import requests
import hmac
import hashlib
from collections import OrderedDict
from urllib.parse import urlencode


class CoinPaymentsAPI:
    api_url = 'https://www.coinpayments.net/api.php'
    api_version = 1

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def _build_params(self, command, **kwargs):
        base_params = [('version', self.api_version),
                       ('key', self.public_key),
                       ('cmd', command),
                       ('format', 'json')]

        return urlencode(OrderedDict(base_params + sorted(kwargs.items())))

    def _build_signature(self, params):
        if not isinstance(params, bytes):
            params = bytearray(params, 'utf-8')

        byte_private_key = bytearray(self.private_key, 'utf-8')

        return hmac.new(byte_private_key, params, hashlib.sha512).hexdigest()

    def check_signature(self, data, signature):
        actual_signature = self._build_signature(data)

        return actual_signature == signature

    def send_api_request(self, command, **kwargs):
        params = self._build_params(command, **kwargs)
        signature = self._build_signature(params)
        headers = {'HMAC': signature,
                   'Content-Type': 'application/x-www-form-urlencoded'}

        return requests.post(self.api_url,
                             data=params,
                             headers=headers).json()

    def get_basic_info(self):
        command = 'get_basic_info'

        return self.send_api_request(command)

    def rates(self, **kwargs):
        command = 'rates'

        return self.send_api_request(command, **kwargs)

    def balances(self, **kwargs):
        command = 'balances'

        return self.send_api_request(command, **kwargs)

    def get_deposit_address(self, **kwargs):
        command = 'get_deposit_address'

        return self.send_api_request(command, **kwargs)

    def create_transaction(self, **kwargs):
        command = 'create_transaction'

        return self.send_api_request(command, **kwargs)

    def get_callback_address(self, **kwargs):
        command = 'get_callback_address'

        return self.send_api_request(command, **kwargs)

    def get_tx_info_multi(self, **kwargs):
        command = 'get_tx_info_multi'

        return self.send_api_request(command, **kwargs)

    def get_tx_info(self, **kwargs):
        command = 'get_tx_info'

        return self.send_api_request(command, **kwargs)

    def get_tx_ids(self, **kwargs):
        command = 'get_tx_ids'

        return self.send_api_request(command, **kwargs)

    def create_transfer(self, **kwargs):
        command = 'create_transfer'

        return self.send_api_request(command, **kwargs)

    def create_withdrawal(self, **kwargs):
        command = 'create_withdrawal'

        return self.send_api_request(command, **kwargs)

    def create_mass_withdrawal(self, **kwargs):
        command = 'create_mass_withdrawal'

        return self.send_api_request(command, **kwargs)

    def convert(self, **kwargs):
        command = 'convert'

        return self.send_api_request(command, **kwargs)

    def get_withdrawal_history(self, **kwargs):
        command = 'get_withdrawal_history'

        return self.send_api_request(command, **kwargs)

    def get_withdrawal_info(self, **kwargs):
        command = 'get_withdrawal_info'

        return self.send_api_request(command, **kwargs)

    def get_conversion_info(self, **kwargs):
        command = 'get_conversion_info'

        return self.send_api_request(command, **kwargs)
