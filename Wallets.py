# Stephen Bowen 2022
import time, requests
from dataclasses import dataclass
from utils import CoinbaseExchangeAuth

@dataclass(frozen=True)
class Wallet:
    id: str
    name: str
    balance: float
    currency: str
    type: str
    primary: bool
    active: bool
    available_on_consumer: bool
    hold_balance: float
    hold_currency: str

class Wallets:
    def __init__(self):
        self.creationTime = time.time()
        self.auth = CoinbaseExchangeAuth()

    """
    Gets all the user's available Coinbase wallets 
    (These are the wallets/accounts that are used for buying and selling on www.coinbase.com)
    """
    def getAllWallets(self) -> [Wallet]:
        r = requests.get(self.auth.api_url + 'coinbase-accounts', auth=self.auth)
        return [Wallet(wallet['id'], wallet['name'], float(wallet['balance']), wallet['currency'], wallet['type'], bool(wallet['primary']), bool(wallet['active']), bool(wallet['available_on_consumer']), float(wallet['hold_balance']), wallet['hold_currency']) for wallet in r.json()]

    #TODO: See what's going on with unsuccessful request
    """
    Generates a one-time crypto address for depositing crypto.
    """
    def generateCryptoAddress(self, account_id) -> str:
        r = requests.post(self.auth.api_url + f'coinbase-accounts/{account_id}/addresses', auth=self.auth)
        return r.json()