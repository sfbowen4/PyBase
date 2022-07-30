# Stephen Bowen 2022
import time, requests
from dataclasses import dataclass
from utils import CoinbaseExchangeAuth


@dataclass(frozen=True)
class Account:
    id: str
    currency: str
    balance: float
    hold: float
    available: float
    profile_id: str
    trading_enabled: bool


class Accounts:
    def __init__(self):
        self.creationTime = time.time()
        self.auth = CoinbaseExchangeAuth()

    """
    Get a list of trading accounts from the profile of the API key.
    """
    def getAllAccounts(self) -> [Account]:
        r = requests.get(self.auth.api_url + 'accounts', auth=self.auth)
        return [Account(account['id'], account['currency'], float(account['balance']), float(account['hold']),
                        float(account['available']), account['profile_id'], account['trading_enabled']) for account in
                r.json()]

    """
    Information for a single account. Use this endpoint when you know the account_id. 
    API key must belong to the same profile as the account.
    """
    def getAccountById(self, account_id) -> Account:
        r = requests.get(self.auth.api_url + f'accounts/{account_id}', auth=self.auth)
        account = r.json()
        return Account(account['id'], account['currency'], float(account['balance']), float(account['hold']),
                       float(account['available']), account['profile_id'], account['trading_enabled'])

    # TODO: Implement pagination for requests
    """
    List the holds of an account that belong to the same profile as the API key. 
    Holds are placed on an account for any active orders or pending withdraw requests. 
    As an order is filled, the hold amount is updated. If an order is canceled, any remaining hold is removed. 
    For withdrawals, the hold is removed after it is completed.
    """
    def getAccountHolds(self, account_id):
        r = requests.get(self.auth.api_url + f'accounts/{account_id}/holds', auth=self.auth)
        return r.json()

    # TODO: Implement pagination for requests
    """
    Lists ledger activity for an account. 
    This includes anything that would affect the accounts balance - transfers, trades, fees, etc.
    """
    def getAccountLedger(self, account_id):
        r = requests.get(self.auth.api_url + f'accounts/{account_id}/ledger', auth=self.auth)
        return r.json()

    # TODO: Implement pagination for requests
    """
    Lists past withdrawals and deposits for an account.
    """
    def getAccountTransfers(self, account_id):
        r = requests.get(self.auth.api_url + f'accounts/{account_id}/transfers', auth=self.auth)
        return r.json()
