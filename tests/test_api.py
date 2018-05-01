import requests
from unittest import TestCase
from unittest.mock import patch, Mock
from coinpayments import CoinPaymentsAPI


class TestAPI(TestCase):
    test_pub_key = 'a2308cc5846557e67b377623dbd2ce939a5fd997ab8302e2295ae65ba1d757e7'
    test_priv_key = '508055A03f88Cd1217f6B724878Ff238d43E961d89E5cCb5be7182F3713613c6'

    def setUp(self):
        self.api = CoinPaymentsAPI(public_key=self.test_pub_key,
                                   private_key=self.test_priv_key)

    def test_send_request(self):
        response_mock = Mock()

        with patch.object(requests, 'post', return_value=response_mock) as mocked_requests:
            self.api.get_deposit_address(currency='BTC')

        mocked_requests.assert_called_once_with(
            'https://www.coinpayments.net/api.php',
            data='version=1&key=a2308cc5846557e67b377623dbd2ce939a5fd997ab8302e2295ae65ba1d757e7&cmd=get_deposit_address&format=json&currency=BTC',
            headers={
                'HMAC': '32c6cdc253046073c369eed253a15bc8ff78c17d62b28c124eb5dfac148b02740e8849887657439369c24fad8a611f58f35d92a9a433804c7b16c7ed38314f6d',
                'Content-Type': 'application/x-www-form-urlencoded'
            })

        assert response_mock.json.call_count == 1

    def test_check_signature(self):
        data = 'version=1&key=a2308cc5846557e67b377623dbd2ce939a5fd997ab8302e2295ae65ba1d757e7&cmd=rates&format=json'
        signature = '09f27bea915ba042a50e1f54bc5988ad07cf4c6d5b375e660ca1109f8d451fd28cc96e8779c9d633e181e400cf7af61a61fbc0d326ac1e5a6ea77e7c5caa9fd9'

        self.assertTrue(self.api.check_signature(data, signature))
