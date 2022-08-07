# Stephen Bowen 2022
import time, requests
from utils import CoinbaseExchangeAuth
from dataclasses import dataclass

@dataclass()
class Fee:
    maker_fee_rate: float
    taker_fee_rate: float
    usd_volume: float

class Fees:
    def __init__(self):
        self.creationTime = time.time()
        self.auth = CoinbaseExchangeAuth()

    """
    Get fees rates and 30 days trailing volume.
    """
    def getFees(self):
        r = requests.get(self.auth.api_url + 'fees', auth=self.auth).json()
        return Fee(r['maker_fee_rate'], r['taker_fee_rate'], r['usd_volume'] if r['usd_volume'] is not None else 0.0)

fees = Fees()
print(fees.getFees().usd_volume)