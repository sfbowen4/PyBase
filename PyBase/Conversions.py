# Stephen Bowen 2022
import time, requests
from utils import CoinbaseExchangeAuth

class Conversions:
    def __init__(self):
        self.creationTime = time.time()
        self.auth = CoinbaseExchangeAuth()

    # TODO: Test
    """
    Converts funds from from currency to to currency. 
    Funds are converted on the from account in the profile_id profile.
    """
    def convertCurrency(self, from_currency, to_currency, amount, profile_id=None, nonce=None):
        payload = {
            "from": f"{from_currency}",
            "to": f"{to_currency}",
            "amount": f"{amount}"
        }
        if profile_id is not None:
            payload["profile_id"] = f"{profile_id}"
        if nonce is not None:
            payload["nonce"] = f"{nonce}"
        r = requests.post(self.auth.api_url + 'conversions', auth=self.auth, json=payload)
        return r.json()

    # TODO: Test
    """
    Gets a currency conversion by id (i.e. USD -> USDC).
    """
    def getConversion(self, conversion_id, profile_id=None):
        r = requests.get(self.auth.api_url + f'conversions/{conversion_id}' + (f'?profile_id={profile_id}' if profile_id is not None else ''), auth=self.auth)
        return r.json()