# Stephen Bowen 2022
import time, requests
from utils import CoinbaseExchangeAuth

class AddressBook:
    def __init__(self):
        self.creationTime = time.time()
        self.auth = CoinbaseExchangeAuth()

    """
    Get all addresses stored in the address book.
    """
    def getAddressBook(self):
        r = requests.get(self.auth.api_url + 'address-book', auth=self.auth)
        return r.json()