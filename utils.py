# Stephen Bowen 2022
import json, hmac, hashlib, time, base64
from requests.auth import AuthBase

CREDENTIALS_URL = './credentials.json'

# Authentication Object
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self):
        #Coinbase Pro API URL
        with open(CREDENTIALS_URL) as f:
            credentials = json.load(f)
            self.api_url = 'https://api.pro.coinbase.com/'
            self.__api_key = credentials['api_key']
            self.__secret_key = credentials['api_secret']
            self.__passphrase = credentials['passphrase']

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or b'').decode()
        hmac_key = base64.b64decode(self.__secret_key)
        signature = hmac.new(hmac_key, message.encode(), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode()

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.__api_key,
            'CB-ACCESS-PASSPHRASE': self.__passphrase,
            'Content-Type': 'application/json'
        })
        return request