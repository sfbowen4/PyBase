# Stephen Bowen 2022
import time, requests
from utils import CoinbaseExchangeAuth
from dataclasses import dataclass

class Transfers:
    def __init__(self):
        self.creationTime = time.time()
        self.auth = CoinbaseExchangeAuth()

    # TODO: Test
    """
    Deposits funds from a www.coinbase.com wallet to the specified profile_id.
    """
    def depositFromCoinbaseAccount(self, amount, coinbase_account_id, currency, profile_id=None):
        payload = {
            "amount": f"{amount}",
            "coinbase_account_id": f"{coinbase_account_id}",
            "currency": f"{currency}"
        }
        if profile_id is not None:
            payload["profile_id"] = profile_id
        r = requests.post(self.auth.api_url + 'deposits/coinbase-account', auth=self.auth, json=payload)
        return r.json()

    # TODO: Test
    """
    Deposits funds from a linked external payment method to the specified profile_id
    """
    def depositFromPaymentMethod(self, amount, coinbase_account_id, currency, profile_id=None):
        payload = {
            "amount": f"{amount}",
            "coinbase_account_id": f"{coinbase_account_id}",
            "currency": f"{currency}"
        }
        if profile_id is not None:
            payload["profile_id"] = profile_id
        r = requests.post(self.auth.api_url + 'deposits/coinbase-account', auth=self.auth, json=payload)
        return r.json()

    """
    Gets a list of the user's linked payment methods.
    """
    def getAllPaymentMethods(self):
        r = requests.get(self.auth.api_url + 'payment-methods', auth=self.auth)
        return r.json()

    # TODO: Clean up the optional logic (nil coalesce?)
    """
    Gets a list of in-progress and completed transfers of funds in/out of any of the user's accounts.
    """
    def getAllTransfers(self, profile_id=None, before=None, after=None, limit: int=None, type=None):
        params = "?" if profile_id is not None and before is not None and after is not None and limit is not None and type is not None else ""
        params += f"profile_id={profile_id}&" if profile_id is not None else ""
        params += f"before={before}&" if before is not None else ""
        params += f"after={after}&" if after is not None else ""
        params += f"limit={limit}&" if limit is not None else ""
        params += f"type={type}" if type is not None else ""

        if len(params) > 0:
            params = params[:-1] if params[-1] == "&" else params
        r = requests.get(self.auth.api_url + 'transfers' + params, auth=self.auth)
        return r.json()

transfers = Transfers()
print(transfers.getAllTransfers())
