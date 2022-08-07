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
        params = "?" if profile_id is not None or before is not None or after is not None or limit is not None or type is not None else ""
        params += f"profile_id={profile_id}&" if profile_id is not None else ""
        params += f"before={before}&" if before is not None else ""
        params += f"after={after}&" if after is not None else ""
        params += f"limit={limit}&" if limit is not None else ""
        params += f"type={type}" if type is not None else ""

        if len(params) > 0:
            params = params[:-1] if params[-1] == "&" else params
        r = requests.get(self.auth.api_url + 'transfers' + params, auth=self.auth)
        return r.json()

    """
    Get information on a single transfer.
    """
    def getTransfersById(self, transfer_id):
        r = requests.get(self.auth.api_url + f'transfers/{transfer_id}', auth=self.auth)
        return r.json()

    def withdrawToCoinbaseAccount(self, amount, coinbase_account_id, currency, profile_id=None):
        payload = {
            "amount": f"{amount}",
            "coinbase_account_id": f"{coinbase_account_id}",
            "currency": f"{currency}"
        }
        if profile_id is not None:
            payload["profile_id"] = profile_id
        r = requests.post(self.auth.api_url + 'withdrawals/coinbase-account', auth=self.auth, json=payload)
        return r.json()

    """
    Withdraws funds from the specified profile_id to an external crypto address
    """
    def withdrawToCryptoAddress(self, amount, currency, crypto_address, profile_id=None, destination_tag=None, no_destination_tag: bool=None, two_factor_code=None, nonce: int=None, network=None, add_network_fee_to_total: bool=None):
        payload = {
            "amount": amount,
            "currency": currency,
            "crypto_address": crypto_address,
        }
        if profile_id is not None:
            payload["profile_id"] = profile_id
        if destination_tag is not None:
            payload["destination_tag"] = destination_tag
        if no_destination_tag is not None:
            payload["no_destination_tag"] = no_destination_tag
        if two_factor_code is not None:
            payload["two_factor_code"] = two_factor_code
        if nonce is not None:
            payload["nonce"] = nonce
        if network is not None:
            payload["network"] = network
        if add_network_fee_to_total is not None:
            payload["add_network_fee_to_total"] = add_network_fee_to_total
        r = requests.post(self.auth.api_url + 'withdrawals/crypto', auth=self.auth, json=payload)
        return r.json()

    """
    Gets the fee estimate for the crypto withdrawal to crypto address
    """
    def getWithdrawalFeeEstimate(self, currency=None, crypto_address=None):
        params = "?" if currency is not None or crypto_address is not None else ""
        params += f"currency={currency}&" if currency is not None else ""
        params += f"crypto_address={crypto_address}&" if crypto_address is not None else ""

        if len(params) > 0:
            params = params[:-1] if params[-1] == "&" else params
        r = requests.get(self.auth.api_url + 'withdrawals/fee-estimate' + params, auth=self.auth)
        return r.json()

    """
    Withdraws funds from the specified profile_id to a linked external payment method
    """
    def withdrawToPaymentMethod(self, amount, payment_method_id, currency, profile_id=None):
        payload = {
            "amount": amount,
            "payment_method_id": payment_method_id,
            "currency": currency,
        }
        if profile_id is not None:
            payload["profile_id"] = profile_id
        r = requests.post(self.auth.api_url + 'withdrawals/payment-method', auth=self.auth, json=payload)
        return r.json()

