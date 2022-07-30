# Stephen Bowen 2022
import time, requests
from utils import CoinbaseExchangeAuth
from dataclasses import dataclass

@dataclass(frozen=True)
class Currency:
    id: str
    name: str
    min_size: float
    status: str
    message: str
    max_precision: float
    convertible_to: [str]
    details: {}
    default_network: str
    supported_networks: [{}]

class Currencies:
    def __init__(self):
        self.creationTime = time.time()
        self.auth = CoinbaseExchangeAuth()

    """
    Gets a list of all known currencies.
    Note: Not all currencies may be currently in use for trading.
    """
    def getAllCurrencies(self) -> [Currency]:
        r = requests.get(self.auth.api_url + 'currencies', auth=self.auth)
        return [Currency(currency['id'], currency['name'], float(currency['min_size']), currency['status'], currency['message'], float(currency['max_precision']), currency['convertible_to'], currency['details'], currency['default_network'], currency['supported_networks']) for currency in r.json()]

    """
    Gets a single currency by id.
    """
    def getCurrency(self, currency_id) -> Currency:
        r = requests.get(self.auth.api_url + f'currencies/{currency_id}', auth=self.auth)
        return Currency(r.json()['id'], r.json()['name'], float(r.json()['min_size']), r.json()['status'], r.json()['message'], float(r.json()['max_precision']), r.json()['convertible_to'], r.json()['details'], r.json()['default_network'], r.json()['supported_networks'])